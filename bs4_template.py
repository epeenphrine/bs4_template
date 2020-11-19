# need lxml from pip (pip3 install lxml)
#%%
import bs4 as bs
import requests

# use requests to get HTML first

url = 'https://google.com'
res = requests.get(f"{url}").content 

soup = bs.BeautifulSoup(res, 'lxml')  # change to soup object for parsing

# find all div tags with class attribute value contentRow-snippets
div_class = soup.findAll('div', {'class': 'contentRow-snippetk'}) 

# find all a tags with href that contains text between tags  
hrefs = soup.findAll('a', href=True, text=True) 

