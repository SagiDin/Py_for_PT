import sys
import requests

"""The Python code will get a urls.txt in order to create a valid URLs list that have a 200 response status code"""
"""Run the following command from your terminal: cat urls.txt | python3 Prob.py 
and you will get a filtered_urls.txt file"""


def urls(out_file):
    # Read URLs from standard input
    url2 = sys.stdin.read().splitlines()

    # Lists to store good URLs (status code 200) and bad URLs
    good_urls = []
    bad_urls = []

    # Iterate through each URL
    for url in url2:
        try:
            # Send a HEAD request to check the status code
            response = requests.head(url)

            # If the response status code is 200 or 403, add the URL to the good_urls list
            if response.status_code == 200 or response.status_code == 403:
                good_urls.append(url)
        except requests.exceptions.MissingSchema:
            # Handle URLs with missing schema (e.g., "http://" or "https://")
            bad_urls.append(url)
            continue
        except requests.exceptions.ConnectionError:
            # Handle connection errors (e.g., DNS resolution failure, connection timeout)
            bad_urls.append(url)
            continue

    # Write good URLs to the output file
    with open(out_file, 'w') as file:
        file.write('\n'.join(good_urls))

    # Print a message indicating successful saving of URLs to the output file
    print(f"Saved URLs {out_file}")


# Define the output file name
out_file = 'filtered_urls.txt'
# Call the urls function with the output file name
urls(out_file)
