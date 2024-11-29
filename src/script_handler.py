import subprocess

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