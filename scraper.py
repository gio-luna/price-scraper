from __future__ import annotations

from typing import Any

import requests
from bs4 import BeautifulSoup

DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


def fetch_page(url: str, user_agent: str | None = None, timeout: int = 10) -> requests.Response:
    """Fetch a web page and return the HTTP response."""
    headers = {"User-Agent": user_agent or DEFAULT_USER_AGENT}

    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response
    except requests.RequestException as exc:
        raise RuntimeError(f"Request failed for {url}: {exc}") from exc


def normalize_price(value: str | None) -> str:
    """Normalize scraped price strings and remove known encoding artifacts."""
    if value is None:
        return "Price not found"

    cleaned = (
        value.replace("Â", "")
        .replace("�", "")
        .replace("\xa0", " ")
        .strip()
    )
    return cleaned


def extract_books(url: str, limit: int = 5) -> list[dict[str, str]]:
    """Extract the first N books from a product listing page."""
    response = fetch_page(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select("article.product_pod")[:limit]

    extracted_books: list[dict[str, str]] = []

    for book in books:
        title_tag = book.find("h3")
        price_tag = book.find("p", class_="price_color")

        title = title_tag.a["title"] if title_tag and title_tag.a else "Title not found"
        price = normalize_price(price_tag.get_text(strip=True) if price_tag else None)

        extracted_books.append({"title": title, "price": price})

    return extracted_books


def main() -> None:
    target_url = "http://books.toscrape.com/"
    print(f"Starting scrape for: {target_url}\n")

    try:
        books = extract_books(target_url)
        print(f"Found {len(books)} books on the page.\n")

        for book in books:
            print(f"Title: {book['title']}")
            print(f"Price: {book['price']}")
            print("-" * 40)
    except RuntimeError as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()