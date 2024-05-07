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
#find all <h2>
h2_tags = soup.find_all('h2')
headings = [tag.get_text() for tag in h2_tags]

#remove <h2> tags from extracted headings
cleaned_headings = [re.sub(r'<h2>|</h2>', '', heading) for heading in headings]

#print the cleaned headings
for heading in cleaned_headings:
    print(heading)