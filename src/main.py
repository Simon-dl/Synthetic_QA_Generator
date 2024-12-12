from get_custom_model import get_custom_model
from request_handler import generate_text, show_model
from dataset_handler import pairs_to_csv
from setup import setup_models
import random
import time
import sys

setup_models()

question_model = 'phi3:mini'

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


topic_list = ["food", "cars", "computers", "books", "movies", "music", "art", "science", "history", "geography", "math", "physics", "chemistry", "biology", "philosophy", "psychology", "sociology", "economics", "politics", "law", "sports", "entertainment", "travel", "fashion", "beauty", "health", "fitness", "technology", "science fiction", "fantasy", "horror", "mystery", "thriller", "romance", "comedy", "animation", "video games", "board games", "card games", "sports", "hobbies", "gardening", "cooking", "baking", "diy", "crafts", "artisanal", "handmade", "vintage", "antiques", "collectibles", "vintage"]
random_topic = random.choice(topic_list)

print(f'Generating {pair_amount} pairs of questions and answers')
times = []
pairs = []
first_pair = True
for i in range(pair_amount):
    
    start = time.time()
    random_topic = random.choice(topic_list)
    print(f'Generating pair {i+1}, topic: {random_topic}')
    prompt_text = generate_text(f'{question_model}', f'ask a question about {random_topic} in 20 words or less')
    response_text = generate_text(custom_model, prompt_text)
    pairs.append([{'question': prompt_text, 'answer': response_text}])
    if first_pair:
        first_pair = False
        print(f'First pair: {pairs[0]}')
        while True:
            okay_pair = input("""\nDid this pair generally look okay to you? (y/n): if not, type 'n' and program will exit so you start again with everything fresh """).strip()
            if okay_pair == 'y':
                break
            elif okay_pair == 'n':
                sys.exit("\n\nExiting program")
            else:
                print("Please enter 'y' or 'n'")
    end = time.time()
    pair_time = round(end - start, 2)
    times.append(pair_time)
    print(f'Pair {i+1} took {pair_time} seconds to generate')

model_name = custom_model.replace(':', '_')
total_time = sum(times)
min_time = min(times)
max_time = max(times)

print(f'\nTotal time to generate {pair_amount} pairs: {round(total_time, 2)} seconds')
print(f'Average time to generate each pair: {round(total_time / pair_amount, 2)} seconds')
print(f'Maximum time to generate a pair: {max_time} seconds')
print(f'Minimum time to generate a pair: {min_time} seconds')


while True:
        format_input = input("""\nWould you like to format the questions and answers? see README.md for more info (y/n): """).strip()
        if format_input == 'y':
            pairs_to_csv(pairs, True, f'{model_name}_dataset')
            break
        elif format_input == 'n':
            pairs_to_csv(pairs, False, f'{model_name}_dataset')
            break
        else:
            print("Please enter 'y' or 'n'")

sys.exit("\n\nExiting program")

#TODO: add a model to format the questions and answers (done)
#TODO: add a function to save the questions and answers to a csv file, make sure it writes lines correctly (done)
#TODO: create a better custom dolphin model to generate system prompts (done),
#TODO: push model to ollama for downloading (12/9/2024) (done)
#TODO: add setup file to pull models from ollama when running the program, make sure to check if the model is already downloaded (done)
#TODO: add setup instructions to README.md (done)
#TODO: clean up code, add comments, and make it more readable, then publish to github

