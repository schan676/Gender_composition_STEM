#have to install BeautifulSoup and Regex and requests

import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
import requests


url = 'https://economics.uchicago.edu/people/job-market-candidates'
page = requests.get(url)
soup = bs(page.text, 'html.parser')

#load html code froma  url


#print(soup)

names = soup.body.findAll('h2')

#to make this easier to read:
def horizontal_to_vertical(lst):
    for item in lst:
        print(item)


#print("websites:")
horizontal_to_vertical(names)

#cleaning the <h2> off
#find all <h2> and this time keep the links
h2_tags = soup.find_all('h2')
headings_with_links = []

for tag in h2_tags:
    heading_text = tag.get_text() #extracts text from h2
    href_attr = tag.find('a')['href'] if tag.find('a') else None # tries to find an a tag within h2
    headings_with_links.append((heading_text, href_attr))#adds to list
#print the cleaned headings with href links
for heading, href in headings_with_links:
    if href:
        print(f"{heading}: {href}")
    else:
        print(heading)

