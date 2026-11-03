# Python Web Scraper for Product Listings

This project is a lightweight Python scraper for extracting product information, titles, and prices from e-commerce catalog pages using `requests` and `BeautifulSoup`.

## Features
- HTML parsing through targeted selectors and page structure analysis.
- Browser-like request headers to reduce the risk of being blocked.
- Clear handling of network errors and HTTP response failures.
- Simple, readable code designed for learning and extension.

## Requirements

### Arch Linux
```bash
sudo pacman -S python-requests python-beautifulsoup4
```

### Other systems
```bash
pip install requests beautifulsoup4
```

## Usage

Run the script from the project directory:

```bash
python scraper.py
```

The current implementation fetches the sample catalog page at `http://books.toscrape.com/` and prints the first five books along with their prices.

## Notes

This project is intended for educational and testing purposes. Please review the target website's terms of service and robots policy before scraping in production or at scale.