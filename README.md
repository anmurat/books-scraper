# Books Scraper & Analysis

A Python web scraper that collects book data from [books.toscrape.com](https://books.toscrape.com) and generates visual analysis.

## What It Does

- Scrapes book titles, prices, ratings, and availability across multiple pages
- Saves data to CSV
- Generates 3 charts with Matplotlib:
  - Books per rating
  - Price distribution histogram
  - Average price per rating

## Tech Stack

- `requests` — HTTP requests
- `BeautifulSoup4` — HTML parsing
- `pandas` — data processing
- `matplotlib` — data visualization

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Step 1: scrape the data
python scraper.py

# Step 2: analyze and visualize
python analyze.py
```

You can change `max_pages` in `scraper.py` to scrape more data (50 pages total available).

## Project Structure

```
books-scraper/
├── scraper.py        # scraping logic
├── analyze.py        # analysis & charts
├── requirements.txt  # dependencies
├── .gitignore
└── README.md
```

## Sample Output

```
=== SUMMARY ===
Total books: 100
Average price: £35.42
Cheapest: £10.03 — A Light in the Attic
Most expensive: £54.89 — Tipping the Velvet
```

## Output
