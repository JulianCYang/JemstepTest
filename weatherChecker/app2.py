#!/usr/bin/python3
#https://medium.com/@aakankshaws/using-beautifulsoup-requests-to-scrape-weather-data-9c6e9d317800
import time
import redis
from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup

def insertValue(key,value):


cache = redis.Redis(host='172.17.0.2', port=6379)
cache.insertValue('poo', 'bar')
value = cache.get('poo')
print(value)

session = HTMLSession()
r = session.get('https://www.accuweather.com/en/za/johannesburg/305448/weather-forecast/305448')
page = requests.get("https://weather.com/en-IN/weather/tenday/l/INKA0344:1:IN")
page = requests.get("https://www.accuweather.com/en/za/johannesburg/305448/weather-forecast/305448")
about = r.html.find('#about', first=True)

print ("Hello World!")
print (r.html.search('Python is a {} language')[0])
