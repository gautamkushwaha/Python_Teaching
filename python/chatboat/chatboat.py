import requests
from bs4 import BeautifulSoup
import pdfkit

def fetch_web_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to retrieve web page. HTTP Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error retrieving web page: {e}")
        return None

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract all text content without HTML tags
    text_content = soup.get_text(separator='\n', strip=True)

    return text_content

def save_to_text_file(text_content, file_name='output.txt'):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(text_content)

def save_to_pdf(text_content, pdf_file_name='output.pdf'):
    options = {
        'quiet': '',
        'encoding': 'UTF-8'
    }
    pdfkit.from_string(text_content, pdf_file_name, options=options)

def main(url):
    web_page_content = fetch_web_page(url)

    if web_page_content:
        text_content = parse_html(web_page_content)

        # Save to text file
        save_to_text_file(text_content)

        # Save to PDF file
        save_to_pdf(text_content)

        print(f"Text and PDF files saved successfully.")
    else:
        print("Failed to fetch web page content.")

if __name__ == "__main__":
    # Replace 'https://example.com' with the desired URL
    main('https://portfolio-iota-nine-60.vercel.app/')
