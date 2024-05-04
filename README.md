# Web Crawler

This is a simple web crawler implemented in Python using the `requests` library for making HTTP requests and `BeautifulSoup` for parsing HTML content.

## Features

- Crawls web pages starting from a given URL up to a certain depth.
- Logs information about crawling process using Python's `logging` module.
- Saves the crawled URLs to a text file.

## Requirements

- Python 3.x
- `requests` library
- `BeautifulSoup` library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/web-crawler.git
```

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```


## Usage

1. Modify the `starting_url` variable in `crawler.py` to specify the URL from which crawling should begin.
2. Optionally, adjust the `MAX_DEPTH` and `REQUEST_DELAY` variables in `crawler.py` to control the depth of crawling and the delay between requests.
3. Run the crawler:

```bash
python crawler.py
```
The crawler will start from the specified URL and crawl the web pages up to the specified depth, logging information about the process. After crawling, it will save the crawled URLs to a text file named `crawled_urls.txt`.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or create a pull request.
