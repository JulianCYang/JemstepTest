#!/usr/bin/python3
import time
import redis
from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup


cache = redis.Redis(host='172.17.0.2', port=6379)
cache.set('poo', 'bar')
value = cache.get('poo')
print(value)

session = HTMLSession()
r = session.get('https://www.accuweather.com/en/za/johannesburg/305448/weather-forecast/305448')
page = requests.get("https://weather.com/en-IN/weather/tenday/l/INKA0344:1:IN")
page = requests.get("https://www.accuweather.com/en/za/johannesburg/305448/weather-forecast/305448")
soup=BeautifulSoup(page.content,"html.parser")
#print(r.html.absolute_links)
about = r.html.find('#about', first=True)

all=soup.find("div",{"class":"locations-title ten-day-page-title"}).find("h1").text
table=soup.find_all("table",{"class":"twc-table"})
l=[]
for items in table:
 for i in range(len(items.find_all("tr"))-1):
  d = {}  
  d["day"]=items.find_all("span",{"class":"date-time"})[i].text
  d["date"]=items.find_all("span",{"class":"day-detail"})[i].text
  d["desc"]=items.find_all("td",{"class":"description"})[i].text 
  d["temp"]=items.find_all("td",{"class":"temp"})[i].text 
  d["precip"]=items.find_all("td",{"class":"precip"})[i].text
  d["wind"]=items.find_all("td",{"class":"wind"})[i].text  
  d["humidity"]=items.find_all("td",{"class":"humidity"})[i].text 
  l.append(d)

print ("Hello World!")
for i in range(len(l)): 
    print (l[i])
print (r.html.search('Python is a {} language')[0])
