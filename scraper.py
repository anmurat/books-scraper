import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://books.toscrape.com/catalogue/"

RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

def get_books_from_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    for article in soup.select("article.product_pod"):
        title = article.h3.a["title"]
        price = float(article.select_one(".price_color").text.strip("£Â"))
        rating_word = article.p["class"][1]
        rating = RATING_MAP.get(rating_word, 0)
        availability = article.select_one(".availability").text.strip()

        books.append({
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability
        })

    return books, soup

def get_next_page(soup, current_url):
    next_btn = soup.select_one("li.next a")
    if not next_btn:
        return None
    next_href = next_btn["href"]
    if "catalogue/" not in current_url:
        return BASE_URL + next_href
    base = current_url.rsplit("/", 1)[0]
    return base + "/" + next_href

def scrape_all(max_pages=5):
    all_books = []
    url = "https://books.toscrape.com/catalogue/page-1.html"

    for page_num in range(1, max_pages + 1):
        print(f"Scraping page {page_num}: {url}")
        books, soup = get_books_from_page(url)
        all_books.extend(books)

        next_url = get_next_page(soup, url)
        if not next_url:
            break
        url = next_url
        time.sleep(0.5)

    df = pd.DataFrame(all_books)
    df.to_csv("books.csv", index=False)
    print(f"\nDone! {len(df)} books saved to books.csv")
    return df

if __name__ == "__main__":
    df = scrape_all(max_pages=5)
    print(df.head())
