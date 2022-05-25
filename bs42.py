import requests 
from bs4 import BeautifulSoup
import pandas as pd 
import time

Baseurl = 'https://www.coursesghana.com'

headers = {
    'user agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
   
    }

slink = []
#for x in range (1,61,30):
r = requests.get('https://www.coursesghana.com/schools/?start=31&SchoolType=private%20primary%20schools')
soup = BeautifulSoup(r.content, 'lxml')
slist = soup.find_all('td')
    
     
for td_tag in slist:
    #if td_tag is not None and 'href' in td_tag.find_all: 
        for link in td_tag.find_all('a', href=True):
        
          slink.append(Baseurl + link['href'])
            
school = []

for link in slink:
        r = requests.get(link, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        name = soup.find('span', id_='ContentPlaceHolder1_lblSchoolName').text.strip() 
        try:
            email = soup.find('span', id_='ContentPlaceHolder1_lblEmail').text.strip()
        except:
            email = 'no email'
        try:
            city = soup.find('span', id_='ContentPlaceHolder1_lblCity').text.strip()
        except:
            city = 'no city'
        try:        
            phone = soup.find('span', id_='ContentPlaceHolder1_lblPhoneNumber1').text.strip()
        except:
            phone = 'no phone'
schools = {
            'name': name,
            'email': email,
            'city' : city,
            'phone' : phone 
           }
df = pd.DataFrame(school)
print(df.head(15))
time.sleep(6)