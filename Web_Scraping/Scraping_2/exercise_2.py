import requests
from bs4 import BeautifulSoup as bs

url = "https://keithgalli.github.io/web-scraping/"
r = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")

web = bs(r.content)

## Task 1 grab all social links from webpage, 3 diff ways

# social = web.select('ul .social')
# for link in social:
#     a = link.find('a')
#     print(a['href'])

# or 

# links = web.select("ul .social a")
# actial_links = [link['href'] for link in links]
# print(actial_links)

# or

# ulist = web.find('ul', attrs={"class": "socials"})
# links = ulist.find_all('a')
# actial_links = [link['href'] for link in links]
# print(actial_links)

# or

# links = web.select("li.social a")
# print(links)

## Table scrape
# table = web.find('table', attrs={'class': 'hockey-stats'})
# info = table.find('thead')
# print(info)

import pandas as pd

table = web.select('table.hockey-stats')[0]
columns = table.find('thead').find_all('th')
column_names = [c.string for c in columns]

rows = table.find('tbody').find_all('tr')
l = []
for tr in rows:
    td = tr.find_all('td')
    row = [str(tr.get_text()).strip() for tr in td]
    l.append(row)

df = pd.DataFrame(l, columns=column_names)
# print(df.loc[df['Team'] != 'Did not play'])
    

## Grab all the fun facts that have is in it

import re

fun_fact = web.select('ul.fun-facts li')
fun_fact_is = [fact.find(string=re.compile('is')) for fact in fun_fact]
fun_fact_is = [fact.find_parent().get_text() for fact in fun_fact_is if fact]
# print(fun_fact_is)

# is_fun_fact = fun_fact.find_all('li')
# for fact in is_fun_fact:
#     fact.string
#     print(fact.get_text()) # multiple elements inside of div that have text

## How to go to webpage and download images

# images = web.select('div.row div.column img')
# image_url = images[0]['src']
# full_url = url + image_url

# img_data = requests.get(full_url).content
# with open('image_name.jpg', 'wb') as handler:
#     # handler.write(img_data)

## Scrape secret message

files = web.select("div.block a")
relative_files = [f['href'] for f in files]

for f in relative_files:
    full_url = url + f
    page = requests.get(full_url)
    bs_page = bs(page.content)
    secret_word = bs_page.find("p", attrs={'id': 'secret-word'}).string
    print(secret_word)

    

