import boto3
import streamlit as st 
import os
import uuid

s3_client=boto3.client("s3")
BUCKET_NAME= os.getenv("BUCKET_NAME")

## Bedrock
from langchain_community.embeddings import BedrockEmbeddings

## Text Splitter
from langchain.text_splitter import RecursiveCharacterTextSplitter

## Pdf Loader
from langchain_community.document_loaders import PyPDFLoader

## import FAISS
from langchain_community.vectorstores import FAISS


# def get_unique_id():
#     return str(uuid.uuid4())

# st.write("This is Admin Site for Chat with PDF demo")
def main():
    # st.write("This is Admin Site for Chat with PDF demo")
    # uploaded_file = st.file_uploader("Choose a file", "pdf")
    # if uploaded_file is not None:
    #     request_id = get_unique_id()
    #     st.write(f"Request Id: {request_id}")
    #     saved_file_name = f"{request_id}.pdf"
    #     with open(saved_file_name, mode="wb") as w:
    #         w.write(uploaded_file.getvalue())

    #     loader = PyPDFLoader(saved_file_name)
    #     pages = loader.load_and_split()

    #     st.write(f"Total Pages: {len(pages)}")

    st.write("Hello, Streamlit!")
if __name__ == "__main__ ":
    main()