#import BeautifulSoup so you can webscrap
from bs4 import BeautifulSoup
import requests

#this is the webpage we want to scrape that has a table
url = 'https://economics.northwestern.edu/people/phd-job-market-candidates/'

#get the btml text from the url
page = requests.get(url)

#stores the html text so we can read it
soup = BeautifulSoup(page.text, 'html.parser')

#find the table, this url only has one table
table = soup.find('table')

#read the html file for just the table
#print(table)

#find the headers of the table
#may be different for each website, will figure that out later
world_titles = soup.find_all('th')

#print(world_titles)

# list comprehension => takes out the funky text and 
# gives us a list of string titles
world_table_titles = [title.text for title in world_titles]

print(world_table_titles)

import pandas as pd

df=pd.DataFrame(columns = world_table_titles)

#print(df)
'''
#tried to find names by looking for strong
strong_tags = soup.find_all('strong')
strong_texts = [tag.get_text().strip() for tag in strong_tags]
print(strong_texts)'''

'''
#trying to pull names from table
elements_with_aria_label = soup.find_all(lambda tag: tag.has_attr('aria-label'))

#loop to grab all the names maybe
for element in elements_with_aria_label: 
    aria_label_text = element['aria-label']
    print(f"Aria-label text: {aria_label_text}")'''
'''
column_data = soup.find_all('td')
for row in column_data:
    row_data = row.find_all('td')
    row_data_text = [data.text.strip() for data in row_data]
    print(row_data)'''

#finds the data in the table
'''column_data = table.find_all('tr')
for row in column_data:
    row_data=row.find_all('a')
    row_data_text = aria-label.text.strip() for 
    print(row_data)'''