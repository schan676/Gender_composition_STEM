# Overview of Possible Gender Inequality Among TOP 20 Economics PhD Programs
[Project Descriptionk](#project-descriptionk)
[TOP 20 School](#top-20-school)
[List of Schools & Departments](#list-of-schools-&-departments)
[Data Processing Steps](#data-processing-steps)
[Code Guide - refer to files with brief description](#code-guide---refer-to-files-with-brief-description)
[Analysis](#analysis)

## Project Overview
### About
We scraped job market candidate information from the top 20 Economics PhD Programs in the U.S., including gender, fields of study, and dissertation topics. We also scraped job market placement information from the same schools to track the employment status (company/institution, position) of each PhD student upon graduation.

We then conducted summary statistics and regression analyses to understand the correlation between gender and job placement.

### Contributions:
- Contribution 1
- Contribution 2

## TOP 20 School
### Best Economics Schools (US News, 2022)

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
- University of California, Davis
- University of California, Merced
- University of California, Riverside
- University of California, Irvine

## List of Schools & Departments
- Scrape/processed 
Departments scraped/processed:
Economics
Political Science
Business
Public Policy

## Data Processing Steps
- Describe the columns, jmc, jm placements, jm types, gender
Job Market Candidates:
first_name
last_name
school
gender
gender_guess
gender_manual
year
school_website
personal_website
chair
committee_member
field
cv_link
jm_paper
paper_link
department
dissertation
thesis
Job Market Placements:
placement
academic (binary)
placement_type
postdoc
permanent_job
Packages and Methods:
Gender guesser package
Infer academic/non-academic placement with ChatGPT

## Code Guide - refer to files with brief description
- A table of school - correspond to the file + brief description
Job market candidate list
institution_department_jm_candidates_year.csv
Job market placement list
institution_department_jm_placements_year.csv



## Analysis

