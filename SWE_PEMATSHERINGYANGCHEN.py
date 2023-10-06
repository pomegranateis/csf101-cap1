import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com'

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')

    if quotes and authors:
        for quote, author in zip(quotes, authors):
            quote_text = quote.text.strip()
            author_name = author.text.strip()
            print(f"Quote: {quote_text}")
            print(f"Author: {author_name}")
            print("-------------------")

    else:
        print("No quotes found on the page.")

except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")


