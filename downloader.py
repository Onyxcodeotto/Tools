import os
import requests

# File containing the links
input_file = "extracted_links.txt"

# Output folder to save files
output_folder = "downloaded_files"
os.makedirs(output_folder, exist_ok=True)

# Read all links from the file
with open(input_file, "r", encoding="utf-8") as file:
    links = file.readlines()

# Download each file
for link in links:
    link = link.strip()  # Remove any extra spaces or newlines
    if not link:
        continue

    try:
        response = requests.get(link)
        response.raise_for_status()  # Raise an error for bad status codes

        # Extract the file name from the link
        file_name = link.split("/")[-1]

        # Save the file to the output folder
        file_path = os.path.join(output_folder, file_name)
        with open(file_path, "wb") as file:
            file.write(response.content)

        print(f"Downloaded: {file_name}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {link}: {e}")

print(f"All files have been downloaded to {output_folder}")