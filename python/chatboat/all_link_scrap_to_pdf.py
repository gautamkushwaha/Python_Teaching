import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, start_url, output_file='output.txt', max_depth=2):
        self.start_url = start_url
        self.output_file = output_file
        self.max_depth = max_depth
        self.visited_urls = set()

    def is_internal_link(self, url, base_url):
        parsed_url = urlparse(url)
        base_domain = urlparse(base_url).netloc
        return parsed_url.netloc == base_domain

    def scrape_and_save_text(self, url, depth=1):
        if depth > self.max_depth or url in self.visited_urls:
            return

        # Make a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract and format text content
            content = ''
            for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'ul', 'ol']):
                if tag.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    content += f'\n\n{tag.text.strip()}\n'
                else:
                    content += tag.text.strip() + '\n'

            # Save content to a text file
            with open(self.output_file, 'a', encoding='utf-8') as file:
                file.write(content)

            # Mark the current URL as visited
            self.visited_urls.add(url)

            # Find and follow internal links on the page
            for link in soup.find_all('a', href=True):
                next_url = urljoin(url, link['href'])
                if self.is_internal_link(next_url, url):
                    self.scrape_and_save_text(next_url, depth=depth+1)

    def run(self):
        self.scrape_and_save_text(self.start_url)


# Replace 'your_url_here' with the actual URL you want to start from
start_url = 'https://nestnepal.com/'
output_file = 'output.txt'
max_depth = 2

scraper = Scraper(start_url, output_file, max_depth)
scraper.run()
