import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    """Fetches HTML content from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching HTML: {e}")
        return None

def scrape_website(url):
    """Scrapes a website for news headlines."""
    html = fetch_html(url)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        headlines = soup.find_all('h3', class_='gs-c-promo-heading__title')
        for headline in headlines:
            title = headline.text.strip()
            print(title)
    else:
        print("Failed to fetch HTML.")

if __name__ == "__main__":
    url = 'https://www.bbc.com/news'  # Replace with your desired website URL
    scrape_website(url)
