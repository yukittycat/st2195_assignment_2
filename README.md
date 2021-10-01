# Practice Assignment 02

Create  a GitHub repository called “st2195_assignment_ 2 ” that includes:
1. a README.md file with a short markdown description of this assignment [1 point]
2. a folder called "r_csv" with a R code for scraping the CSV example on cars (we want the table) in the Wikipedia page https://en.wikipedia.org/wiki/Comma-separated_values and saving the resulting output in the local folder (in CSV) [4.5 points]
3. a folder called "python_csv" with a Python version of the code in point 2 [4.5 points]

It is advised to use the packages rvest (R) and BeautifulSoup (Python) for scraping operations. RSelenium (R) and Selenium (Python) can also be used, but they are generally more complicated to setup.

Hint: You may want to have a look at https://rvest.tidyverse.org/articles/harvesting-the-web.html

Additional notes on task clarification:
  + Look for the example cars table from the Wikipedia URL
  + Scrape the table and write to a file in CSV format
  + Read the CSV file to a data frame to verify that it was correctly saved
