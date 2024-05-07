import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from collections import deque

visited = set()

def extract_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        links = [a.get('href') for a in soup.find_all('a', href=True)]
        return links
    except Exception as e:
        print(f"Error extracting links from {url}: {e}")
        return []

def bfs_crawl(start_url, depth_limit):
    queue = deque([(start_url, 0)])

    while queue:
        url, depth = queue.popleft()

        if url in visited or depth > depth_limit:
            continue

        visited.add(url)
        print(f"Crawling: {url}")

        # Send HTTP request, parse HTML, and extract links
        links = extract_links(url)

        for link in links:
            # Construct absolute URL
            absolute_url = urljoin(url, link)
            queue.append((absolute_url, depth + 1))

# Start crawling from the main domain
bfs_crawl("https://nestnepal.com/", depth_limit=1)
