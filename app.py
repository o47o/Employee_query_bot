# python -m streamlit run C:\employee_query_bot\app.py

import streamlit as st
import os
from loader import load_documents_from_folder, create_vector_store
from query_bot import get_conversational_chain
from dotenv import load_dotenv

from openai import OpenAI
from openai import api_key
import openai
from langchain.callbacks import get_openai_callback

load_dotenv()

st.set_page_config(page_title="💬 HR FAQ Chatbot", layout="centered")

st.title("🤖 HR FAQ Chatbot")

with st.sidebar:
    st.title("⚙️ Settings")

    if st.button("🔄 Reset Chat"):
        st.session_state.chat_history = []
        st.session_state.qa_chain = None
        st.rerun()


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

# Load documents only once
if st.session_state.qa_chain is None:
    with st.spinner("Loading and embedding documents..."):
        folder_path = r"C:\employee_query_bot\data"
        docs = load_documents_from_folder(folder_path)
        if not docs:
            st.error("No valid documents found in 'documents/' folder.")
        else:
            vectorstore = create_vector_store(docs)
            st.session_state.qa_chain = get_conversational_chain(vectorstore)
            st.success("✅ Documents loaded!")

# uploaded_file = st.file_uploader("Upload HR Policy Document (.pdf or .txt)", type=["pdf", "txt"])

# if uploaded_file and not st.session_state.qa_chain:
#     with st.spinner("Processing document..."):
#         file_path = os.path.join("data", uploaded_file.name)
#         with open(file_path, "wb") as f:
#             f.write(uploaded_file.read())

#         docs = load_documents(file_path)
#         vectorstore = create_vector_store(docs)
#         st.session_state.qa_chain = get_conversational_chain(vectorstore)

#     st.success("✅ Document processed! Start chatting below.")

if st.session_state.qa_chain:
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input("Ask your HR question here...")

    if user_input:
        st.chat_message("user").markdown(user_input)
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        with st.spinner("Thinking..."):
            with get_openai_callback() as cb:
                result = st.session_state.qa_chain.invoke({
                    "question": user_input,
                    "chat_history": [(m["content"], "") for m in st.session_state.chat_history if m["role"] == "user"]
                })

                response = result["answer"]
                token_info = {
                    "total_tokens": cb.total_tokens,
                    "prompt_tokens": cb.prompt_tokens,
                    "completion_tokens": cb.completion_tokens,
                    "cost": cb.total_cost
                }


        st.chat_message("assistant").markdown(response)
        st.session_state.chat_history.append({"role": "assistant", "content": response})

        with st.expander("📊 Token Usage"):
            st.markdown(f"- **Prompt tokens**: {token_info['prompt_tokens']}")
            st.markdown(f"- **Completion tokens**: {token_info['completion_tokens']}")
            st.markdown(f"- **Total tokens**: {token_info['total_tokens']}")
            st.markdown(f"- **Estimated cost**: ${token_info['cost']:.5f}")