import streamlit as st
import openai
from gtts import gTTS
import os

def generate(prompt):
    openai.api_key = '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'

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    result = response.choices[0].message['content']
    tts = gTTS(text=result, lang='en')
    tts.save("output.mp3")
    os.system("start output.mp3")  # This will play the audio file
    return result

def clear():
    st.empty()

st.title("ChatBot")

prompt = st.text_input("Enter your question:")
st.write("")  # Adding some space between input and buttons

# Centering the buttons along the x-axis
col1, col2, col3 = st.columns([4, 4, 1])
with col2:
    if st.button("Generate"):
        result = generate(prompt)
        st.write(result)

with col2:
    if st.button("Clear"):
        clear()
