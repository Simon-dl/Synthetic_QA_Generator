import os

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