# 📰 News Summarization & Hindi Text-to-Speech Application

## 📌 Overview  
This project extracts the latest news articles related to a given company, performs sentiment analysis, and converts the summarized content into Hindi speech using text-to-speech (TTS).

## 🚀 Features  
✅ **News Extraction** – Fetches at least 10 unique articles related to the given company.  
✅ **Sentiment Analysis** – Categorizes each article as Positive, Negative, or Neutral.  
✅ **Comparative Analysis** – Provides insights on how news coverage varies.  
✅ **Hindi Text-to-Speech (TTS)** – Converts the sentiment summary into Hindi audio.  
✅ **User-Friendly Interface** – Uses Streamlit for a simple and interactive UI.  
✅ **REST API Integration** – Uses Flask to fetch news, analyze sentiment, and generate TTS.  
✅ **Deployment on Hugging Face Spaces** – The application is hosted for easy access.  

## 🛠️ Installation & Setup  
```bash
git clone <your-repo-link>
cd <your-repo-folder>
pip install -r requirements.txt
python api.py  # Start API server
streamlit run app.py  # Start Web UI
```
## 🌐 API Endpoints  
| Endpoint | Method | Description | Example |
|----------|--------|------------|---------|
| `/news`  | `GET`  | Fetches news articles for a company | `/news?company=Tesla` |
| `/tts`   | `GET`  | Generates Hindi TTS audio for the company's news summary | `/tts?company=Tesla` |
