# 📚 Books Scraper

A Python web scraper that extracts book information from [books.toscrape.com](https://books.toscrape.com/) including titles, prices, star ratings and book categories.

## Features

- Extracts book titles from the website.
- Retrieves pricing information for each book.
- Collects star ratings (One to Five stars).
- Displays total count of books found.
- Lists all types of category for books.
- Clean formatted output with f-strings.

## Technologies Used

- **Python 3.14**
- **BeautifulSoup4** - HTML parsing and web scraping.
- **Requests** - HTTP library for making web requests.
- **lxml** - XML and HTML parser.

## Prerequisites

Make sure you have Python installed on your system. You can check by running:
```bash
python --version
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/ScrapeLab.git
cd ScrapeLab
```

2. Install required dependencies:
```bash
pip install beautifulsoup4
pip install lxml
pip install requests
```

Or install from requirements.txt:
```bash
pip install -r requirements.txt
```

##  Use 

Run the scraper:
```bash
python books_scraper.py
```

## Requirements

Create a `requirements.txt` file with:
```
beautifulsoup4==4.12.2
lxml==4.9.3
requests==2.31.0
```
