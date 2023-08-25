# Code to scrap 'Python Books from the Amazon API using Scrapingdog'
# Scrapingdog is a web scraping API that manages millions of proxies and
# thousands of headless browsers to let you scrape crucial data from any website.
# https://www.scrapingdog.com/
# Go to the website and paste the url to scrape. Copy the new code.

from bs4 import BeautifulSoup
import requests
import csv

r = requests.get("https://api.scrapingdog.com/scrape?api_key=64e80911ee737d54df64fb51&url=https://www.amazon.com/s?k=python+books&ref=nb_sb_noss_2&dynamic=false")

soup = BeautifulSoup(r.content, 'html.parser')
books = soup.find_all('div' , attrs = {'class': 'a-section aok-relative s-image-square-aspect'})

titles = []
for i in books:
    title = i.img['alt']
    titles.append(title)
print ({"Titles": titles})

filename = 'Python_books_Amazon.csv'
with open (filename, 'w', newline = '') as f:
    w = csv.writer(f)
    w.writerow(['Amazon Python Books']) # write the header
    for title in titles:
        w.writerow([title]) #write each title as a row
        f.write('\n\n')


























