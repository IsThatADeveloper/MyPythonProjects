import requests
from bs4 import BeautifulSoup as bs

# loading page
r = requests.get("https://keithgalli.github.io/web-scraping/example.html")

soup = bs(r.content)

# print(soup.prettify())

# first_header = soup.find('h2')
# print(first_header)

# headers = soup.find_all('h2')
# print(headers)

# first_header = soup.find_all(["h1", "h2"])
# print(first_header)

# paragraph = soup.find_all('p', attrs={"id": 'paragraph-id'})
# print(paragraph)

# you can nest find/findall calls

body = soup.find('body')
div = body.find('div')
header = div.find('h1')

# We can search for specific strings in our find/find_all calls
import re
p = soup.find_all("p", string=re.compile("Some")) # helpful in finding certain words in string
# print(p)

headers = soup.find_all("h2", string=re.compile("(H|h)eader")) # helpful in finding certain words in string
# print(headers)

# Select (CSS selector)
content = soup.select("div p")
# print(content)

paragraphs = soup.select("h2 ~ p")

bold_text = soup.select('p#paragraph-id b')

paragraphs = soup.select('body > p')
for paragraph in paragraphs:
    p_select = paragraph.select('i')
    # print(p_select)

header = soup.find_all("h2")
for head in header:
    h2_text = head.string
    # print(h2_text)

div = soup.find('div')
# print(div.get_text()) # multiple elements inside of div that have text

# get a property from an element
link = soup.find('a')
print(link['href'])

paragraphs = soup.select('p#paragraph-id')
# print(paragraphs[0]['id'])

# code navigation
# path syntax
# print(soup.body.div.h1.string)

# Know terms: Parent, sibling, child

# print(soup.body.find("div").find_next_siblings())



