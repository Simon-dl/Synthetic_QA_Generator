from get_custom_model import get_custom_model
from request_handler import generate_text
import random

while True:
        model_input = input(" \n \nEnter the name of the model you want to use to answer questions or type 'setup' to set up a custom model and use that: ").strip()
        if model_input == 'setup':  # Check if topic is not empty
            custom_model = get_custom_model()
            break
        elif model_input:
            custom_model = model_input
            break
        
pair_amount = 2
while True:
        pair_input = input("""\nHow many pairs of questions and answers would you like to generate?
Please enter a number (default is 2): """).strip()

        if not pair_input : # If empty, use default
            break
        try:
            # Convert input to int
            new_pair_amount = int(pair_input)
            if new_pair_amount < 1:
                print("Please enter a number greater than 0")
            else:
                pair_amount = new_pair_amount
                break  
        except ValueError:
            break
#custom_model = get_custom_model()
#custom_model = 'lazy-llama:latest'


topic_list = ["food", "cars", "computers", "books", "movies", "music", "art", "science", "history", "geography", "math", "physics", "chemistry", "biology", "philosophy", "psychology", "sociology", "economics", "politics", "law", "sports", "entertainment", "travel", "fashion", "beauty", "health", "fitness", "technology", "science fiction", "fantasy", "horror", "mystery", "thriller", "romance", "comedy", "animation", "video games", "board games", "card games", "sports", "hobbies", "gardening", "cooking", "baking", "diy", "crafts", "artisanal", "handmade", "vintage", "antiques", "collectibles", "vintage"]
random_topic = random.choice(topic_list)

print(f'Generating {pair_amount} pairs of questions and answers')
print(random_topic)
prompt_text = generate_text('phi3:mini', f'ask a question about {random_topic} in 20 words or less')
print(prompt_text)
response_text = generate_text(custom_model, prompt_text)
print(response_text)


#TODO: Add a loop to generate the number of pairs of questions and answers specified by the user
#TODO: add a request_handler function to make sure user input is valid
#TODO: add a model to format the questions and answers as json
#TODO: add a function to save the questions and answers json to a file
#TODO: add a function to upload the file to huggingface?
#TODO: create a better custom dolphin model to generate system prompts, push to ollama for downloading
#TODO: add setup file to set up custom models 
#TODO: add setup instructions to README.md
#TODO: clean up code, add comments, and make it more readable, then publish to github
#TODO: create a .bat file to run the program?
