# Web Scraping Example using BeautifulSoup
import requests
from bs4 import BeautifulSoup

# URL to scrape
print("Start from 'https' ")
url = input("Enter the full URL you want to scrape: ")


# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract and print the title of the page
    title = soup.title.string
    print(f'Title: {title}')

    # Extract and print all the links on the page
    links = soup.find_all('a')
    print('\nLinks:')
    for link in links:
        print(link.get('href'))

else:
    print(f'Error: Unable to fetch the page. Status code: {response.status_code}')
