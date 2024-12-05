import csv
import os
#from datasets import load_dataset

fake_data = {'conversations' : [[{'question': "burh", 'answer': "whydoe"}]]}

fake_pairs = [{'question': "burh", 'answer': "whydoe"}]

path = "utils/csv_files/qa_dataset.csv"

def pairs_to_csv(pairs, filename='dataset'):
    """
    takes the pairs and writes them to a csv file
    """
    file_path = f'utils/csv_files/{filename}.csv'
    data_dict = {'conversations': [pairs]}
    print(file_path, data_dict)
    write_to_csv(data_dict, file_path)

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
pairs_to_csv(fake_pairs, 'test')
