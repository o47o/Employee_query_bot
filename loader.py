# loader.py
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
import os


def load_documents_from_folder(folder_path):
    docs = []
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        ext = os.path.splitext(filename)[1].lower()

        try:
            if ext == ".pdf":
                loader = PyPDFLoader(full_path)
            elif ext == ".txt":
                loader = TextLoader(full_path, encoding="utf-8")
            else:
                continue

            raw_docs = loader.load()
            splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
            split_docs = splitter.split_documents(raw_docs)
            # docs.extend(splitter.split_documents(raw_docs))

            if not split_docs:
                print(f"⚠️ No chunks created from: {filename}")
            else:
                print(f"✅ Loaded {len(split_docs)} chunks from: {filename}")

            docs.extend(split_docs)

        except Exception as e:
            print(f"⚠️ Error loading {filename}: {e}")
            continue

    return docs

def create_vector_store(docs):
    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(docs, embeddings)
