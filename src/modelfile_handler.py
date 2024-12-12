import ollama
import pathlib
import os
from paths_handler import get_full_path
from script_handler import create_script, run_script




def create_and_move_modelfile(base_model_name, new_model_name):
    make_modelfile_script = f"""
    try {{
        ollama show {base_model_name} --modelfile | Out-File -FilePath {new_model_name}-modelfile -Encoding utf8 
        Write-Host \"Successfully created {new_model_name}-modelfile\"
    }} catch {{
        Write-Error \"Failed to create modelfile: $_\"
        exit 1
    }}
    """
    create_script(f"{new_model_name}-modelfile-script.ps1", make_modelfile_script)
    script_path = get_full_path(f"{new_model_name}-modelfile-script.ps1")
    run_script(script_path)

    # Get paths
    new_modelfile_path = f"{new_model_name}-modelfile"
    new_script_path = f"{new_model_name}-modelfile-script.ps1"
    full_modelfile_path = get_full_path(new_modelfile_path)
    full_script_path = get_full_path(new_script_path)

    modelfile_destination_path = get_full_path("utils/model_files")
    script_destination_path = get_full_path("utils/scripts")

    # Create destination directorys if it doesn't exist
    os.makedirs(modelfile_destination_path, exist_ok=True)
    os.makedirs(script_destination_path, exist_ok=True)

    # Move the modelfile and script creating it their respective folders
    try:
        destination_file = os.path.join(modelfile_destination_path, new_modelfile_path)
        os.replace(full_modelfile_path, destination_file)
        print(f"Successfully moved modelfile to {destination_file}")
    except Exception as e:
        print(f"Error moving modelfile: {e}")
        return None
    
    try:
        script_destination_file = os.path.join(script_destination_path, new_script_path)
        os.replace(full_script_path, script_destination_file)
        print(f"Successfully moved script to {script_destination_file}")
    except Exception as e:
        print(f"Error moving modelfile: {e}")
        return None
    
    return destination_file

"""modelfile will only work if the system has qoute around text with no qoute marks in text or around the system prompt,
so if you want to use a modelfile, you must remove the qoutes from the system prompt
the code below works with dolphin-mistral models, it did not work with llama3.2. 
so you will have to update the code to work with other models.
"""

def update_system_text(filename, new_system_text):
    """
    Updates the system text in the modelfile, works with dolphin-mistral models
    """
    full_filename = get_full_path(filename)
    try:
        # Read all lines from file
        with open(full_filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Find SYSTEM line and remove extra quotation marks
        system_found = False
        for i, line in enumerate(lines):
            if line.strip().startswith('SYSTEM "'):
                
                # Replace the line without the extra quotes
                lines[i] = f'SYSTEM """{new_system_text}"""\n'
                
                # Remove the following line if it only contains a quotation mark
                if i + 1 < len(lines) and lines[i + 1].strip() == '"':
                    lines.pop(i + 1)
                
                system_found = True
                break
        
        # If SYSTEM not found, add it at end
        if not system_found:
            system_line = f'SYSTEM """{new_system_text}"""\n'
            insert_position = len(lines)
            lines.insert(insert_position, system_line)
        
        # Write back to file
        with open(full_filename, 'w', encoding='utf-8') as file:
            file.writelines(lines)
            
        return True
    except FileNotFoundError:
        print(f"Error: File {full_filename} not found")
        return False
    except Exception as e:
        print(f"Error updating file: {e}")
        return False
    

def update_tempurature(filename, new_temp):
    """
    Updates the temperature in the modelfile
    """
    full_filename = get_full_path(filename)
    print(full_filename)
    try:
        # Read all lines from file
        with open(full_filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Find SYSTEM line
        temp_found = False
        for i, line in enumerate(lines):
            if "PARAMETER temperature" in line.strip():
                lines[i] = f'PARAMETER temperature {new_temp}\n'
                temp_found = True
                break
        
        # If temperature not found, add it at the end
        if not temp_found:
            temp_line = f'PARAMETER temperature {new_temp}\n'

            insert_position = len(lines)  
    
            lines.insert(insert_position, temp_line)
        
        # Write back to file
        with open(full_filename, 'w', encoding='utf-8') as file:
            file.writelines(lines)
            
        return True
    except FileNotFoundError:
        print(f"Error: File {full_filename} not found")
        return False
    except Exception as e:
        print(f"Error updating file: {e}")
        return False



