import os
import fitz  # PyMuPDF
from docx import Document

def process_pdf_files(folder_path, output_folder):
    print(f"Processing PDF files in {folder_path}...")
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each PDF file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            base_name = os.path.splitext(filename)[0]
            txt_filename = f"{base_name}.txt"
            txt_path = os.path.join(output_folder, txt_filename)

            print(f"Checking if text file {txt_path} already exists...")
            # Skip if the .txt file already exists
            if os.path.exists(txt_path):
                print(f"Text file {txt_path} already exists. Skipping...")
                continue

            file_path = os.path.join(folder_path, filename)
            print(f"Extracting text from {file_path}...")
            text = extract_text_from_pdf(file_path)
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(text)
            print(f"Text extracted and saved to {txt_path}")

def process_docx_files(folder_path, output_folder):
    print(f"Processing DOCX files in {folder_path}...")
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each DOCX file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.docx'):
            base_name = os.path.splitext(filename)[0]
            txt_filename = f"{base_name}.txt"
            txt_path = os.path.join(output_folder, txt_filename)

            print(f"Checking if text file {txt_path} already exists...")
            # Skip if the .txt file already exists
            if os.path.exists(txt_path):
                print(f"Text file {txt_path} already exists. Skipping...")
                continue

            file_path = os.path.join(folder_path, filename)
            print(f"Extracting text from {file_path}...")
            text = extract_text_from_docx(file_path)
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(text)
            print(f"Text extracted and saved to {txt_path}")

def copy_txt_files(folder_path, output_folder):
    print(f"Copying TXT files from {folder_path} to {output_folder}...")
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)

    # Copy each TXT file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            base_name = os.path.splitext(filename)[0]
            txt_filename = f"{base_name}.txt"
            txt_path = os.path.join(output_folder, txt_filename)

            print(f"Checking if text file {txt_path} already exists...")
            # Skip if the .txt file already exists
            if os.path.exists(txt_path):
                print(f"Text file {txt_path} already exists. Skipping...")
                continue

            file_path = os.path.join(folder_path, filename)
            print(f"Copying text file from {file_path} to {txt_path}...")
            with open(file_path, 'r', encoding='utf-8') as file, \
                 open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(file.read())
            print(f"File copied to {txt_path}")

def extract_text_from_pdf(pdf_path):
    print(f"Opening PDF file {pdf_path}...")
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    print(f"Text extraction complete for {pdf_path}")
    return text

def extract_text_from_docx(docx_path):
    print(f"Opening DOCX file {docx_path}...")
    doc = Document(docx_path)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    print(f"Text extraction complete for {docx_path}")
    return '\n'.join(text)

if __name__ == "__main__":
    input_folder = "/Users/ataonat/Desktop/Codes/bitchai_testing/pdfs"  # Replace with the path to your input folder
    output_folder = "texts"  # Output folder for the text files

    print("Starting processing of files...")
    # Process PDF files
    process_pdf_files(input_folder, output_folder)

    # Process DOCX files
    process_docx_files(input_folder, output_folder)

    # Copy TXT files
    copy_txt_files(input_folder, output_folder)
    print("All files processed.")