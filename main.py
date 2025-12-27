from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://books.toscrape.com/').text
soup = BeautifulSoup(html_text, 'lxml')

books = soup.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

print(f"Total Books Found: {len(books)}\n")
print("=" * 70)

for index, book in enumerate(books, 1):
    
    book_title = book.find('h3').a['title']

    # Get price
    price = book.find('p', class_='price_color').text
    
    
    rating = book.find('p', class_='star-rating')['class'][1]
    
    # Print using f-string
    print(f"{index}. Title: {book_title}")
    print(f"   Price: {price}")
    print(f"   Rating: {rating} stars")
    print("-" * 100)

