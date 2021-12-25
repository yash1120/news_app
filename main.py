from flask import Flask , render_template , redirect 
from dotenv import load_dotenv
import flask
import requests 
import os

import application.config
load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")

TOP_HEADLINES = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"
EVERYTHING    = "https://newsapi.org/v2/everything&apiKey={API_KEY}"

# news = requests.get(TOP_HEADLINES).json()
# articles = news['articles']
# for article in articles :
#     print(article['title'])

app = Flask(__name__)

CATEGORIES = ('general', 'sports', 'business', 'entertainment', 'health',
              'science', 'technology')
@app.route("/")
def root():
    news = requests.get(TOP_HEADLINES).json()
    articles = news['articles']
    return render_template("index.html",articles=articles)

@app.route("/category/<string:category>")
def category(category):
    news = requests.get(TOP_HEADLINES)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True
    )