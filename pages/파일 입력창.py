import streamlit as st
import random

st.title("여러 가지 입력창")

st.button("Reset", type="secondary")
if st.button('랜덤숫자생성'):
    st.write(random.random())


text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)

st.link_button("Go to gallery", "https://streamlit.io/gallery")

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')
else:
    st.write('동의 버튼을 먼저 클릭해주세요. ')

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'])

st.write('You selected:', options)

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ':rainbow[Comedy]':
    st.write('You selected comedy.')
else:
    st.write("You selected ", genre)

number = st.number_input('숫자를 입력해주세요.', step=1)
st.write("The current number is ", number)

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

import pandas as pd #csv파일을 불러오기 위함

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name, encoding ='euc-kr')
    st.write(bytes_data)