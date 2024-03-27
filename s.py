import streamlit as st 
from openai import OpenAI 

st.title('ChatGpt-like clone')

client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

if "openai_model" not in st.session_state:
    st.session_state['openai_model']='gpt-3.5-turbo'
    
if 'messages' not in st.session_state:
    st.session_state = []
    
for message in st.session_state:
    with st.chat_message('role'):
        st.markdown(message['content'])
        
if prompt := st.chat_input('Whats up?'):
    st.session_state.message.append({'role': 'user', 'content': prompt})
    with st.chat_message('user'):
        st.markdown(prompt)
        
    with st.chat_message('assistant'):
        stream = client.chat.completions.create(
           model=st.session_state['openai_model'],
           messages=[
               {'role': m['role'], 'content': m['content']}
               for m in st.session_state.messsages
           ],
           stream=True
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({'role': 'assistant', 'content': response})
    
    
    #for i in range(len(fruits)):  # Generates integer indices
    #print(fruits[i])
        
     