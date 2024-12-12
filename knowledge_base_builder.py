import os 
import pandas as pd
from langchain.document_loaders import PyPDFLoader


DATASET_DIR = "./downloaded_files"


def extract_sds_information(path):
    try:
        loader = PyPDFLoader(path)
        pages = []
        for page in loader.load():
            pages.append(page.page_content)

        # Combine all pages into one text block
        full_text = "\n".join(pages)

        # Extract relevant sections (e.g., GHS Classification, CAS Numbers)
        # This is a simplified example; you can use regex or NLP for more advanced parsing
        identification = "Hydrogen Peroxide" if "Hydrogen Peroxide" in full_text else "Unknown"
        cas_number = "7722-84-1" if "7722-84-1" in full_text else "Unknown"
        hazards = "Oxidizing Liquid" if "Oxidizing Liquid" in full_text else "Unknown"

        # Return extracted information as a dictionary
        return {
            "File Name": os.path.basename(pdf_path),
            "Identification": identification,
            "CAS Number": cas_number,
            "Hazards": hazards,
        }
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        return None