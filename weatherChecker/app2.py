#!/usr/bin/python3
#https://medium.com/@aakankshaws/using-beautifulsoup-requests-to-scrape-weather-data-9c6e9d317800
import time
import redis
from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup
import json
import pymongo

def insertValue(test,key,value):
  test.set(key,value)

cache = redis.Redis(host='172.17.0.2', port=6379)
insertValue(cache,'tester', 'bread')
value = cache.get('tester')
#print(value)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["tester"]


response = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=3820d6b1e287dc0ebe4436e2e41ae3fa")
data = response.json()
print ('Temperature: ' , data['list'][0]['main']['temp'])
#print(data['list'])
#print (data['list']['main']['pressure'])
#print(response.status_code)
#print (response.headers)

#session = HTMLSession()
#r = session.get('https://www.accuweather.com/en/za/johannesburg/305448/weather-forecast/305448')
#page = requests.get("https://weather.com/en-IN/weather/tenday/l/INKA0344:1:IN")
#page = requests.get("https://www.accuweather.com/en/za/johannesburg/305448/weather-forecast/305448")
#about = r.html.find('#about', first=True)

#print (r.html.search('Python is a {} language')[0])
