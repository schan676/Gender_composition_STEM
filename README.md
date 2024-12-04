# Overview of Possible Gender Inequality Among TOP 20 Economics PhD Programs
## Table of Content
- [Project Overview](#project-overview)

- [Targeted Institutions](#targeted-institutions)

- [Data Processing Steps](#data-processing-steps)

- [Code Guide - refer to files with brief description](#code-guide---refer-to-files-with-brief-description)

- [Analysis](#analysis)

## Project Overview
### About
For this project, we collected comprehensive data on job market candidates from the top 20 Economics PhD programs in the United States, including information on gender, fields of study, and dissertation topics. Additionally, we gathered job placement data from the same institutions to analyze the employment outcomes (e.g., company or institution, position) of graduating PhD students.

Our analysis involved generating summary statistics and conducting regression analyses to examine the relationship between gender and job placement outcomes.
### Contributions:
- Lea Angelakos
- Samantha Chan
- Amy Dao
- Chris Luo
- Jia Yi (Tracy) Zhao


## Targeted Institutions
### Top 20  Economics Schools (US News, 2022)
A majority of the data are from the very best Economics institution ranked by the US News:
- Harvard
- MIT
- Stanford
- Princeton
- University of California, Berkeley
- University of Chicago
- Yale University
- Northwestern University
- Columbia University
- University of Pennsylvania
- New York University
- University of California, Los Angeles
- University of Michigan, Ann Arbor
- California Institute of Technology
- Cornell University
- University of California, San Diego
- University of Wisconsin, Madison
- Duke University
- University of Minnesota, Twin Cities
- Brown University

### Additional Schools:
In addition, we also include the other institutions in the UC system:
- University of California, Davis
- University of California, Merced
- University of California, Riverside
- University of California, Irvine

### Schools & Departments
|University                            |department       |
|--------------------------------------|-----------------|
|Harvard University                    |Economics        |
|Massachusetts Institute of Technology |Economics        |
|Stanford                              |Economics        |
|Princeton                             |Economics        |
|University of California, Berkeley    |Economics        |
|University of California, Berkeley    |HASS             |
|University of California, Berkeley    |ARE              |
|University of Chicago                 |Buisness         |
|University of Chicago                 |Economics        |
|Yale University                       |Economics        |
|Northwestern                          |Economics        |
|Northwestern                          |Economics        |
|Columbia University                   |Economics        |
|University of Pennsylvania            |Economics        |
|New York Univiersity                  |Economics        |
|University of California, Los Aangeles|Economics        |
|University of Michigan, Ann Arbor     |Economics        |
|California institue of Technology     |Economics        |
|Cornell University                    |Economics        |
|UC San Diego                          |Business         |
|UC San Diego                          |Economics        |
|UC San Diego                          |Political Science|
|University of Wisconsin, Madison      |Economics        |
|Duke University                       |Economics        |
|University of Minnesota, Twin Cities  |Economics        |
|Brown University                      |Economics        |
|UC Merced                             |Economics        |
|UC Merced                             |Political Science|
|UC Davis                              |Economics        |
|UC Davis                              |Political Science|


## Data Processing Steps
### Identifying the attribute
| Column Name         | Description                            |
|---------------------|----------------------------------------|
| name                | Full name                             |
| gender_guess        | Gender using `gender_guesser`         |
| school_website      | School website                        |
| field               | Field of interest                     |
| paper_name          | Job market paper name                 |
| paper_link          | Link to job market paper              |
| chair               | Chair                                 |
| committee_members   | Committee members                     |
| year                | Year of completion                    |
| university          | University name                       |
| department          | Department                            |
| cv_link             | Link to CV                            |
| thesis              | Dummy if thesis is downloaded         |
| personal_website    | Personal website                      |
| placement           | Where candidates were placed          |
| placement_type      | Type of placement                     |
| academic            | Dummy if `placement_type` is academic |
| postdoc             | Dummy if placement was postdoc        |
| gender_manual       | Manual fixes for gender               |
| thesis_name         | Name of thesis                        |

### Data Scraping 
This table shows our current status with retrieving the relevant data:

|school                                |department       |jmc available?|jmc years available|have we scraped it?(JMC|placement available?(name,instituion,job title)|placement years available|have we scraped it?(historical placements)|Contributor        |website link                                                       |
|--------------------------------------|-----------------|--------------|-------------------|-----------------------|-----------------------------------------------|-------------------------|------------------------------------------|-------------------|-------------------------------------------------------------------|
|Harvard University                    |Economics        |1             |[2024]             |0                      |name. institution                              |[2005,2023]              |0                                         |Chris Luo          |https://www.economics.harvard.edu/job-placement                    |
|Massachusetts Institute of Technology |Economics        |1             |[2024]             |0                      |institution                                    |[2019,2023]              |0                                         |Chris Luo          |https://economics.mit.edu/academic-programs/phd-program/job-market |
|Stanford                              |Economics        |              |[2023]             |1                      |name, institution                              |[2005,2025]              |0                                         |                   |                                                                   |
|Princeton                             |Economics        |              |                   |                       |                                               |[2010,2024]              |0                                         |                   |                                                                   |
|University of California, Berkeley    |Economics        |1             |[2024]             |1                      |institution, job title                         |[2006,2024]              |1                                         |Chris Luo          |https://econ.berkeley.edu/graduate/professional-placement          |
|University of California, Berkeley    |HASS             |1             |[2024]             |1                      |name, institution, job title                   |[2013,2024]              |1                                         |Chris Luo          |https://haas.berkeley.edu/phd/careers/                             |
|University of California, Berkeley    |ARE              |0             |[]                 |0                      |name, institution, job title                   |[2003,2024]              |1                                         |Chris Luo          |https://are.berkeley.edu/job-candidates                            |
|University of Chicago                 |Buisness         |1             |[2024]             |1                      |0                                              |0                        |0                                         |Chris Luo          |https://www.chicagobooth.edu/phd/career-outcomes                   |
|University of Chicago                 |Economics        |1             |[2024]             |1                      |0                                              |0                        |0                                         |Chris Luo          |https://economics.uchicago.edu/people/2024-25-job-market-candidates|
|Yale University                       |Economics        |1             |[2024]             |1                      |name, institution                              |[1998,2024]              |1                                         |Samantha Chan      |                                                                   |
|Northwestern                          |Economics        |              |[2024]             |1                      |                                               |[2005,2024]              |0                                         |Lea Angelakos      |                                                                   |
|Northwestern                          |Economics        |              |[2023]             |1                      |                                               |                         |0                                         |                   |                                                                   |
|Columbia University                   |Economics        |1             |[2024]             |1                      |name, institution                              |[2011,2024]              |1                                         |Jia Yi (Tracy) Zhao|                                                                   |
|University of Pennsylvania            |Economics        |1             |[2024]             |1                      |name, institution                              |[2006,2024]              |1                                         |Jia Yi (Tracy) Zhao|                                                                   |
|New York Univiersity                  |Economics        |1             |[2024]             |0                      |institution                                    |[2012, 2023]             |0                                         |Chris Luo          |https://as.nyu.edu/departments/econ/job-market.html                |
|University of California, Los Aangeles|Economics        |1             |[2024]             |0                      |name, institution, job title                   |[1999, 2023]             |0                                         |Chris Luo          |https://economics.ucla.edu/                                        |
|University of Michigan, Ann Arbor     |Economics        |1             |[2024]             |0                      |name, institution                              |[2014, 2023]             |0                                         |Chris Luo          |https://lsa.umich.edu/econ/doctoral-program/                       |
|California institue of Technology     |Economics        |1             |[2024]             |0                      |0                                              |0                        |0                                         |Chris Luo          |https://www.hss.caltech.edu/graduate-studies/job-market-candidates |
|Cornell University                    |Economics        |1             |[2024]             |0                      |name, job title                                |[2007.2023]              |0                                         |Chris Luo          |https://economics.cornell.edu/node/4828                            |
|UC San Diego                          |Business         |1             |[2023]             |1                      |                                               |                         |1                                         |Amy Dao            |                                                                   |
|UC San Diego                          |Economics        |1             |[2024]             |1                      |                                               |                         |1                                         |Amy Dao            |                                                                   |
|UC San Diego                          |Political Science|1             |[2024]             |1                      |                                               |                         |1                                         |Amy Dao            |                                                                   |
|University of Wisconsin, Madison      |Economics        |1             |[2024]             |0                      |name, institution, job title                   |[2010, 2023]             |0                                         |Chris Luo          |https://econ.wisc.edu/doctoral/                                    |
|Duke University                       |Economics        |1             |[2024]             |0                      |0                                              |0                        |0                                         |Chris Luo          |https://econ.duke.edu/graduate/hire-duke-phd                       |
|University of Minnesota, Twin Cities  |Economics        |0             |[]                 |0                      |name, institution, job title                   |[2012, 2023]             |0                                         |Chris Luo          |https://cla.umn.edu/economics/graduate/job-placement-achievements  |
|Brown University                      |Economics        |1             |[2024]             |0                      |0                                              |0                        |0                                         |Chris Luo          |https://economics.brown.edu/job-market-candidates-0                |
|UC Merced                             |Economics        |              |[2024]             |1                      |                                               |                         |                                          |Amy Dao            |                                                                   |
|UC Merced                             |Political Science|              |[2024]             |1                      |                                               |                         |                                          |Amy Dao            |                                                                   |
|UC Davis                              |Economics        |              |[2024]             |1                      |                                               |                         |                                          |Amy Dao            |                                                                   |
|UC Davis                              |Political Science|              |[2024]             |1                      |                                               |                         |                                          |Amy Dao            |                                                                   |

### Data Cleaning
Here is an excerpt of our merged dataset, refer to [this](data/clean/gender_gap_PhD_STEM.csv) for detail information: 
| Name               | Gender Guess | School Website                                   | Field                                      | Paper Name                                         | Paper Link                                   | Chair                          | Committee Member                            | Year  | University           | Placement                                      | Placement Type   | Academic | Postdoc | Degree | References |
|--------------------|--------------|------------------------------------------------|-------------------------------------------|---------------------------------------------------|----------------------------------------------|-------------------------------|---------------------------------------------|-------|----------------------|------------------------------------------------|------------------|----------|---------|--------|-----------|
| Dong Woo Hahm      | andy         | http://dongwoohahm.com                         | Applied Microeconomics, Economics of Education, Labor | Leveraging Uncertainties to Infer Preferences: An Application | [Link](https://econ.columbia.edu/wp-content/uploads/s...) | Yeon-Koo Che, Miguel Urquiola | Pierre-André Chiappori, YingHua He           | 2024  | Columbia University  | University of Southern California (Teaching) | Academic         | 1.0      | 0.0     | NaN    | NaN       |
| Susannah Scanlan   | female       | https://econ.columbia.edu/e/susannah-scanlan/ | Macroeconomics, Econometrics              | Attention Allocation and the Factor Structure     | [Link](https://econ.columbia.edu/wp-content/uploads/s...) | Serena Ng, Michael Woodford   | Hassan Afrouzi, Jennifer La'O               | 2024  | Columbia University  | Capital Fund Management                       | International Org | 0.0      | 0.0     | NaN    | NaN       |
| Seung-hun Lee      | unknown      | https://seunghunlee918.github.io              | Development Economics, Political Economy, Public Policy | Organized Crime, Local Politicians, and State Capacity | [Link](https://econ.columbia.edu/wp-content/uploads/s...) | Suresh Naidu                  | Michael Best, Rodrigo Soares                | 2024  | Columbia University  | Post-doc HKUST-SNUTaipei School of Economics | Academic         | 1.0      | 1.0     | NaN    | NaN       |
| Qianyang Zhang     | unknown      | http://qianyangz.github.io                    | Industrial Organization, Microeconomics, Urban Economics | Equilibrium Effects of Energy Efficiency Disclosures | [Link](https://econ.columbia.edu/wp-content/uploads/s...) | Don Davis, David Weinstein    | Gautam Gowrisankaran                         | 2024  | Columbia University  | Amazon                                        | Industry         | 0.0      | 0.0     | NaN    | NaN       |
| Parijat Lal        | male         | http://www.parijatlal.com                     | Development Economics, Public Economics, Labor | Cooperatives, Competition, and Compensation: Evidence from... | [Link](https://econ.columbia.edu/wp-content/uploads/s...) | Michael Best                   | Joseph Stiglitz, Eric Verhoogen, Jack Willis | 2024  | Columbia University  | Post-doc Columbia Business School            | Academic         | 1.0      | 1.0     | NaN    | NaN       |


## Code Guide 
### Data Scraping using Python
Here is a **very** brief overview of how data scraping works with Python.
1. **Import Required Packages**:
    - To start, you should install and import required packages.
    - Use `requests` to fetch webpage content.
    - Use `BeautifulSoup` from `bs4` for parsing HTML data.
   ```python
   import requests
   from bs4 import BeautifulSoup
   ```
2. **Fetch Webpage Content**:
    - Use requests.get(URL) to retrieve the HTML or text from a website.
    ```python
    response = requests.get("https://example.com")
    html_content = response.text
     ```
3. **Parse HTML Content**:
    - Use BeautifulSoup to convert raw HTML into a navigable object.
    ```python
    soup = BeautifulSoup(html_content, "html.parser")
    ```
4. **Extract Data**:
    - Locate elements using tags, classes, or IDs (e.g., soup.find_all('tag')).
    ```python
    data = soup.find_all('div', class_='data-class')
    ```
5. **Clean and Structure Data**:
    - Process extracted data into a structured format (e.g., list or dictionary).
6. **Save Data to CSV**:
    - Use pandas or csv to save data for analysis.
    ```python
    import pandas as pd
    df = pd.DataFrame(data)
    df.to_csv("output.csv", index=False)
    ```

### Corresponding files
Please refer to file_guide spreadsheet to see a more specific format of this section of the Readme:
| File Name                                    | Description                                                                                       |
|---------------------------------------------|---------------------------------------------------------------------------------------------------|
| [NYU_code.py](code/build/NYU_code.py)       | Python script for NYU data scraping and analysis.                                                |
| [UCB_UCHICAGO_SCRAPE.ipynb](code/build/UCB_UCHICAGO_SCRAPE.ipynb) | Jupyter notebook for scraping UCB and UChicago candidate information.                           |
| [UCD_EconPhD.ipynb](code/build/UCD_EconPhD.ipynb) | Jupyter notebook for UC Davis Economics PhD data extraction and processing.                     |
| [UCD_PoliSciPhD.ipynb](code/build/UCD_PoliSciPhD.ipynb) | Jupyter notebook for UC Davis Political Science PhD data handling.                              |
| [UCM_EconPhD.ipynb](code/build/UCM_EconPhD.ipynb) | Jupyter notebook for UC Merced Economics PhD data analysis.                                     |
| [UCM_PoliSciPhD.ipynb](code/build/UCM_PoliSciPhD.ipynb) | Jupyter notebook for UC Merced Political Science PhD data scraping and processing.              |
| [UCSD_BusinessPhD.ipynb](code/build/UCSD_BusinessPhD.ipynb) | Jupyter notebook for UCSD Business PhD data analysis.                                           |
| [UCSD_EconPhD.ipynb](code/build/UCSD_EconPhD.ipynb) | Jupyter notebook for UCSD Economics PhD data extraction and cleaning.                           |
| [UCSD_PoliSciPhD.ipynb](code/build/UCSD_PoliSciPhD.ipynb) | Jupyter notebook for UCSD Political Science PhD candidate analysis.                             |
| [chicago8.py](code/build/chicago8.py)       | Python script for processing University of Chicago PhD candidate information.                    |
| [nwecon2.py](code/build/nwecon2.py)         | Python script for Northwestern Economics candidate data processing.                              |
| [stanford.py](code/build/stanford.py) | Script for Stanford PhD candidate data scraping with personal website extraction.               |
| [test6.py](code/build/test6.py)             | General-purpose test script for data extraction and processing.                                  |
| [u_chicago_v9.py](code/build/u_chicago_v9.py) | Python script for advanced data handling of University of Chicago PhD candidates.               |
| [upenn_econ.csv](code/build/upenn_econ.csv) | CSV file containing Economics PhD candidate data from the University of Pennsylvania.            |
| [yale_econ.ipynb](code/build/yale_econ.ipynb) | Jupyter notebook for Yale Economics PhD candidate data analysis.                                |
| [yale_econ_phd_candidates.csv](code/build/yale_econ_phd_candidates.csv) | CSV file containing PhD candidate information from Yale Economics department.                   |

## Analysis
### Key Insights
- **Placement by Type**:
  - 60.48% of candidates were placed in academic positions.
  - 13.73% went to industry roles.
  - 11.08% of candidates became postdocs.

For detailed results, see [Gender Gap PhD STEM Analysis](data/clean/gender_gap_PhD_STEM_analysis.txt).

