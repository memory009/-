import requests
from bs4 import BeautifulSoup
from selenium import webdriver
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url='http://forecast.weather.com.cn/town/weather1dn/101280101004.shtml#around2'
res=requests.get(url,headers=headers)
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')
temperature= soup.find(class_='temp').text
wind= soup.find(class_='wind').text
min_tem=soup.find(class_='minMax').find('span')
print(wind)
print(temperature)
print(min_tem)
#tem=temperature.text
# wind=wind1.text