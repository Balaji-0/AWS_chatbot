import boto3
import streamlit as st 
import os
import uuid

s3_client=boto3.client("s3")
BUCKET_NAME= os.getenv("BUCKET_NAME")

##bedrock

from langchain.embeddings import BedrockEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader


def main():
    st.write("This is Admin Site for Chat with PDF demo")
    uploaded_file = st.file_uploader("Choose a file", "pdf")
    if uploaded_file is not None:
        request_id = uuid()
        st.write(f"Request Id: {request_id}")
        saved_file_name = f"{request_id}.pdf"
        with open(saved_file_name, mode="wb") as w:
            w.write(uploaded_file.getvalue())

        loader = PyPDFLoader(saved_file_name)
        pages = loader.load_and_split()

        st.write(f"Total Pages: {len(pages)}")
if __name__ == "__main__ ":
    main()