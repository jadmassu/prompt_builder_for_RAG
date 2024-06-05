from langchain_community.document_loaders import PyPDFLoader

import os

def load_pdf(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file does not exist.")

    # Check if the file is a PDF
    if not file_path.lower().endswith('.pdf'):
        raise ValueError("The file is not a PDF.")

    try:
        # Attempt to load the PDF
        path = PyPDFLoader(file_path)
        return path
    except Exception as e:
        raise RuntimeError(f"An error occurred while loading the PDF: {e}")

def split_pdf(loaded_pdf):
    try:
        # Attempt to split the loaded PDF
        pages = loaded_pdf.load_and_split()
        return pages
    except Exception as e:
        raise RuntimeError(f"An error occurred while splitting the PDF: {e}")

def extract_text_from_pages(pdf_reader):
    try:
        extracted_text = ""
        for i, page in enumerate(pdf_reader.pages):
            text = page.extract_text()
            if text:
                extracted_text += text
        return extracted_text
    except Exception as e:
        raise RuntimeError(f"An error occurred while extracting text from pages: {e}")


