import os
from bs4 import BeautifulSoup

# Specify the directory containing your HTML files
directory = '.'
# Specify the output file name
output_file = './combined_content.html'

# Create or overwrite the output file
with open(output_file, 'w', encoding='utf-8') as outfile:
    # Write the opening HTML tags
    outfile.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Combined Content</title>\n</head>\n<body>\n')

    # Loop through all HTML files in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as infile:
                # Parse the HTML content
                soup = BeautifulSoup(infile, 'html.parser')
                # Find the specific div
                div_content = soup.find('div', class_='markdown-preview-sizer markdown-preview-section')
                if div_content:
                    # Write the content of the div to the output file
                    outfile.write(str(div_content))
                    outfile.write('\n')  # Add a newline for better readability

    # Write the closing HTML tags
    outfile.write('</body>\n</html>')

print(f'Content from specified divs has been combined into {output_file}')
