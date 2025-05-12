import os
import bs4
import re
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer


class RAGChain:
    def __init__(self):
        os.environ['LANGCHAIN_TRACING_V2'] = 'true'
        os.environ['LANGSMITH_ENDPOINT'] = "https://api.smith.langchain.com"
        os.environ['LANGSMITH_TRACING'] = 'true'
        os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
        os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY_FOR_LANGCHAIN')
        
        self.docs = None
        self.splits = None
        self.vectorstore = None
        self.embeddings = None

    def load_docs(self, urls):
        loader = WebBaseLoader(
            web_paths=(urls)
            # bs_kwargs=dict(
            #     parse_only=bs4.SoupStrainer(
            #         class_=("post-content", "post-title", "post-header")
            #     )
            # ),
            )
        self.docs = loader.load()
        return self.docs

    def split_docs(self, docs):
        text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=1000,
            chunk_overlap=200)
        self.splits = text_splitter.split_documents(docs)
        return self.splits
    
    def embed_docs(self, docs, model_name):
        hf = HuggingFaceEmbeddings(
            model_name = model_name
        )
        texts = [doc.page_content for doc in docs]
        embeddings = hf.embed_documents(texts)
        self.embeddings = embeddings

        #return self.embeddings
        self.vectorstore = Chroma.from_documents(documents=docs,
                                                embedding=hf)
        return self.vectorstore
