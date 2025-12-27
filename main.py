from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://books.toscrape.com/').text
soup = BeautifulSoup(html_text, 'lxml')

books = soup.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

print(f"Total Books Found: {len(books)}\n")
print("=" * 70)

book_categories = soup.find('div', class_ = 'side_categories')
categories = book_categories.find('ul').find_all('a')
for index, category in enumerate(categories, 1):
    category_name = category.text.strip()
    print(f"{index}. {category_name}")

print("\n")

for index, book in enumerate(books, 1):
    
    book_title = book.find('h3').a['title']

    
    price = book.find('p', class_='price_color').text
    
    
    rating = book.find('p', class_='star-rating')['class'][1]
    
    
    print(f"{index}. Title: {book_title}")
    print(f"   Price: {price}")
    print(f"   Rating: {rating} stars")
    print("-" * 100)

