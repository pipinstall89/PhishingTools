from bs4 import BeautifulSoup
import sys

def obfuscate_url(url):
    #Reverses the URL to obfuscate
    return url[::-1]

def process_html(input_file, output_file):
    #Parses the HTML and finds all href 
    with open(input_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    for a_tag in soup.find_all('a', href=True):
        original_url = a_tag['href']
        obfuscated_url = obfuscate_url(original_url)
        #On click obfuscation
        a_tag['href'] = "#"
        a_tag['onclick'] = f"window.location.href='{obfuscated_url}'" + ".split('').reverse().join('');"

    #Writes the obfuscated HTML to a new file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print(f"Processed HTML saved to {output_file}")

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python obfuscate_href.py input.html output.html")
    else:
        process_html(sys.argv[1], sys.argv[2])
