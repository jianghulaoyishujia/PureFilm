import os
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

url = 'http://www.btbtdy.com/btdy/dy11263.html'

response = requests.get(url).content
# print(response.decode('utf8'))

soup = BeautifulSoup(response,'lxml')
# print(soup.prettify())
# list = soup.find_all('ul',{'class':'p_list_02'})
# name = soup.find('div').attrs['src']
pic = soup.find('div',{'class':'vod_img'}).find('img').attrs['src']

name = 'fuck'
c = requests.get(pic).content
if not os.path.exists('fuck'):
    os.mkdir('fuck')
urlretrieve(pic,'fuck/yes.jpg')
print(pic)