from request_handler import show_model, pull_model

system_model_name = "Director-fin"
prompt_model_name = "phi3:mini"

response = show_model(system_model_name)
if not response:
    print(f"Model {system_model_name} not found, pulling model...")
    #pull_model(system_model_name)
    #print(f"Model {system_model_name} pulled successfully")
else:
    print(f"Model {system_model_name} found")
