import os
import json

def process_text_files(folder_path):
    # Ensure the output directory exists
    output_dir = os.path.join(folder_path, 'output')
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over each text file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                words = text.split()
                
                # Split text into 300-word chunks
                chunks = [words[i:i + 300] for i in range(0, len(words), 300)]
                
                # Create a dictionary to store the chunks
                chunks_dict = {str(i + 1): ' '.join(chunk) for i, chunk in enumerate(chunks)}
                
                # Save the chunks to a JSON file
                json_filename = f"{os.path.splitext(filename)[0]}.json"
                json_path = os.path.join(output_dir, json_filename)
                with open(json_path, 'w', encoding='utf-8') as json_file:
                    json.dump(chunks_dict, json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    folder_path = 'texts'  # Change this to your folder path if different
    process_text_files(folder_path)