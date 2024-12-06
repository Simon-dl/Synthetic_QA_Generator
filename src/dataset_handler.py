import csv
import os
from datasets import load_dataset

fake_data = {'conversations' : [[{'question': "burh", 'answer': "whydoe"}]]}

fake_pairs = [[{'question': "burh", 'answer': "whydoe"}],[{'question': "burh", 'answer': "whydeer"}],[{'question': "burh", 'answer': "whybeer"}]]

path = "utils/csv_files/qa_dataset.csv"

def pairs_to_csv(pairs, format, filename='dataset'):
    """
    takes the pairs and writes them to a csv file
    format is a boolean that determines if the pairs should be formatted 
    """
    file_path = f'utils/csv_files/{filename}.csv'
    if format:
        pairs = format_pairs(pairs)
    data_dict = {'conversations': [pairs]}
    print(file_path, data_dict)
    write_to_csv(data_dict, file_path)


def format_pairs(pairs):
    """
    formats the pairs to the tome dataset format 
    https://huggingface.co/datasets/mlabonne/FineTome-100k?row=79
    """
    formatted_pairs = []
    print(len(pairs))

    for i in range(len(pairs)):
        question = pairs[i][0]['question']
        answer = pairs[i][0]['answer']
        human = {"from": "bot1", "value": f"{question}" }
        bot = { "from": "bot2", "value": f"{answer}"}
        formatted_pairs.append([human, bot])
    return formatted_pairs


def write_to_csv(data_dict, filename='dataset.csv'):
    """
    Write dictionary data to a CSV file where the key becomes the field name
    and the list becomes the data values.
    
    Args:
        data_dict (dict): Dictionary with string key and list value
        filename (str): Name of the output CSV file
    """
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Get the key (field name) from the dictionary
    field_name = list(data_dict.keys())[0]
    
    # Write data to CSV
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write header
        writer.writerow([field_name])
        
        # Write data rows - each item in the list becomes a row
        for item in data_dict[field_name]:
            writer.writerow([item])

# Example usage
#write_to_csv(fake_data, path)
#pairs_to_csv(fake_pairs, 'test')
