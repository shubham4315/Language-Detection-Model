import pickle
import string
import streamlit as st
import webbrowser

global Lrdetect_Model

LrdetectFile = open('language_detection_model.pckl','rb')
Lrdetect_Model = pickle.load(LrdetectFile)
LrdetectFile.close()
st.title("Language Detetction Tool")
input_test = st.text_input("Provide your text input here" , 'Hello My name is Shubham')

button_clicked = st.button("Predict Language Name")
if button_clicked:
    st.text(Lrdetect_Model.predict([input_test]))