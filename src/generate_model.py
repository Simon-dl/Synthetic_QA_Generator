import subprocess
import sys
import os
from paths_handler import get_full_path

def create_script(script_path, contents):
    """
    Create a PowerShell script file with the specified contents
    """
    try:
        # Write the contents to the file (no shebang needed for Windows)
        with open(script_path, 'w') as file:
            file.write(contents)
            
        print(f"Successfully created script at {script_path}")
        return True
        
    except Exception as e:
        print(f"Error creating script: {e}")
        return False
    

def run_script(script_path):
    try:
        # On Windows
        result = subprocess.run(['powershell', '-File', script_path], 
                              check=True, 
                              text=True, 
                              capture_output=True)
        
        print("Script output:", result.stdout)
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error running script: {e}")
        print("Script error output:", e.stderr)
        return None
    

def generate_model(model_name, model_file):
    """
    This function generates a PowerShell script to create a model using Ollama.
    """
    
    script_contents = f"""ollama create {model_name} --file {model_file}"""
    #script_contents = f"""ollama help run"""
    


    script_name = f"utils/shell_scripts/{model_name} _script.ps1"
    script_path = get_full_path(script_name)

    print(f"Full path: {script_path}")
    
    #create_script(script_path, script_contents)
    run_script(script_path)

generate_model("hoggwash-higgle", "test-modelfile")

# Create the script with .ps1 extension for PowerShell
#script_path = "example_script.ps1"
#create_script(script_path, script_contents)

# Get the full path and run the script
#full_path = paths_handler.get_full_path(script_path)
#run_script(full_path)