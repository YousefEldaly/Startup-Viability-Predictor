from abc import ABC, abstractmethod

class VectorStoreBase(ABC):
    @abstractmethod
    def create(self, texts, metadatas=None):
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def add_texts(self, texts, metadatas=None):
        pass

    @abstractmethod
    def similarity_search(self, query, k):
        pass

    @abstractmethod
    def similarity_search_with_score(self, query, k):
        pass

    @abstractmethod
    def persist(self):
        pass
