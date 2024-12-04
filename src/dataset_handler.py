import csv
import os

fake_data = {'conversations' : [{'question': "burh", 'answer': "whydoe"}]}

def write_to_csv(data, filename='dataset.csv'):
    """
    Write dictionary data to a CSV file.
    
    Args:
        data (list): List of dictionaries containing 'question' and 'answer' pairs
        filename (str): Name of the output CSV file
    """
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Write data to CSV
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['conversations']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header
        writer.writeheader()
        
        # Write data rows
        writer.writerows(data)

# Example usage
write_to_csv(fake_data, 'data/qa_dataset.csv')