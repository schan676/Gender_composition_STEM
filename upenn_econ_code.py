import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape
url = "https://economics.sas.upenn.edu/graduate/job-market-candidates"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Table that contains the information
table = soup.find_all("table")[2]

# Find all the rows containing the desired information
rows = table.find_all("tr") 

# exclude the fields row
del rows[0]

# Initialize lists to store data
names = []
interests = []
market_papers = []
advisors = []
links = []

# Iterate through each row and extract the desired information
for row in rows:
    # Extract name
    name_tag = row.find("a")
    if name_tag:
        name = name_tag.text.strip()
    
    # Extract interest
    interest_tag = row.find("p")
    if interest_tag:
        interest = interest_tag.text.strip()
    
    # Extract market paper title
    paper_tag = row.find("h5")
    if paper_tag:
        paper = paper_tag.text.strip()
    
    # Extract advisor
    advisor_tag = row.find(class_="views-field-field-advisors")
    if advisor_tag:
        advisor = advisor_tag.text.strip()
    
    # Extract website
    link = name_tag['href'] if name_tag else None

    # Append extracted data to lists
    names.append(name)
    interests.append(interest)
    market_papers.append(paper)
    advisors.append(advisor)
    links.append(link)
    
# Create a DataFrame to store the extracted data
data = {
    "Name": names,
    "Personal Website": links,
    "Interest": interests,
    "Market Paper Title": market_papers,    
    "Advisors": advisors
}

df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("upenn_econ.csv", index=False)
