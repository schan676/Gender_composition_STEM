'''
Lea Angelakos UChicago web scraping code

This code should go through the job market candidates for the economics department
of U Chicago. Then it will put the data scraped in a pandas dataframe and export 
into a csv file to append to the main one. Hopefully this will also be able to 
guess the gender of the names on this list

'''

# importing pandas to make a data frame and importing beautiful soup to be able to 
# web scrape and other things to make the code work


import os
import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
import requests
#import gender_guesser.detector as gender

# changing the working directory


# the url for uchicago econ job market
url = "https://economics.uchicago.edu/people/job-market-candidates"

'''
with open('2023-24 Job Market Candidates _ Kenneth C. Griffin Department of Economics.html','r') as uchicago:
    content = uchicago.read()

    print(content)'''

#making the soup 
url = "https://economics.uchicago.edu/people/job-market-candidates"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

data = []
#grabbing data from only the division i want
values = soup.find_all("div", class_="paragraph paragraph--type--uc-text-block paragraph--view-mode--default")

#print(values)


#creating item columns
#the following code runs through the data in the divider that has the attributes
#that associate with the value
for people in values:
    
    item = {}
    item['name'] = people.find("a").text # pulls name
    # i found a page that has this years placements, but i am short on time so I am putting in in
# manually

    # all academic tenure track positions
    if 'Santiago Franco' in item['name']:
        item['placement'] = 'Boston University'

    if 'Sangmin (Simon) Oh' in item['name']:
        item['placement'] = 'Colmbia GSB'

    if 'Sulagna Dasgupta' in item['name']:
        item['placement'] = 'Cornell University'

    if 'Toshiaki Komatsu' in item['name']:
        item['placement'] = 'National Taiwan University'

    if 'Aleksei Oskolkov' in item['name']:
        item['placement'] = 'Princeton University'

    if 'Estéfano Rubio' in item['name']:
        item['placement'] = 'Universidad Adolfo Ibanez'

    if 'Marcos Sora' in item['name']:
        item['placement'] = 'University of Illinois at Urbana-Champaign'

    if 'Michael Varley' in item['name']:
        item['placement'] = 'University of Kentucky'

    if 'Zhiyu Fu' in item['name']:
        item['placement'] = 'Washington University in St. Louis'

    # all academic non tenure track
    if 'Ivan Kwok' in item['name']:
        item['placement'] = 'Brown University'

    if 'Sidharth Sah' in item['name']:
        item['placement'] = 'New York University Center for Data Science'

    # public sector
    if 'Michael Galper' in item['name']:
        item['placement'] = 'Dapartment of Justice Expert Analysis Group'

    if 'Hazen Eckert' in item['name']:
        item['placement'] = 'National Security Agency'

    if 'Harshil Sahai' in item['name']:
        item['placement'] = 'World Bank Young Professionals'

    # private sector
    if 'Maria Ignacia Cuevas de Saint Pierre' in item['name']:
        item['placement'] = 'Amazon'

    if 'Nadia Lucas' in item['name']:
        item['placement'] = 'Amazon'

    if 'Jingtao Zheng' in item['name']:
        item['placement'] = 'Citadel Securities'

    if 'Scott Behmer' in item['name']:
        item['placement'] = 'RAND'

    # post doc
    if 'Shanon Hsu-Ming Hsu' in item['name']:
        item['placement'] = 'The University of Chicago'

    if 'Elena Istomina' in item['name']:
        item['placement'] = 'The University of Chicago'
    item['school'] = "University of Chicago" # school is the same for everyone
    item['year'] = 2024 # year is the same for everyone
    #item['prim_research_focus'] = people.find("span").strong
    extra = people.find("p").text # getting job market paper, research focuses, advisors, email, and personal website

    links = people.find_all('a', href = True) #finds all links 
    for link in links: # stripping the links and sorting them
        if "pdf" in link['href']:
            item['job_market_paper'] = link['href']

        elif "drive" in link['href']:
            item['job_market_paper'] = link['href']

        elif "economics.uchicago" in link['href']:
            item['school_website'] = link['href']

        else:
            item['personal_website'] = link['href']
    
    #defining words to split
    words_to_split_at = ["Primary Research Focus:", "Secondary Research Focus:", "References:", \
                         "Job Market Paper Title:", "Email:"]
    #creating a regular expression pattern
    pattern = '|'.join(re.escape(word) for word in words_to_split_at)

    split_text = re.split(pattern, extra)

    if 1< len(split_text) < 6 :
        item['research_focus_1'] = split_text[1]
        item['references'] = split_text[2]

    elif 5<len(split_text):
        item['research_focus_1'] = split_text[1]
        item['research_focus_2'] = split_text[2]
        item['references'] = split_text[3]




    data.append(item)

if item['name'] == 'Ufuk Akcigit':
    data.remove(item)

df = pd.DataFrame(data)



df.to_csv("uchicago_econ24.csv")