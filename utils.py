import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from gtts import gTTS

def fetch_news(company):
    url = f"https://newsapi.org/v2/everything?q={company}&apiKey=YOUR_API_KEY"
    response = requests.get(url).json()
    
    articles = []
    for article in response.get("articles", [])[:10]:
        articles.append({
            "title": article["title"],
            "summary": article["description"],
            "url": article["url"]
        })
    
    return articles

def analyze_sentiment(articles):
    for article in articles:
        analysis = TextBlob(article["summary"])
        polarity = analysis.sentiment.polarity
        
        if polarity > 0:
            article["sentiment"] = "Positive"
        elif polarity < 0:
            article["sentiment"] = "Negative"
        else:
            article["sentiment"] = "Neutral"
    
    return articles

def generate_tts(text, filename="output.mp3"):
    tts = gTTS(text=text, lang="hi")
    tts.save(filename)
    return filename
