"""
This script reads a list of URLs from a file named 'links.txt' and attempts to retrieve each URL using the requests library.
It uses a session with retry logic to handle transient errors.
Modules:
    requests: To make HTTP requests.
    requests.adapters: To configure HTTP adapters for the session.
    urllib3.util.retry: To configure retry logic for the session.
Functions:
    None
Variables:
    session (requests.Session): A session object with retry logic configured.
    retries (Retry): A Retry object with retry configuration.
    i (int): A counter to keep track of successfully retrieved links.
    links_storage (list): A list to store URLs read from 'links.txt'.
    response (requests.Response): The response object returned by the session.get() method.
Usage:
    The script reads URLs from 'links.txt', attempts to retrieve each URL, and counts the number of successful retrievals.
    It prints the number of successfully retrieved links at the end.
"""

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import requests

session = requests.Session()
retries = Retry(total=3, backoff_factor=5, status_forcelist=[500, 502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retries))

i=0

with open ('links.txt', 'r') as file:
    links_storage = file.readlines()
    links_storage = [link.strip() for link in links_storage]
    
    for links in links_storage:
        try:
            response = session.get(links, timeout=30)
            if response.status_code == 200:
                i += 1
            else:
                print(f'Failed to retrieve {links}')
        except requests.exceptions.RequestException as e:
            print(f'Failed to retrieve {links}')

print(f'Successfully retrieved {i} links')