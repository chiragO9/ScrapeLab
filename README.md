# 📚 Books Scraper

A Python web scraper that extracts book information from [books.toscrape.com](https://books.toscrape.com/) including titles, prices, and star ratings.

## 🎯 Features

- Extracts book titles from the website
- Retrieves pricing information for each book
- Collects star ratings (One to Five stars)
- Displays total count of books found
- Clean formatted output with f-strings

## 🛠️ Technologies Used

- **Python 3.x**
- **BeautifulSoup4** - HTML parsing and web scraping
- **Requests** - HTTP library for making web requests
- **lxml** - XML and HTML parser

## 📋 Prerequisites

Make sure you have Python installed on your system. You can check by running:
```bash
python --version
```

## 🚀 Installation

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

## 💻 Usage

Run the scraper:
```bash
python books_scraper.py
```

## 📊 Sample Output
```
Total Books Found: 20

======================================================================
1. Title: A Light in the Attic
   Price: £51.77
   Rating: Three stars
----------------------------------------------------------------------
2. Title: Tipping the Velvet
   Price: £53.74
   Rating: One stars
----------------------------------------------------------------------
3. Title: Soumission
   Price: £50.10
   Rating: One stars
----------------------------------------------------------------------
...
```

## 📁 Project Structure
```
ScrapeLab/
│
├── books_scraper.py      # Main scraper script
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
└── .gitignore           # Git ignore file
```

## 🔍 Code Explanation

### Main Components:

**1. Fetching the webpage:**
```python
html_text = requests.get('https://books.toscrape.com/').text
soup = BeautifulSoup(html_text, 'lxml')
```

**2. Finding all books:**
```python
books = soup.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
```

**3. Extracting information:**
```python
book_title = book.find('h3').a['title']
price = book.find('p', class_='price_color').text
rating = book.find('p', class_='star-rating')['class'][1]
```

## 🧠 What I Learned

- How to make HTTP requests using the Requests library
- Parsing HTML content with BeautifulSoup
- Navigating the DOM to locate specific elements
- Extracting text content vs HTML attributes
- Understanding CSS class selectors
- Using f-strings for formatted output
- Working with lists and loops in Python

## 🔧 Key Concepts

### HTML Attribute Access
```python
# Accessing attributes using bracket notation
element['title']    # Gets the title attribute
element['class']    # Gets class as a list
element['href']     # Gets the href attribute
```

### Star Rating Extraction
```python
# The class attribute returns a list: ['star-rating', 'Three']
rating = book.find('p', class_='star-rating')['class'][1]
# [0] = 'star-rating' (not useful)
# [1] = 'Three' (the actual rating)
```

## 📝 Requirements

Create a `requirements.txt` file with:
```
beautifulsoup4==4.12.2
lxml==4.9.3
requests==2.31.0
```

## ⚠️ Important Notes

- This project is for **educational purposes only**
- Always respect the website's `robots.txt` and terms of service
- The website [books.toscrape.com](https://books.toscrape.com/) is specifically designed for web scraping practice
- Be mindful of request frequency to avoid overloading servers

## 🚧 Future Enhancements

- [ ] Add data export to CSV format
- [ ] Implement multi-page scraping (pagination)
- [ ] Add error handling for network issues
- [ ] Filter books by price range
- [ ] Sort books by rating
- [ ] Create data visualizations

## 🤝 Contributing

This is a personal learning project, but suggestions and feedback are welcome!

## 📄 License

This project is open source and available for educational purposes.

## 📧 Contact

Feel free to reach out if you have questions or suggestions!

---

⭐ If you found this helpful, please give it a star!

**Happy Scraping!** 🚀
```

---

## Also Create These Files:

### **requirements.txt:**
```
beautifulsoup4==4.12.2
lxml==4.9.3
requests==2.31.0
```

### **.gitignore:**
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Project specific
*.csv
*.json
output/
