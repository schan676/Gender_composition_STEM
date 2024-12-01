# Overview of Possible Gender Inequality Among TOP 20 Economics PhD Programs
## Table of Content
[Project Descriptionk](#project-descriptionk)

[Targeted Institutions](#targeted-institutions)

[Schools & Departments](#schools-&-departments)

[Data Processing Steps](#data-processing-steps)

[Code Guide - refer to files with brief description](#code-guide---refer-to-files-with-brief-description)

[Analysis](#analysis)

## Project Overview
### About
For this project, we collected comprehensive data on job market candidates from the top 20 Economics PhD programs in the United States, including information on gender, fields of study, and dissertation topics. Additionally, we gathered job placement data from the same institutions to analyze the employment outcomes (e.g., company or institution, position) of graduating PhD students.

Our analysis involved generating summary statistics and conducting regression analyses to examine the relationship between gender and job placement outcomes.
### Contributions:
- Contribution 1
- Contribution 2

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

## Schools & Departments
- Scrape/processed 
Departments scraped/processed:
Economics
Political Science
Business
Public Policy

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
### Data Scraing - Overview
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


## Code Guide - refer to files with brief description

## Analysis

