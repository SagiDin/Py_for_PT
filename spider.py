from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

# Set to store visited URLs to avoid revisiting
visited_urls = set()


# Function to crawl URLs recursively and search for a keyword
def spider_urls(url, keyword):
    try:
        # Send HTTP GET request to the URL
        response = requests.get(url)
    except:
        # Handle request failure
        print(f"Request failed {url}")
        return

    # Check if the request was successful or forbidden
    if response.status_code == 200 or response.status_code == 403:
        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        # Find all anchor tags in the HTML
        a_tag = soup.find_all('a')
        # List to store extracted URLs
        urls = []
        # Extract href attribute from anchor tags
        for tag in a_tag:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)

        # Open file to store URLs containing the keyword
        with open("urls.txt", "a") as file:
            # Iterate through extracted URLs
            for u in urls:
                if u not in visited_urls:
                    # Add URL to visited set to avoid revisiting
                    visited_urls.add(u)
                    # Join base URL with extracted URL
                    url_join = urljoin(url, u)
                    # Check if keyword is present in the URL
                    if keyword in url_join:
                        # Write URL to file
                        file.write(url_join + "\n")
                        # Print URL containing the keyword
                        print(url_join)
                        # Recursive call to crawl further
                        spider_urls(url_join, keyword)
                else:
                    # If URL is already visited, skip it
                    pass


# Get URL and keyword input from user
url = input("Enter the URL that you want to scrape: ")
keyword = input("Enter the keyword to search for in the URL provided: ")
# Call the spider_urls function to start crawling
spider_urls(url, keyword)
