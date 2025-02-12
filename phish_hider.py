from bs4 import BeautifulSoup
import sys

def obfuscate_url(url):
    """Reverse the URL string to obfuscate it."""
    return url[::-1]

def process_html(input_file, output_file):
    """Find all hrefs in an HTML file and obfuscate them using JavaScript."""
    with open(input_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    for a_tag in soup.find_all('a', href=True):
        original_url = a_tag['href']
        obfuscated_url = obfuscate_url(original_url)
        
        # Replace href with JavaScript-based onclick obfuscation
        a_tag['href'] = "#"
        a_tag['onclick'] = f"window.location.href='{obfuscated_url}'" + ".split('').reverse().join('');"

    # Write the modified HTML to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print(f"Processed HTML saved to {output_file}")

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python obfuscate_href.py input.html output.html")
    else:
        process_html(sys.argv[1], sys.argv[2])
