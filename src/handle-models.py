import ollama
import pathlib
import os

# Use a raw string or forward slashes for the path
test_file = r"src/test-modelfile"

def get_full_path(relative_path):
    """
    Convert a relative path to a full absolute path using the current working directory
    
    Args:
        relative_path (str): The relative path to convert
        
    Returns:
        str: The full absolute path
    """
    try:
        # Get the current working directory
        cwd = os.getcwd()
    
        # Join the current directory with the relative path
        full_path = os.path.join(cwd, relative_path)
       
        # Normalize the path (resolves any '..' or '.' in the path)
        full_path = os.path.normpath(full_path)
        
        # Convert to absolute path (resolves any symlinks)
        full_path = os.path.abspath(full_path)
        return full_path
        
    except Exception as e:
        print(f"Error creating full path: {e}")
        return None

def update_system_text(filename, new_system_text):
    try:
        # Read all lines from file
        with open(filename, 'r', encoding='utf-16') as file:
            lines = file.readlines()
        
        # Find and replace the SYSTEM line
        for i, line in enumerate(lines):
            if "SYSTEM" in line:
                lines[i] = f'SYSTEM """{new_system_text}"""\n'
                break
        
        # Write back to file
        with open(filename, 'w', encoding='utf-16') as file:
            file.writelines(lines)
            
        return True
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return False
    except Exception as e:
        print(f"Error updating file: {e}")
        return False

full_path = get_full_path(test_file)
print(full_path)

system_text = update_system_text(full_path, "keep trying it")
print(system_text)
"""
response = ollama.chat(model="lazy-llama",
                       messages=[
                           {
                            "role": "user", 
                            "content": "What is the capital of France?"
                            }
                           ])
print(response)
"""

#ollama.create(model="testmodel", modelfile="gen-modelfile")