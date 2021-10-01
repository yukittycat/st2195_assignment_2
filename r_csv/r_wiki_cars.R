#set wd
setwd("C:/Users/E5-471G/Documents/SIM-UOL/2021-22 Year 3/ST2195 Programming for Data Science/P02/r_csv")

#install and load rvest
install.packages("rvest")
library("rvest")

#specify the url for scraping
url <- "https://en.wikipedia.org/wiki/Comma-separated_values"

html <- url %>%
  read_html() %>%
  html_nodes(xpath = "/html/body/div[3]/div[3]/div[5]/div[1]/table[2]") %>%
  html_table()
#copied full xpath instead of xpath (unexpected mw)

#view the scraped table
html

#convert to data frame and check
cars_df <- as.data.frame(html)
cars_df

#export to csv
write.csv(cars_df, file = "r_wiki_cars.csv", row.names = FALSE)

#import r_wiki_cars.csv to a data frame to verify
read.table("r_wiki_cars.csv", header = TRUE, sep = ",")
