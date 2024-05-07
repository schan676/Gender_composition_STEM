# need to install pandas and lxml before running this code for a website that has a table

import pandas as pd
import ssl

ssl._create_default_https_context=ssl._create_unverified_context


scraper = pd.read_html('https://economics.northwestern.edu/people/phd-job-market-candidates/')

print(scraper)
