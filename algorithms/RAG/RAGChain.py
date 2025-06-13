import os
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

class RAGChain:
    def __init__(self, model_name, persist_directory="chroma_db"):
        # Env vars for tracing
        os.environ['LANGCHAIN_TRACING_V2'] = 'true'
        os.environ['LANGSMITH_ENDPOINT'] = "https://api.smith.langchain.com"
        os.environ['LANGSMITH_TRACING'] = 'true'
        os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
        os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY_FOR_LANGCHAIN')

        self.persist_directory = persist_directory
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)
        self.vectorstore = None

    def split_texts(self, texts, chunk_size=1000, chunk_overlap=200):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        return splitter.create_documents(texts)

    def create_vectorstore(self, texts, metadatas=None):
        """
        Creates a new Chroma vectorstore from given texts + optional metadata.
        """
        self.vectorstore = Chroma.from_texts(
            texts=texts,
            embedding=self.embeddings,
            metadatas=metadatas,
            persist_directory=self.persist_directory
        )
        return self.vectorstore

    def load_vectorstore(self):
        """
        Loads an existing vectorstore from disk.
        """
        self.vectorstore = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embeddings
        )
        return self.vectorstore

    def add_texts(self, texts, metadatas=None):
        """
        Adds new texts with optional metadata.
        """
        if self.vectorstore is None:
            raise ValueError("Vectorstore not initialized. Call create_vectorstore() or load_vectorstore() first.")
        self.vectorstore.add_texts(texts, metadatas=metadatas)
        self.vectorstore.persist()

    def similarity_search(self, query, k=3):
        """
        Returns a list of Documents with .page_content and .metadata
        """
        if self.vectorstore is None:
            raise ValueError("Vectorstore not initialized.")
        return self.vectorstore.similarity_search(query, k=k)

    def save(self):
        """
        Explicitly persist the current vectorstore to disk.
        """
        if self.vectorstore is not None:
            self.vectorstore.persist()
    def similarity_search_with_score(self, text, k=4):
        return self.vectorstore.similarity_search_with_score(text, k=k)
