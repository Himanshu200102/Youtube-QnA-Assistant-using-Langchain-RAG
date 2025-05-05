# 🎥 YouTube Video Q&A Assistant

This project allows users to ask natural language questions about any YouTube video. It uses Retrieval-Augmented Generation (RAG) to process the video transcript, find relevant segments, and generate grounded answers using the LLaMA 2 model via Ollama.

---

## 🚀 Features

- 🔗 Paste a YouTube video URL
- 🧠 Transcribes and chunks video content
- 🔍 Uses sentence-transformers + FAISS for semantic retrieval
- 🗣️ LLaMA 2 (via Ollama) answers using only relevant video parts
- 💡 Interactive, stylish interface via Streamlit

---

## 🛠️ How It Works

1. Loads the transcript using YoutubeLoader from LangChain.
2. Splits it into chunks using RecursiveCharacterTextSplitter.
3. Embeds the chunks using sentence-transformers/all-MiniLM-L6-v2.
4. Stores them in a FAISS vector store.
5. Accepts user question and retrieves top-k relevant chunks.
6. Passes them into a custom prompt to llama2 via Ollama.
7. Displays a factual, grounded answer.

---

## 📦 Installation Instructions

### 1. Clone the repository
git clone https://github.com/your-username/youtube-qa-assistant.git
cd youtube-qa-assistant

### ⚙️ Step 2: Install dependencies
Ensure Python 3.8 or later is installed, then run:
pip install -r requirements.txt

### 🧠 Step 3: Set up Ollama + LLaMA 2
If Ollama isn't already installed:
Download from: https://ollama.com
Then in terminal: ollama run llama2

### 💻 Step 4: Launch the Streamlit app
streamlit run main.py
This will open a browser window where you can paste a YouTube link and ask questions.

---

## 🧩 Tech Stack

| Component             | Purpose                               |
|-----------------------|---------------------------------------|
| LangChain             | Prompt and chain orchestration        |
| FAISS                 | Efficient similarity search           |
| sentence-transformers | Generates semantic embeddings         |
| Ollama + LLaMA 2      | Local LLM response generation         |
| Streamlit             | Web interface                         |
| YouTubeLoader         | Transcript extraction from YouTube    |

Enjoy building with local LLMs! 🧠💬
