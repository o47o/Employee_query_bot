from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

def get_conversational_chain(vectorstore):
    llm = ChatOpenAI(temperature=0)

    prompt = PromptTemplate.from_template("""
You are an HR assistant for a company. Answer the employee's questions **only** using the information provided in the document.
If you don't know the answer based on the document, respond with:
"I’m sorry, I couldn’t find that information in the document."

Question: {question}
=========
{context}
=========
Helpful Answer:
""")

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm,
        retriever=vectorstore.as_retriever(),
        return_source_documents=True,  # Useful for debugging
        combine_docs_chain_kwargs={"prompt": prompt}
    )

    # return qa_chain
    return ConversationalRetrievalChain.from_llm(
        llm,
        retriever=vectorstore.as_retriever(),
        return_source_documents=True,
        combine_docs_chain_kwargs={"prompt": prompt}
    )
