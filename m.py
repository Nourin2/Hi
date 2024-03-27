import streamlit as st 
from openai import OpenAI 

st.title('ChatGpt-like clone')

client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

if "openai_model" not in st.session_state:
    st.session_state['openai_model']= 'gpt-3.5-turbo'
if 'messages' not in st.session_state:
    st.session_state = []

for message in st.session_state:
    with st.chat_message('role'):
        st.markdown(message['content'])

if prompt := st.chat_input('Whats up?'):
    st.session_state.message.append({'role': 'user', 'content': prompt})
    with st.chat_message('user'):
        st.markdown(prompt)
    