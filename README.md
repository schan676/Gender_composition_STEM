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

### Data Scra

## Code Guide - refer to files with brief description
- A table of school - correspond to the file + brief description
Job market candidate list
institution_department_jm_candidates_year.csv
Job market placement list
institution_department_jm_placements_year.csv



## Analysis

