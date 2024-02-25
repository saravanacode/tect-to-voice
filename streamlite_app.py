import streamlit as st
import openai
from gtts import gTTS
from io import BytesIO

def generate(prompt):
    openai.api_key = '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'

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    result = response.choices[0].message['content']
    
    # Create a BytesIO object to store the audio data
    sound_file = BytesIO()
    
    # Generate speech using gTTS and write it to the BytesIO object
    tts = gTTS(text=result, lang='en')
    tts.write_to_fp(sound_file)
    
    # Reset the BytesIO object to the beginning
    sound_file.seek(0)
    
    # Display the audio using st.audio
    st.audio(sound_file, format='audio/mp3')  # Specify the format as mp3
    
    return result

def clear():
    st.empty()

st.title("ChatBot")

st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")

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
