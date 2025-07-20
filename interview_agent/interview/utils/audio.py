import pyttsx3
import speech_recognition as sr
import streamlit as st

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.save_to_file(text, "response.mp3")
    engine.runAndWait()
    with open("response.mp3", "rb") as audio_file:
        st.audio(audio_file.read(), format="audio/mp3")

def listen_live():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙 Listening... Please speak now.")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        return f"Speech Recognition error: {e}"
