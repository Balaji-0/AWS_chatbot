# PDF Reader Admin Site

## Overview

The PDF Reader Admin Site is a Streamlit application that allows users to upload PDF files and interact with their content. It integrates with AWS services and leverages the LangChain library for embedding and processing documents.

## Features

- **File Upload**: Users can upload PDF files for processing.
- **PDF Parsing**: The application uses the `PyPDFLoader` to read and split PDF files into manageable parts.
- **Embedding with Bedrock**: Utilizes AWS Bedrock for document embeddings, allowing for advanced interactions with the text.
- **Vector Store**: Implements FAISS for efficient similarity search among embeddings.

## Prerequisites

- Python 3.11
- Docker (for containerized deployment)
- AWS account with necessary permissions and access keys
- Required Python packages listed in `requirements.txt`

## Installation

### Clone the Repository

```bash
git clone https://github.com/Balaji-0/AWS_chatbot.git
cd your-repo-directory
