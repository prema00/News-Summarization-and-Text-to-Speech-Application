import streamlit as st
import requests

st.title("📢 News Summarization & Hindi TTS")

company = st.text_input("Enter Company Name")

if st.button("Fetch News & Analyze"):
    response = requests.get(f"http://127.0.0.1:5000/news?company={company}")
    articles = response.json()
    
    st.write("### News Articles & Sentiment")
    for article in articles:
        st.write(f"**{article['title']}**")
        st.write(f"Summary: {article['summary']}")
        st.write(f"Sentiment: {article['sentiment']}")
        st.write("---")

    st.write("### Hindi Audio Summary")
    audio_response = requests.get(f"http://127.0.0.1:5000/tts?company={company}")
    st.audio(audio_response.content, format="audio/mp3")
