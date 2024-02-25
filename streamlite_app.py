import streamlit as st
import ollama
from typing import Dict, Generator
from gtts import gTTS
from io import BytesIO

def ollama_generator(model_name: str, messages: Dict) -> Generator:
    stream = ollama.chat(
        model=model_name, messages=messages, stream=True)
    for chunk in stream:
        yield chunk['message']['content']


import base64



def autoplay_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )



sound_file = BytesIO()
st.title("Ollama with Streamlit demo")
if "selected_model" not in st.session_state:
    st.session_state.selected_model = ""
if "messages" not in st.session_state:
    st.session_state.messages = []
st.session_state.selected_model = st.selectbox(
    "Please select the model:", [model["name"] for model in ollama.list()["models"]])
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if prompt := st.chat_input("How could I help you?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": "restrcit your response within more then 20 lines but it should be a exact answer this is my question :"+ " " + prompt})
    # Display user message in chat message container
        

    with st.chat_message("assistant"):
        response = st.write_stream(ollama_generator(
            st.session_state.selected_model, st.session_state.messages))
        tts = gTTS(str(response), lang='en')
        tts.write_to_fp(sound_file)
        tts.save('sample.wav')

        gif = st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")
        autoplay_audio('sample.wav')
        gif.empty()
        
        # st.audio(sound_file,autoplay=True)
    st.session_state.messages.append(
        {"role": "assistant", "content": response})
