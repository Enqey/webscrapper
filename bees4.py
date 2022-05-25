
import requests
from bs4 import BeautifulSoup
import pandas as pd

Baseurl = 'https://www.thewhiskyexchange.com/'

headers = {
    'user agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }

plinks = []
for x in range (1,4):
    r = requests.get(f'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={x}&psize=24&sort=pasc')
soup = BeautifulSoup(r.content, 'lxml')
plist = soup.find_all('li', class_='product-grid__item')

for item in plist:
    for link in item.find_all('a', href=True):
        plinks.append(Baseurl + link['href'])
        

whisky = []
for link in plinks:
    r = requests.get(link, headers=headers) 
    soup = BeautifulSoup(r.content, 'lxml')
    name = soup.find('h1', class_='product-main__name').text.strip()
    price = soup.find('p', class_='product-action__price').text.strip()
    try:
          rating = soup.find('span', class_='review-overview__rating star-rating star-rating--50').text.strip()
    except:
          rating = 'no rating'
    whiskylinks = {
          'name' : name,
          'price' : price,
          'rating' : rating
      }
    whisky.append(whiskylinks)
    
    df = pd.DataFrame(whisky)
        
    df.to_excel('‪C:/Users/Enqey De-Ben Rockson/Downloads/data.xlsx', index = False)
    
    