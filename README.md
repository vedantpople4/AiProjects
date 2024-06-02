# Article Summarization Application

Welcome to the Article Summarization Application repository! This project is an AI-powered application designed to fetch and summarize news articles. Leveraging advanced natural language processing techniques, this application condenses lengthy articles into concise summaries, facilitating quick understanding of key points.

## 🌟 Key Features:
- **Seamless URL Input**: Easily input URLs of news articles and receive instant summaries.
- **Cutting-edge Summarization Model**: Utilizes the `facebook/bart-large-cnn` model for high-quality text summarization.
- **Intuitive Interface**: Built with Streamlit for a user-friendly and interactive experience.

## 🛠️ Tech Stack:
- **Streamlit**: Crafting a responsive and interactive web application.
- **Requests & BeautifulSoup**: Fetching and parsing news article content from URLs.
- **Hugging Face Transformers**: Leveraging the `facebook/bart-large-cnn` model for article summarization.
- **PyTorch**: Serving as the backend framework for the transformer models.

## 🔧 How to Get Started:
1. **Clone the Repository**: https://github.com/vedantpople4/AiProjects
2. **Install Dependencies**:
   ```sh
   pip install streamlit requests beautifulsoup4 transformers torch
   ```
3. **Run the Application**:
   ```sh
   streamlit run streamlit_app.py
   ```

## 💻 How It Works:
1. **User Input**: Input the URLs of the news articles you wish to summarize.
2. **Fetch and Process**: The app retrieves and preprocesses the content from the provided URLs.
3. **Summarization**: Utilizes the BART model to generate concise summaries of the articles.
4. **Results Display**: Summarized text is showcased on the Streamlit interface for easy consumption.

This application epitomizes how AI can streamline information consumption by distilling lengthy articles into digestible summaries. It's ideal for individuals seeking to stay informed without dedicating excessive time to reading full articles.

## 🤝 Get Involved:
Feel free to contribute to the project, propose enhancements, or fork it to create your own versions. 
