# This code scraps quotes from the website 'values.com' and prints each quote's theme, url, image, saying and author in a .csv file
# A CSV (comma-separated values) file stores tabular data (numbers and text) in plain text, where each line of the file typically represents one data record.
# Each record is separated by a comma

import requests
import csv
from bs4 import BeautifulSoup

URL = "https://www.values.com/inspirational-quotes"
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'}
# headers used to avoid errors
r = requests.get(url = URL, headers = headers)
soup = BeautifulSoup(r.content, 'html5lib')

quotes = [] # a list to store all the quotes
table = soup.find ('div', attrs = {'id': 'all_quotes'})

for row in table.findAll ('div', attrs = {'col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {} # a dictionary to store each quote entry
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split("#")[0]
    quote['author'] = row.img['alt'].split("#")[1]
    quotes.append(quote)
       
#print(quotes)

filename = 'inspirational_quotes.csv'
with open (filename, 'w', newline = '') as f:
    w = csv.DictWriter(f,['theme', 'url','img','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)
        f.write('\n\n')

#print(soup.prettify())





