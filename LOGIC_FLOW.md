# 🔄 Employee Query Bot - Logic Flow Diagram

## 📊 High-Level Architecture Flow

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   User Input    │───▶│  Streamlit UI    │───▶│  Session State  │
│   (Question)    │    │     (app.py)     │    │   Management    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │                        │
                                ▼                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Document      │◄───│  Document Loader │    │  Vector Store   │
│   Processing    │    │   (loader.py)    │    │     (FAISS)     │
│   (PDF/TXT)     │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │                        │
                                ▼                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   OpenAI API    │◄───│   Query Bot      │◄───│   Retriever     │
│   (LLM Chain)   │    │ (query_bot.py)   │    │   (Similarity   │
│                 │    │                  │    │     Search)     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                                ▼
                        ┌──────────────────┐
                        │   AI Response    │
                        │   + Token Info   │
                        │                  │
                        └──────────────────┘
```

## 🚀 Detailed Application Flow

### **1. Application Initialization**
```
START
  │
  ├─ Load Environment Variables (.env)
  │   └─ OPENAI_API_KEY
  │
  ├─ Initialize Streamlit Page Config
  │   ├─ Title: "💬 HR FAQ Chatbot"
  │   └─ Layout: "centered"
  │
  ├─ Initialize Session State
  │   ├─ chat_history = []
  │   └─ qa_chain = None
  │
  └─ Check if qa_chain exists
      ├─ NO: Go to Document Loading
      └─ YES: Go to Chat Interface
```

### **2. Document Loading & Processing**
```
DOCUMENT LOADING
  │
  ├─ Scan data/ folder
  │   ├─ Find PDF files
  │   └─ Find TXT files
  │
  ├─ For each document:
  │   ├─ Load document content
  │   │   ├─ PDF: PyPDFLoader
  │   │   └─ TXT: TextLoader
  │   │
  │   ├─ Split into chunks
  │   │   ├─ chunk_size: 1000
  │   │   └─ chunk_overlap: 100
  │   │
  │   └─ Add to docs list
  │
  ├─ Create embeddings (OpenAI)
  │
  ├─ Build FAISS vector store
  │
  ├─ Create conversational chain
  │   ├─ LLM: ChatOpenAI (temperature=0)
  │   ├─ Retriever: vectorstore.as_retriever()
  │   └─ Prompt: HR Assistant template
  │
  └─ Store qa_chain in session_state
```

### **3. Chat Interface Flow**
```
CHAT INTERFACE
  │
  ├─ Display Chat History
  │   └─ Show previous messages
  │
  ├─ Wait for User Input
  │   └─ chat_input: "Ask your HR question here..."
  │
  ├─ User submits question
  │   │
  │   ├─ Add user message to chat_history
  │   │
  │   ├─ Process with QA Chain
  │   │   ├─ Input: user question + chat history
  │   │   ├─ Retrieve relevant documents
  │   │   ├─ Generate context from documents
  │   │   ├─ Send to OpenAI with prompt
  │   │   └─ Get AI response
  │   │
  │   ├─ Track token usage
  │   │   ├─ Prompt tokens
  │   │   ├─ Completion tokens
  │   │   ├─ Total tokens
  │   │   └─ Estimated cost
  │   │
  │   ├─ Display AI response
  │   │
  │   ├─ Add response to chat_history
  │   │
  │   └─ Show token usage statistics
  │
  └─ Loop back to wait for next input
```

## 🔧 Component Breakdown

### **app.py (Main Interface)**
```
┌─────────────────────────────────┐
│           app.py                │
├─────────────────────────────────┤
│ • Streamlit UI setup            │
│ • Session state management      │
│ • Chat interface rendering      │
│ • Token usage tracking          │
│ • Reset functionality           │
└─────────────────────────────────┘
```

### **loader.py (Document Processing)**
```
┌─────────────────────────────────┐
│          loader.py              │
├─────────────────────────────────┤
│ • load_documents_from_folder()  │
│   ├─ PDF processing             │
│   ├─ TXT processing             │
│   └─ Document chunking          │
│                                 │
│ • create_vector_store()         │
│   ├─ OpenAI embeddings          │
│   └─ FAISS vector database      │
└─────────────────────────────────┘
```

### **query_bot.py (AI Chain)**
```
┌─────────────────────────────────┐
│         query_bot.py            │
├─────────────────────────────────┤
│ • get_conversational_chain()    │
│   ├─ ChatOpenAI LLM             │
│   ├─ Custom HR prompt template  │
│   ├─ ConversationalRetrieval    │
│   └─ Source document return     │
└─────────────────────────────────┘
```

## 📝 Data Flow Sequence

### **Step-by-Step Processing**
1. **User Question** → Streamlit Chat Input
2. **Question Processing** → Add to chat history
3. **Document Retrieval** → FAISS similarity search
4. **Context Building** → Relevant document chunks
5. **LLM Processing** → OpenAI API call with context
6. **Response Generation** → AI answer based on documents
7. **Token Tracking** → Usage statistics calculation
8. **Display Results** → Show answer + token info
9. **State Update** → Add to conversation history

## 🎯 Key Decision Points

### **Document Loading Logic**
```
IF qa_chain is None:
    ├─ Load documents from data/ folder
    ├─ Create vector embeddings
    ├─ Initialize conversational chain
    └─ Display "Documents loaded!"
ELSE:
    └─ Proceed to chat interface
```

### **Question Processing Logic**
```
IF user submits question:
    ├─ Add question to chat history
    ├─ Invoke QA chain with:
    │   ├─ Current question
    │   └─ Previous chat history
    ├─ Get response + token usage
    ├─ Display response
    └─ Update chat history
ELSE:
    └─ Wait for user input
```

### **Error Handling**
```
TRY:
    ├─ Load each document
    ├─ Process embeddings
    └─ Generate response
CATCH:
    ├─ Log error message
    ├─ Continue with other documents
    └─ Display user-friendly error
```

## 📊 Performance Considerations

### **Optimization Points**
- **One-time Loading**: Documents loaded only once per session
- **Session Persistence**: Vector store cached in session state
- **Chunked Processing**: Large documents split for better retrieval
- **Efficient Search**: FAISS for fast similarity matching
- **Token Tracking**: Real-time cost monitoring

### **Memory Management**
- Documents processed in chunks
- Vector store stored in session state
- Chat history maintained in memory
- Automatic cleanup on reset

---

## 🔄 Reset Flow
```
User clicks "🔄 Reset Chat"
  │
  ├─ Clear chat_history = []
  ├─ Set qa_chain = None
  ├─ Trigger app rerun
  └─ Return to document loading phase
```

This flow diagram shows how your Employee Query Bot processes documents, manages conversations, and provides intelligent responses based on your HR policy documents!
