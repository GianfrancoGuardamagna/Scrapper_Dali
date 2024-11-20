"""
This script retrieves URLs from multiple sitemap XML files and writes them to a text file.
Modules:
    requests: To make HTTP requests to retrieve the sitemap XML files.
    bs4 (BeautifulSoup): To parse the XML content of the sitemap files.
    time: To add a delay between requests.
Variables:
    urls (list): A list of sitemap XML file URLs to be processed.
    links (list): A list to store the URLs extracted from the sitemap files.
Workflow:
    1. Iterate over each URL in the `urls` list.
    2. Make an HTTP GET request to retrieve the sitemap XML file.
    3. If the request is successful (status code 200):
        a. Parse the XML content using BeautifulSoup.
        b. Find all <loc> tags and extract their text content.
        c. Append the extracted URLs to the `links` list.
    4. If the request fails, print an error message with the URL.
    5. Write all extracted URLs to a file named 'links.txt', each URL on a new line.
Usage:
    Run the script to retrieve URLs from the specified sitemap XML files and save them to 'links.txt'.
"""

import requests
from bs4 import BeautifulSoup
import time

urls = [
    'https://recicladores.com.ar/post-sitemap1.xml',
    'https://recicladores.com.ar/post-sitemap2.xml',
    'https://recicladores.com.ar/post-sitemap3.xml',
    'https://recicladores.com.ar/post-sitemap4.xml',
    'https://recicladores.com.ar/post-sitemap5.xml',
    'https://recicladores.com.ar/post-sitemap6.xml',
    'https://recicladores.com.ar/post-sitemap7.xml',
    'https://recicladores.com.ar/post-sitemap8.xml',
    'https://recicladores.com.ar/post-sitemap9.xml',
    'https://recicladores.com.ar/post-sitemap10.xml'
]

links = []

for url in urls:
    time.sleep(1)  # Add a delay before retrying
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, features='xml')
        loc_tags = soup.find_all('loc')
        for loc in loc_tags:
            links.append(loc.get_text())
    else:
        print(f'Failed to retrieve {url}')

with open('links.txt', 'w') as file:
    for link in links:
        file.write(link + '\n')
