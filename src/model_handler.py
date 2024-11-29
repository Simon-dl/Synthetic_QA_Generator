import ollama
import pathlib
import os
from request_handler import create_model, generate_text


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


topic = """Speak as an AI talking about how lazy you are for 25 words, say you wont provide useful information and assistance"""



out = generate_text("newfin:latest", topic)
print(out)


