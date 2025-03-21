import streamlit as st

st.title('Hello World')
st.write('This is a simple Streamlit app.')

if st.button('say hello'):
	st.text('hello,Streamlit!')
	
name = st.text_input('Please enter your name:')
if name:
   st.write(f'Hello, {name}!')


st.file_uploader('Please upload a file:', type=['txt', 'csv'])
	
