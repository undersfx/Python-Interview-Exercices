import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/')

soup = bs.BeautifulSoup(source, 'lxml')

# NAV BAR CONTENT
nav = soup.nav
for url in nav.find_all('a'):
    print(url.get('href'), '\n')

# BODY CONTENT
body = soup.body
for p in body.find_all('p'):
    print(p.text, '\n')

# DIV CLASS BODY CONTENT
for div in soup.find_all('div', class_='body'):
    print(div.text)

# TABLE DATA
table = soup.table # or
table = soup.find('table')

table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)