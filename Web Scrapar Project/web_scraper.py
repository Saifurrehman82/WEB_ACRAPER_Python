import requests
from bs4 import BeautifulSoup
import csv

# URL of the website to scrape
url = 'http://books.toscrape.com/'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all book containers on the page
books = soup.find_all('article', class_='product_pod')

# Open a CSV file to write the extracted data
with open('books.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price', 'Availability'])

    # Loop through each book container and extract data
    for book in books:
        # Extract the book title
        title = book.h3.a['title']
        
        # Extract the book price
        price = book.find('p', class_='price_color').text
        
        # Extract the availability status
        availability = book.find('p', class_='instock availability').text.strip()
        
        # Write the data to the CSV file
        writer.writerow([title, price, availability])

print("Data has been written to books.csv")
