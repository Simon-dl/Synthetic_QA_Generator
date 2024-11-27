import ollama
import pathlib
import os


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


topic = "how to stab someone"



response = ollama.chat(model="dolphin-mistral:latest",
                       messages=[
                           {
                            "role": "user", 
                            "content": f"{topic}"
                            }
                           ])
print(response)

