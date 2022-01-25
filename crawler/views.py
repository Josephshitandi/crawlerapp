from django.shortcuts import render
from crawler.models import Headline 
import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup    

# Create your views here.
