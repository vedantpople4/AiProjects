import streamlit as st
import requests
from bs4 import BeautifulSoup
from transformers import BartForConditionalGeneration, BartTokenizer

st.title("Article Summarization Application")

urls_input = st.text_area("Enter the URLs of news articles (one per line):")

if st.button("Fetch and Summarize Articles"):

    urls = urls_input.split('\n')

    def fetch_article_content(url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            article_text = ' '.join([para.text for para in paragraphs])
            return article_text
        except Exception as e:
            return f"Error fetching article from {url}: {str(e)}"

    articles_content = [fetch_article_content(url.strip()) for url in urls]

    summarization_model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
    summarization_tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")

    def summarize_text(text):
        inputs = summarization_tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = summarization_model.generate(inputs, max_length=512, min_length=80, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = summarization_tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary

    for i, content in enumerate(articles_content):
        summarized_text = summarize_text(content)
        st.subheader(f"Summary of Article {i + 1}")
        st.write(summarized_text)
