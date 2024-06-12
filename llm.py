import streamlit as st
from langchain_openai import ChatOpenAI

# https://graphacademy.neo4j.com/courses/llm-chatbot-python/2-configuration/1-llm/

#part 1
llm = ChatOpenAI(
    openai_api_key=st.secrets["OPENAI_API_KEY"],
    model=st.secrets["OPENAI_MODEL"],
)


#part 2
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    openai_api_key=st.secrets["OPENAI_API_KEY"]
)