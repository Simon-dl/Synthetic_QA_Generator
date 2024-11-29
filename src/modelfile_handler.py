import ollama
import pathlib
import os
from paths_handler import get_full_path
from script_handler import create_script, run_script




def create_and_move_modelfile(base_model_name, new_model_name):
    make_modelfile_script = f"""
    try {{
        ollama show {base_model_name} --modelfile > {new_model_name}-modelfile
        Write-Host \"Successfully created {new_model_name}-modelfile\"
    }} catch {{
        Write-Error \"Failed to create modelfile: $_\"
        exit 1
    }}
    """
    create_script(f"{new_model_name}-modelfile-script.ps1", make_modelfile_script)
    script_path = get_full_path(f"{new_model_name}-modelfile-script.ps1")
    run_script(script_path)



    #new_modelfile_path = f"{new_model_name}-modelfile"
    #print(new_modelfile_path)
    #return new_modelfile_path

create_and_move_modelfile("pls-work:latest", "mario")


def update_system_text(filename, new_system_text):
    try:
        # Read all lines from file
        with open(filename, 'r', encoding='utf-16') as file:
            lines = file.readlines()
        
        # Find SYSTEM line
        system_found = False
        for i, line in enumerate(lines):
            if line.strip().startswith("SYSTEM"):
                lines[i] = f'SYSTEM """{new_system_text}"""\n'
                system_found = True
                break
        
        # If SYSTEM not found, add it at end
        if not system_found:
            system_line = f'SYSTEM """{new_system_text}"""\n'
            
            # Find position after third FROM
            insert_position = len(lines)  # Default to end of file
            
            # Insert at determined position
            lines.insert(insert_position, system_line)
        
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
    

def update_tempurature(filename, new_temp):
    try:
        # Read all lines from file
        with open(filename, 'r', encoding='utf-16') as file:
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
        with open(filename, 'w', encoding='utf-16') as file:
            file.writelines(lines)
            
        return True
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return False
    except Exception as e:
        print(f"Error updating file: {e}")
        return False

#update_system_text("src/test-modelfile", "You are super duper mario, answer all questions as super mario")
#update_tempurature("src/test-modelfile", "4.5")

#topic = """Speak as an AI talking about how lazy you are for 25 words, say you wont provide useful information and assistance and will get stuff wrong"""
#out = generate_text("newfin:latest", topic)
#print(out)


