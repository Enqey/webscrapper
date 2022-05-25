# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 15:29:45 2021

@author: Enqey De-Ben Rockson
"""

import requests 
from bs4 import BeautifulSoup as bs 

url = "http://172.20.10.3/"

headers = {
    
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    
    }

data = requests.get(url)

#print(data.status_code)

source = data.content

#print(source)

soup = bs(source, 'lxml')

links = soup.find_all("td")

for link in links:
    if "FAudio" in link.text:
       print(link)
       print(link.attrs['class'])
        
#urls = []
#for link in soup.find_all("td"):
 #   b = link.find("button")
   #if b is not None and 'class' in a_tag.attrs:
   #     L = a_tag.get('class')
  #  urls.append(b.attrs('type'))

#print(urls)



