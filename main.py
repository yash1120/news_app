from flask import Flask , render_template , redirect 
from dotenv import load_dotenv
import requests 
import os

import application.config
load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")

TOP_HEADLINES = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"
EVERYTHING    = "https://newsapi.org/v2/everything"

news = requests.get(TOP_HEADLINES).json()
articles = news['articles']
for article in articles :
    print(article['title'])