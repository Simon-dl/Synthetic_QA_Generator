from paths_handler import get_full_path
import requests
import json




create_url = "http://localhost:11434/api/create"
generate_url = "http://localhost:11434/api/generate"

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
    decode_response(response)


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
    decode_response(response)
    

    



def decode_response(response):
    if response.status_code == 200:
        for line in response.iter_lines():
            if line:
                result = json.loads(line.decode('utf-8'))
                print(result)
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