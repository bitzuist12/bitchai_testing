import os
import json

import os
import json

def create_json_from_txt(input_folder, json_output_folder):
    print("Starting to create JSON files from TXT files...")
    # Ensure the JSON output folder exists
    os.makedirs(json_output_folder, exist_ok=True)
    
    # Iterate over each .txt file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            file_path = os.path.join(input_folder, filename)
            json_filename = f"{os.path.splitext(filename)[0]}.json"
            json_path = os.path.join(json_output_folder, json_filename)
            print(f"Processing {filename}...")

            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                words = text.split()
                chunks = [words[i:i + 300] for i in range(0, len(words), 300)]
                chunks_dict = {str(i + 1): ' '.join(chunk) for i, chunk in enumerate(chunks)}

                with open(json_path, 'w', encoding='utf-8') as json_file:
                    json.dump(chunks_dict, json_file, ensure_ascii=False, indent=4)
                    print(f"Created {json_filename} with {len(chunks)} chunks.")

    
def combine_json_files(folder_path, output_file):
    print("Combining JSON files...")
    combined_data = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            print(f"Reading {filename}...")
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
        print(f"Combined data written to {output_file}.")

if __name__ == "__main__":
    # input_folder = '/Users/ataonat/Desktop/Codes/bitchai_testing/data/texts'
    json_output_folder = '/Users/ataonat/Desktop/Codes/bitchai_testing/data/jsons'
    output_file = 'data/combined.json'
    # create_json_from_txt(input_folder, json_output_folder)
    combine_json_files(json_output_folder, output_file)

