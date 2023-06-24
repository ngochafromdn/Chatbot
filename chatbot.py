import streamlit as st
from streamlit_chat import message
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from Modules.data_extraction import DataExtraction
from Modules.chain import Chain
from Modules.prompt import prompt
import os


user_api_key = st.sidebar.text_input('API key',label="#### Enter your OPEN AI API here 👇",placeholder="Enter your OPEN AI API here ")
input_link = st.sidebar.text_input(
    label="#### Your input link 👇",
    placeholder="Paste your input link")

if input_link and user_api_key:
    os.environ["OPENAI_API_KEY"] = user_api_key
    docs = DataExtraction.convert_to_docs(input_link)
    # Create the conversational retrieval chain
    chain = Chain.create_chain(user_api_key, docs, prompt.generate_qa_prompt())

    def conversational_chat(query):
        result = chain({"question": query, "chat_history": st.session_state['history']})
        st.session_state['history'].append((query, result["answer"]))
        return result["answer"]
    
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Hello ! Ask me anything about " + input_link + " 🍉"]

    if 'past' not in st.session_state:
        st.session_state['past'] = ["I am user ! 🌼"]
        
    #container for the chat history
    response_container = st.container()
    #container for the user's text input
    container = st.container()

    with container:
        with st.form(key='my_form', clear_on_submit=True):
            
            user_input = st.text_input("Enter your question:", placeholder="Talk about your link information here (:", key='input')
            submit_button = st.form_submit_button(label='Send')
            
        if submit_button and user_input:
            output = conversational_chat(user_input)
            
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)

    if st.session_state['generated']:
        with response_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="big-smile")
                message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs")
                
