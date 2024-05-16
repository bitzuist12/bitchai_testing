import os
import json

def combine_json_files(folder_path, output_file):
    combined_data = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                for number, text in data.items():
                    combined_data.append({
                        "file_name": filename,
                        "number": number,
                        "text": text
                    })
    
    with open(output_file, 'w') as output:
        json.dump(combined_data, output, indent=4)

if __name__ == "__main__":
    folder_path = '/Users/ataonat/Desktop/bitchai_testing/texts/output'
    output_file = 'combined.json'
    combine_json_files(folder_path, output_file)