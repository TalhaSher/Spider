import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import time
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

visited_links = set()
to_be_crawled = []
crawled_urls = set()  # To store crawled URLs


MAX_DEPTH = 3
REQUEST_DELAY = 1


def crawler(starting_url, depth=0):
    if depth > MAX_DEPTH:
        return

    time.sleep(REQUEST_DELAY)
    find_all_links(starting_url)

    for url in to_be_crawled:
        if url not in visited_links:
            logger.info(f"Crawling {url}")
            crawled_urls.add(url)  # Add crawled URL to set
            crawler(url, depth + 1)


def find_all_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
        soup = bs(html_content, 'html.parser')

        for a in soup.find_all('a', href=True):
            link = urljoin(url, a['href'])
            if link.startswith('http') and link not in to_be_crawled:
                to_be_crawled.append(link)
            elif not link.startswith(('http', 'https')):
                logger.warning(f"Relative URL found: {link}")

    except requests.RequestException as e:
        logger.error(f"Error accessing {url}: {e}")


def save_to_file(file_path, urls):
    with open(file_path, 'w') as file:
        for url in urls:
            file.write(url + '\n')


if __name__ == "__main__":
    starting_url = "https://youtube.com"
    crawler(starting_url)

    output_file = "crawled_urls.txt"
    save_to_file(output_file, crawled_urls)
    logger.info(f"Results saved to {output_file}")