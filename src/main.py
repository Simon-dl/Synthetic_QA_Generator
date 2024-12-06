from get_custom_model import get_custom_model
from request_handler import generate_text, show_model
from dataset_handler import pairs_to_csv
import random
import time

while True:
        model_input = input(" \n \nEnter the name of the model you want to use to answer questions or type 'setup' to set up a custom model and use that: ").strip()
        if model_input == 'setup':  # Check if topic is not empty
            custom_model = get_custom_model()
            break
        elif model_input:
            custom_model = model_input
            if show_model(custom_model):
                break
            else:
                print(f"Model {custom_model} not found, please try again")
        
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
times = []
pairs = []
for i in range(pair_amount):
    
    start = time.time()
    random_topic = random.choice(topic_list)
    print(f'Generating pair {i+1}, topic: {random_topic}')
    prompt_text = generate_text('phi3:mini', f'ask a question about {random_topic} in 20 words or less')
    response_text = generate_text(custom_model, prompt_text)
    pairs.append([{'question': prompt_text, 'answer': response_text}])
    end = time.time()
    pair_time = round(end - start, 2)
    times.append(pair_time)
    print(f'Pair {i+1} took {pair_time} seconds to generate')

model_name = custom_model.replace(':', '_')
pairs_to_csv(pairs, True, f'{model_name}_dataset')
total_time = sum(times)
min_time = min(times)
max_time = max(times)

print(f'\nTotal time to generate {pair_amount} pairs: {round(total_time, 2)} seconds')
print(f'Average time to generate each pair: {round(total_time / pair_amount, 2)} seconds')
print(f'Maximum time to generate a pair: {max_time} seconds')
print(f'Minimum time to generate a pair: {min_time} seconds')




#TODO: add a model to format the questions and answers as json
#TODO: add a function to save the questions and answers json to a file (done)
#TODO: add a function to upload the file to huggingface? https://huggingface.co/docs/datasets/en/upload_dataset
#TODO: create a better custom dolphin model to generate system prompts, push to ollama for downloading
#TODO: add setup file to set up custom models 
#TODO: add setup instructions to README.md
#TODO: clean up code, add comments, and make it more readable, then publish to github
#TODO: create a .bat file to run the program?
