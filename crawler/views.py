from django.shortcuts import render
from crawler.models import Headline 
import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup    

# Create your views here.

def scrape(request):
  Headline.objects.all().delete()
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url = "https://www.theonion.com/latest"
  content = session.get(url).content
  soup = BSoup(content, "html.parser")
  News = soup.find_all('div', {"class":"cw4lnv-11 dFCKPx"})
