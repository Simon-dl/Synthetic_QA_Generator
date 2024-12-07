import csv
import os
from datasets import load_dataset


def pairs_to_csv(pairs, format, filename='dataset'):
    """
    takes the pairs and writes them to a csv file
    format is a boolean that determines if the pairs should be formatted 
    """
    file_path = f'utils/csv_files/{filename}.csv'
    if format:
        pairs = format_pairs(pairs)
    data_dict = {'conversations': [pairs]}
    write_to_csv(data_dict, format, file_path)


def format_pairs(pairs):
    """
    formats the pairs to the tome dataset format 
    https://huggingface.co/datasets/mlabonne/FineTome-100k?row=79
    """
    formatted_pairs = []


    for i in range(len(pairs)):
        question = pairs[i][0]['question']
        answer = pairs[i][0]['answer']
        human = {"from": "bot1", "value": f"{question}" }
        bot = { "from": "bot2", "value": f"{answer}"}
        formatted_pairs.append([human, bot])
    return formatted_pairs


def write_to_csv(data_dict, formatted, filename='dataset.csv'):
    """
    Write dictionary data to a CSV file where each conversation pair is on its own line.
    
    Args:
        data_dict (dict): Dictionary with 'conversations' key containing list of pairs
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
        
        if formatted:
            for item in data_dict[field_name][0]:  # Note the [0] to access the inner list
                writer.writerow([item])
        else:
            # Write each conversation pair as a separate row
            for pair in data_dict[field_name][0]:  # Note: [0] because fake_data has nested list
                writer.writerow([pair])



            





