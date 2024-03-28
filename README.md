# Python for Penetration Testing
## Description:
  This project is made to penetration testing in order to exeaming there test exploit with python code 
### Fuzzy.py Script Description:
**Info:**
This python script preform Fuzz after the "/" in target URL
1. Create your own word list in txt file 
2. Open a terminal and run the command:
`cat wordlist.txt | python3 fuzzy.py`
### Spider.py Script Description:
**Info:**
The spider script is a Python program designed to crawl web pages recursively starting from a given URL. It searches for URLs containing a specified keyword and prints them to the console. Additionally, it stores these URLs in a file named urls.txt. The spider script utilizes the requests library to make HTTP requests, BeautifulSoup for HTML parsing, and urljoin to resolve relative URLs. It maintains a set of visited URLs to avoid revisiting the same pages. The script is suitable for web scraping tasks where the goal is to extract URLs containing specific keywords.
**Spider Script Manual Guide:**
Ensure you have Python installed on your system. If not, download and install Python from the official website: [Python Downloads](https://www.python.org/downloads/).
Clone or download the spider script (spider.py) from this repository.
Open a terminal or command prompt.
Run the spider script by executing the following command:
`python spider.py`
Follow the prompts to input the URL you want to scrape and the keyword you want to search for.
The script will start crawling the provided URL, searching for the specified keyword, and print the URLs containing the keyword to the console. Additionally, it will save these URLs to a file named urls.txt.

### Prob Script Description:
**Info:**
The prob script is a Python program that filters URLs based on their response status codes. It reads a list of URLs from standard input, sends HEAD requests to each URL, and selects only those with a status code of 200 or 403. The script handles various error scenarios gracefully, such as URLs with missing schema or connection errors. It outputs the filtered URLs to a file named filtered_urls.txt. The prob script is useful for validating URLs and selecting only those that are accessible and responsive.
**Prob Script Manual Guide:**
Create a file named urls.txt containing the list of URLs you want to filter. Each URL should be on a separate line.
Open a terminal or command prompt.
Run the prob script by executing the following command:
`cat urls.txt | python prob.py`
This command pipes the contents of urls.txt to the prob script.
The script will filter the URLs based on their response status codes, selecting only those with a status code of 200 or 403. It will then save the filtered URLs to a file named filtered_urls.txt.
