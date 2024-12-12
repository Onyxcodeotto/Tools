from bs4 import BeautifulSoup

# Read the HTML content from a text file
input_file = "links.txt"  # Replace with your file name
with open(input_file, "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract all links
links = [a['href'] for a in soup.find_all('a', href=True)]

# Write the extracted links to a new text file
output_file = "extracted_links.txt"
with open(output_file, "w", encoding="utf-8") as file:
    for link in links:
        file.write(link + "\n")

print(f"Links have been extracted and saved to {output_file}")