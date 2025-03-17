from flask import Flask, request, jsonify
from utils import fetch_news, analyze_sentiment, generate_tts

app = Flask(__name__)

@app.route("/news", methods=["GET"])
def get_news():
    company = request.args.get("company")
    articles = fetch_news(company)
    analyzed_articles = analyze_sentiment(articles)
    return jsonify(analyzed_articles)

@app.route("/tts", methods=["GET"])
def get_tts():
    company = request.args.get("company")
    articles = fetch_news(company)
    summary_text = " ".join([article["summary"] for article in articles])
    
    filename = generate_tts(summary_text)
    return open(filename, "rb").read()

if __name__ == "__main__":
    app.run(debug=True)
