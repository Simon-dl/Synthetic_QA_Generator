from paths_handler import get_full_path
import requests
import json

create_url = "http://localhost:11434/api/create"
generate_url = "http://localhost:11434/api/generate"
delete_url = "http://localhost:11434/api/delete"
show_url = "http://localhost:11434/api/show"
pull_url = "http://localhost:11434/api/pull"

def pull_model(model_name: str):
    """
    Pulls a model from ollama using the provided model name.
    """
    data = {
        "model": model_name
    }
    response = requests.post(pull_url, json=data)
    out = decode_response(response,case="pull")
    if out:
        print(f"Model {model_name} pulled successfully, see ollama list")
    else:
        print(f"Error: model {model_name} not found, check ollama website for proper model name")


def create_model(model_name: str, modelfile_path: str):
    """
    Creates a new model using the provided model name and modelfile.

    Args:
        model_name (str): Name of the model to be created
        modelfile_path (str): Path to the modelfile to be used

    Will show up as model name in ollama list.
    """
    full_path = get_full_path(modelfile_path)
    output = read_file_contents(full_path)
    data = {
            "model": model_name,
            "modelfile": output,
        }
    response = requests.post(create_url, json=data)
    out = decode_response(response,case="create")
    if out:
        print(f"Model {model_name} created successfully")
        return model_name



def show_model(model_name: str):
    data = {
        "model": model_name
    }
    response = requests.post(show_url, json=data)
    out = decode_response(response,case="show")
    return out
        

def unload_model(model_name: str):
    """
    Unloads a model using the provided model name.
    """
    data = {
        "model": f"{model_name}",
        "messages": [],
        "keep_alive": 0
        }
    response = requests.post(generate_url, json=data)
    decode_response(response,case="unload")


def generate_text(model_name: str, prompt: str):
    """
    Generates text using the provided model name and prompt.

    returns the generated text as a string.
    """
    data = {
            "model": model_name,
            "prompt": prompt,
        }
    response = requests.post(generate_url, json=data)
    text = decode_response(response,case="generate")
    return text
    



def decode_response(response, case: str):
    """
    Decodes the response from the server. Return different values depending on the case.

    Thanks https://github.com/pdichone/ollama-fundamentals/blob/main/start-1.py
    for the generate case starter code
    """
    if case == "pull":
        if response.status_code == 200:
            for line in response.iter_lines():
                if line:
                    json_response = json.loads(line.decode('utf-8'))
                    print(json_response)
            return True
        else:
            print(f"Error: {response.status_code}")
            return False
        
        
    elif response.status_code == 200:
        if case == "create":
            for line in response.iter_lines():
                if line:
                    # Decode the bytes to string and parse JSON
                    json_response = json.loads(line.decode('utf-8'))
                    status = json_response["status"]
                    if status == "success":
                        return True
                    
        elif case == "show":
            for line in response.iter_lines():
                if line:
                    json_response = json.loads(line.decode('utf-8'))
                    if "model_info" in json_response:
                        return True
                    else:
                        return False
        
        elif case == "unload":
            total_response = response.json()
            model_name = total_response["model"]
            if total_response["done"] and total_response["done_reason"] == "unload":
                print(f"Model {model_name} unloaded successfully")

        elif case == "generate":
            # Initialize empty string for collecting response
            
            full_text = ""
            for line in response.iter_lines():
                if line:
                    json_response = json.loads(line.decode('utf-8'))
                    individual_text = json_response["response"]
                    full_text += individual_text
                    
            
            return full_text
    else:
        print(f"Error: {response.status_code} {response.text}")

        return False


def read_file_contents(file_path: str) -> str:
    """
    Reads the contents of a file and returns it as a string.
    
    Args:
        file_path (str): Path to the file to be read
        
    Returns:
        str: Contents of the file
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        IOError: If there's an error reading the file
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading file {file_path}: {str(e)}")
    

