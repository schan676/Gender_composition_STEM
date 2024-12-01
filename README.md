# Overview of Possible Gender Inequality Among TOP 20 Economics PhD Programs
[Project Descriptionk](#project-descriptionk)
[Targeted Institutions](#targeted-institutions)
[List of Schools & Departments](#list-of-schools-&-departments)
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
A majority of the data are from the very best Economics institution ranked by the US News.
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
In addition, we also include the other institutions in the UC system
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

### Data Scraing

## Code Guide - refer to files with brief description
- A table of school - correspond to the file + brief description
Job market candidate list
institution_department_jm_candidates_year.csv
Job market placement list
institution_department_jm_placements_year.csv



## Analysis

