"""
This script reads a list of URLs from 'links.txt', fetches the HTML content of each URL, 
parses specific information using BeautifulSoup, and stores the extracted data in a JSON file 'data_book.json'.

Modules:
    requests: To handle HTTP requests.
    json: To handle JSON data.
    bs4 (BeautifulSoup): To parse HTML content.

Functions:
    None

Variables:
    session (requests.Session): A session object to handle HTTP requests with retry logic.
    retries (Retry): A Retry object to define retry logic for HTTP requests.
    html_book (list): A list to store dictionaries of extracted information.
    links_storage (list): A list to store URLs read from 'links.txt'.
    response (requests.Response): The response object for each HTTP request.
    soup (BeautifulSoup): The BeautifulSoup object to parse HTML content.
    raw_info (Tag): The HTML tag containing the information to be extracted.
    company (Tag): The HTML tag containing the company name.
    info (ResultSet): A list of HTML tags containing the detailed information.
    book (dict): A dictionary to store the extracted information for each URL.
    counter (int): A counter to manage JSON formatting.

File Operations:
    Reads URLs from 'links.txt'.
    Writes extracted information to 'data_book.json' in JSON format.
"""

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import requests
import json
from bs4 import BeautifulSoup

session = requests.Session()
retries = Retry(total=3, backoff_factor=5, status_forcelist=[500, 502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retries))

html_book = []

with open('links.txt', 'r') as file:
    links_storage = file.readlines()
    links_storage = [link.strip() for link in links_storage]

    for link in links_storage:
        response = session.get(link, timeout=30)

        if response.status_code == 200:
            try:
                soup = BeautifulSoup(response.content, features='html.parser')
                raw_info = soup.find('div', class_='column narrow')
                company = soup.find('h1')
                info = raw_info.find_all('li')
                book = {}
                for items in info:
                    text = items.get_text().strip()
                    book["empresa"] = company.get_text().strip()
                    if ':' in text:
                        key, value = text.split(':', 1)
                        book[key] = value
                html_book.append(book)
            except:
                pass
        print(len(html_book))


counter = 1
with open ('data_book.json','a') as file:
    file.write('[' + '\n')
    for dictionary in html_book:
        json.dump(dictionary, file)
        counter += 1
        while counter <= len(html_book):
            file.write(',' + '\n')
            break
    file.write('\n' + ']') 