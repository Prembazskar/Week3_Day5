
import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"

headers = {"User-Agent": "Mozilla/5.0"}

try:
    page = requests.get(URL, headers=headers, timeout=10)
    page.raise_for_status()

    soup = BeautifulSoup(page.text, "html.parser")

    # BBC headline selector (verify using Chrome Inspect)
    items = soup.find_all("h2", attrs={"data-testid": "card-headline"})

    headlines = []
    seen = set()

    for item in items:
        headline = item.get_text(" ", strip=True)

        if headline and headline not in seen:
            headlines.append(headline)
            seen.add(headline)

        if len(headlines) == 5:
            break

    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline}")

    if len(headlines) < 5:
        print(f"Only {len(headlines)} headlines found.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching news: {e}")
