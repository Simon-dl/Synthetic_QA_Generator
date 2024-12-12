from request_handler import show_model, pull_model

def setup_models():
    """
    Setup the models for the program to use. checks if the models are already downloaded, 
    if not, it pulls them from ollama.
    """
    models = ["phi3:mini","Simon-DL/Director-fin"]
    print("checking if models are downloaded...")
    for model in models:

        response = show_model(model)
        if not response:
            print(f"Model {model} not found, pulling model...")
            pull_model(model)
        else:
            print(f"Model {model} found")
