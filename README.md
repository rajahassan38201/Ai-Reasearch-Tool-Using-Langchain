https://github.com/user-attachments/assets/a16feea6-b49c-4ba1-a44e-72a8844c3ffc

# Ai-Reasearch-Tool-Using-Langchain

---

# 🧠 AI Research Tool – LangChain Application

## 📘 Overview

**AI Research Tool** is a smart assistant designed to help students, researchers, and professionals extract key information and summaries from large texts. It uses the **LangChain framework** along with **LLMs (Large Language Models)** to provide relevant, clean, and short summaries to support research tasks.

---

## 🚀 Features

* Paste or upload long research content
* Extract main ideas, key points, and summaries
* Get intelligent answers to research questions
* Streamlined user interface built with Streamlit
* Supports flexible language model backends (Google GenAI or OpenAI)

---

## 🛠️ Technologies Used

* **Python 3.10+**
* **LangChain**
* **Google Generative AI / OpenAI**
* **Streamlit**
* **Text Splitters and Embeddings**
* **FAISS / Chroma (Vector Database)**

---

## 📁 Project Structure

```
ai-research-tool/
│
├── app.py                   # Streamlit interface
├── requirements.txt         # Project dependencies
├── .env                     # API Keys
└── README.md                # Project documentation
```

---

## ⚙️ Installation

1. **Clone the Repository**

```bash
git clone https://github.com/rajahassan38201/Ai-Reasearch-Tool-Using-Langchain.git
cd Ai-Reasearch-Tool-Using-Langchain
```

2. **Create Virtual Environment (Optional)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Set Up Environment Variables**
   Create a `.env` file and add:

```
GOOGLE_API_KEY=your_google_genai_key_here
```

---

## ▶️ Usage

1. Start the Streamlit app:

```bash
streamlit run app.py
```

2. Enter or paste research content
3. Ask questions or request a summary
4. View generated summaries or responses instantly

---

## 🔍 How It Works

* Text is split into smaller parts using LangChain tools
* Embeddings are generated for better retrieval
* A question or summary prompt is sent to the LLM
* The AI gives accurate, clear answers or summaries using RAG

---

## 📌 Use Cases

* Academic research assistance
* Paper and article summarization
* Technical content simplification
* Review of large scientific or policy documents

---

## 🤝 Contributing

Feel free to open issues, suggest features, or create pull requests to improve the tool.

---
