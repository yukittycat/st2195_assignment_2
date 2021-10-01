# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 22:39:31 2021

@author: E5-471G
"""
#set and check the working directory
import os
os.chdir('C:/Users/E5-471G/Documents/SIM-UOL/2021-22 Year 3/ST2195 Programming for Data Science/P02/python_csv')
os.getcwd()

#import library used to query website, pandas, BeautifulSoup
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup

#specify the url
wiki = "https://en.wikipedia.org/wiki/Comma-separated_values"

#query the website and return the html
page = urllib.request.urlopen(wiki)

#parse html in page and store in soup
soup = BeautifulSoup(page)

#view structure of the html page
print(soup.prettify())

#find the cars table 
cars_table = soup.find('table', class_ = 'wikitable')
cars_table

#set as data frame
cars_df = pd.read_html(str(cars_table))[0]
cars_df

#create and export to csv
cars_df.to_csv("python_cars.csv", index = True)

#verify by importing csv into data frame
print(pd.read_csv("python_cars.csv"))