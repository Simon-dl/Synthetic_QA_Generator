from paths_handler import get_full_path
import requests
import json




create_url = "http://localhost:11434/api/create"
generate_url = "http://localhost:11434/api/generate"
delete_url = "http://localhost:11434/api/delete"

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

def delete_model(model_name: str):
    """
    Deletes a model using the provided model name.
    """
    data = {
        "model": model_name
    }
    print(data)
    response = requests.post(delete_url, json=data)
    out = decode_response(response,case="delete")
    if out:
        print(f"Model {model_name} deleted successfully")
    else:
        print(f"Error: model {model_name} not found, check ollama list")
        

def unload_model(model_name: str):
    """
    Unloads a model using the provided model name.
    """
    data = {
        "model": "llama3.2",
        "messages": [],
        "keep_alive": 0
        }
    response = requests.post(generate_url, json=data)
    decode_response(response,case="unload")


def generate_text(model_name: str, prompt: str):
    """
    Generates text using the provided model name and prompt.
    """
    data = {
            "model": model_name,
            "prompt": prompt,
            "stream": True
        }
    response = requests.post(generate_url, json=data)
    decode_response(response,case="generate")
    

    



def decode_response(response, case: str):
    """
    Decodes the response from the server. Return different values depending on the case.

    Thanks https://github.com/pdichone/ollama-fundamentals/blob/main/start-1.py
    for the generate case
    """
    if case == "delete":
        if response.status_code == 200:
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
        
        elif case == "unload":
            total_response = response.json()
            model_name = total_response["model"]
            if total_response["done"] and total_response["done_reason"] == "unload":
                print(f"Model {model_name} unloaded successfully")

        elif case == "generate":
            print("Generated Text:", end=" ", flush=True)
            # Iterate over the streaming response
            for line in response.iter_lines():
                if line:
                    # Decode the line and parse the JSON
                    decoded_line = line.decode("utf-8")
                    result = json.loads(decoded_line)
                    # Get the text from the response
                    generated_text = result.get("response", "")
                    print(generated_text, end="", flush=True)
    else:
        print(f"Error: {response.status_code}")
        print(response.text)


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
        with open(file_path, 'r', encoding='utf-16') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading file {file_path}: {str(e)}")
    

generate_text("pls-work:latest", "how do I peel a banana?")
#create_model("pls-work", "src/test-modelfile")
#delete_model("pls-work:latest")
