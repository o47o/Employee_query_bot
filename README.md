# 🤖 Employee Query Bot

> **An intelligent, user-friendly HR FAQ chatbot for querying company policies and documents, powered by OpenAI and Streamlit.**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0-red.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT-4-green.svg)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-orange.svg)

## ✨ Features

### 📋 **Core Capabilities**
- **Interactive Chat**: Real-time conversation about HR policies.
- **FAQ Assistant**: Answers based on company documents.
- **Modern UI**: Responsive design with Streamlit.
- **Secure Credentials**: API keys managed with `.env`.
- **Efficient Retrieval**: Uses FAISS for fast document search.

## 📋 Prerequisites

### **Required Software**
1. **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
2. **OpenAI API Key** - [Get API Key](https://platform.openai.com/api-keys)

## 🚀 Quick Start

### **1. Clone or Download**
```bash
git clone <your-repo-url>
cd employee_query_bot
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Environment Setup**
Create a `.env` file in the project root with your OpenAI API key:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### **4. Run the Application**
```bash
streamlit run app.py
```

## 🎯 How to Use

### **Getting Started**
Open your browser to `http://localhost:8501`:
1. Verify the connection and load documents.
2. Start asking questions about your HR policies!

### **Example Interactions**
- **Explore Policies**: "What is the leave policy?"
- **Understand Benefits**: "Tell me about the referral policy."

### **Document Upload**
Add HR documents (`.pdf` or `.txt`) to the `data/` folder for more robust answers.

## 📁 Project Structure

```
employee_query_bot/
├── app.py                      # Main Streamlit interface
├── query_bot.py                # Query handler using LangChain
├── loader.py                   # Document loading and vector storage
├── requirments.txt             # Python dependencies
├── .env                        # Environment variables (place your API key here)
├── data/                       # HR documents (PDF/TXT)
└── __pycache__/                # Compiled Python files
```

## 🔒 Security Features
- **Environment Variables**: API keys managed in `.env`
- **No Hardcoded Credentials**: All sensitive data externalized

## 🛠️ Troubleshooting
### **Common Issues**
- Ensure the `.env` file is correctly formatted.
- Check document formats in the `data/` directory.

## 🎨 Future Enhancements
- **ChatGPT Integration**: For more conversational interactions.
- **Multi-Document Support**: Enhanced document analysis.

## 📫 Support
If you encounter any issues, please create an issue on GitHub.
