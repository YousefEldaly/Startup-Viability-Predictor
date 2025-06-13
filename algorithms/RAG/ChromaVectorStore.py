# algorithms/RAG/ChromaVectorStore.py

from langchain_community.vectorstores import Chroma
from .VectorStoreBase import VectorStoreBase

from langchain_chroma import Chroma

class ChromaVectorStore(VectorStoreBase):
    def __init__(self, embeddings, persist_directory="chroma_db"):
        self.embeddings = embeddings
        self.persist_directory = persist_directory
        self.store = None

    def create(self, texts, metadatas=None):
        self.store = Chroma.from_texts(
            texts=texts,
            embedding=self.embeddings,
            metadatas=metadatas,
            persist_directory=self.persist_directory
        )

    def add_texts(self, texts, metadatas=None):
        if self.store is None:
            self.store = Chroma(
                persist_directory=self.persist_directory,
                embedding_function=self.embeddings
            )
        self.store.add_texts(texts, metadatas=metadatas)

    def similarity_search(self, query, k=3):
        if self.store is None:
            self.store = Chroma(
                persist_directory=self.persist_directory,
                embedding_function=self.embeddings
            )
        return self.store.similarity_search(query, k=k)

    def similarity_search_with_score(self, query, k=3):
        if self.store is None:
            self.store = Chroma(
                persist_directory=self.persist_directory,
                embedding_function=self.embeddings
            )
        return self.store.similarity_search_with_score(query, k=k)

    def load(self):
        self.store = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embeddings
        )

    def persist(self):
        pass