import streamlit as st
from utils import write_message

#Mitch
from agent import generate_response

# tag::setup[]
# Page Config
st.set_page_config("Mitch - RAG - LLM", page_icon=":blue_heart:")
st.title("ChatGPT-via RAG - langchain")
st.caption('Made by Mitch in Melbourne 	:blue_heart:')
with st.container():
   st.write("This chatbot is connecting to OPEN AI Chat GPT through API...")
   st.write("This bad boy also calls neo4j thrugh GraphCypherQAChain, but I haven't done that yet.")

# end::setup[]

# tag::session[]
# Set up Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi, I'm EBERT the GraphAcademy Chatbot! How can I help you? Fun fact!  I repeat your questions after I answer them.. who knows why!?"},
    ]
# end::session[]

# tag::submit[]
# Submit handler
def handle_submit(message):
    """
    Submit handler:

    You will modify this method to talk with an LLM and provide
    context using data from Neo4j.
    """

    # Handle the response
    with st.spinner('Thinking...'):
        response = generate_response(message)
        write_message('assistant', response)
        from time import sleep
        sleep(1)
        write_message('assistant', message)
# end::submit[]


# tag::chat[]
# Display messages in Session State
for message in st.session_state.messages:
    write_message(message['role'], message['content'], save=False)

# Handle any user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    write_message('user', prompt)

    # Generate a response
    handle_submit(prompt)
# end::chat[]
