# need lxml from pip (pip3 install lxml)
#%%
## save requests response locally 
import requests
import bs4 as bs
import json 

res = requests.get('https://google.com')
with open('data.html', 'w') as f:
    f.write(str(res.content)) ## str() to save


## load local html into bs4
with open('data.html') as f:
    soup = bs.BeautifulSoup(f, 'lxml')
div = soup.findAll('div')
print(div)

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
