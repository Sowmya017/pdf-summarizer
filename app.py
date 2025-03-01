from flask import Flask 
import streamlit as st
import os

app=Flask(__name__)

def main():
    st.set_page_config(page_title="PDF Summarizer") #head title
    st.title("PDF Summarizer App") #heading of the page

    st.write("Summarize your pdf files un just few seconds!!")#desc of the page
    st.divider() #adds a horizontal line


    #cretes a file uploader widget to uplod the pdfs
    st.file_uploader('Upload your PDF documen',type='pdf')

    submit=st.submit('Generate Summary')
if __name__ == '__main__':
    app.run(debug=True)

