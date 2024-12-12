from request_handler import show_model, pull_model

def setup_models():
    models = ["phi3:mini","Simon-DL/Director-fin"]

    for model in models:

        response = show_model(model)
        if not response:
            print(f"Model {model} not found, pulling model...")
            pull_model(model)
        else:
            print(f"Model {model} found")
