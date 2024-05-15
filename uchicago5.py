from bs4 import BeautifulSoup
import csv

with open('2023-24 Job Market Candidates _ Kenneth C. Griffin Department of Economics.html','r') as uchicago:
    content = uchicago.read()
    
    #making the soup 
    soup = BeautifulSoup(content, 'lxml')
    
    # getting names, paper titles, and websites kind of
    a_texts = [a_tag.get_text() for a_tag in soup.find_all('a')]
    names = [h2_tag.get_text() for h2_tag in soup.find_all('h2')]
    #142
    print('Names:', names)
    

    #getting primary and secondard research focuses, references, and emails
    p_texts = [p_tag.get_text() for p_tag in soup.find_all('p')]

    info = []
    info_new = []
    primary =[]
    secondary = []
    references = []
    email = []
    website =[]
    paper_title=[]
    #for i in range(len(p_texts)):
        #info = p_texts[i].split('strong')
        #info_new.append(info[i])


    for i in range(len(p_texts)):
        info.append(p_texts[i].split('\n'))
    
    for i in range(len(info)):
        for j in range(len(info[i])):
            if 'Primary' in info[i][j]:
                primary.append(info[i][j])
            elif 'Secondary' in info[i][j]:
                secondary.append(info[i][j])
            elif 'References' in info[i][j]:
                references.append(info[i][j])
            elif 'Email' in info[i][j]:
                email.append(info[i][j])
            elif 'Website' in info[i][j]:
                website.append(info[i][j])
            else:
                paper_title.append(info[i][j])
   


    print('Primary Research Focus:', primary)
    print('Secondary Research Focus', secondary)
    print('References:', references)
    print('Email:', email)
    print('Website:', website)
    print('Paper Titles:', paper_title)
    
    #putting the lists into a csv file

    # Zip the lists to transpose rows into columns
    transposed_data = zip(names, paper_title, website, primary, secondary, references, email)

# Open CSV file in write mode
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
    
    # Write transposed data to CSV file
        for row in transposed_data:
            writer.writerow(row)

   


    