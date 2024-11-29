from modelfile_handler import create_and_move_modelfile
from request_handler import generate_text

def get_custom_model(base_model_name = "dolphin-mistral"):
    """
    Gets a custom model based on a base model name and a topic from user input.
    
    Args:
        base_model_name (str): The base model to use
        
    Returns:
        tuple: (model_name, topic)
    """
    # Get topic from user
    while True:
        topic = input(" \n \nEnter a topic for your custom model (e.g., 'Mario', 'Shakespeare', etc.): ").strip()
        if topic:  # Check if topic is not empty
            break
        print("Topic cannot be empty. Please try again.")

    system_prompt = ""
    while True:
        text = prompt_model(base_model_name, topic)
        satis = input( "\n \n \nIs this satifactory as a system prompt? selecting no will reprompt the model. \ny for yes, n for no: " ).strip()
        if satis == 'y':  # Check if yes
            system_prompt = text
            break
            

    print(system_prompt)
    
    return topic


def prompt_model(base_model_name, topic):
    print(f" \ntopic: {topic} \n\nprompting model {base_model_name} with topic {topic} to generate a system prompt")

    text = generate_text(f"{base_model_name}", f"you are {topic}, talk like an assistant knowldgeable about {topic} in 20 words or less")

    print("\n model response: \n \n -------------------------------------------------------------------------- \n", text, "\n --------------------------------------------------------------------------")

    return text

get_custom_model()


