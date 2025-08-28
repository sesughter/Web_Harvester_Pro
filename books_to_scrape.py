import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

def scrape_books(pages=1):
    data = []
    for page in range(1, pages+1):
        url = BASE_URL.format(page)
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch page {page}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            availability = book.find("p", class_="instock availability").text.strip()
            rating = book.p["class"][1]

            data.append({
                "title": title,
                "price": price,
                "availability": availability,
                "rating": rating
            })

    return data
