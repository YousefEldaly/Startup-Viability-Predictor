# DataFrameRAG.py
import pandas as pd
from algorithms.RAG.RAGChain import RAGChain
class DataFrameRAG:
    def __init__(self, df, text_column, rag_chain: RAGChain):
        self.df = df
        self.text_column = text_column
        self.rag_chain = rag_chain

    def build_index(self):
        texts = self.df[self.text_column].fillna("").astype(str).tolist()
        metadatas = [{"row_index": i} for i in self.df.index]
        self.rag_chain.create_vectorstore(texts, metadatas)
    
    def query(self, text, k=50, threshold=80.0):
        """
        Search for similar rows with proper cosine similarity conversion.
        """
        results_with_scores = self.rag_chain.similarity_search_with_score(text, k=k)
        rows = []
        for doc, distance in results_with_scores:
            similarity_pct = (1 - distance) * 100 
            if similarity_pct >= threshold:
                row_index = doc.metadata["row_index"]
                row = self.df.loc[row_index].copy()
                row["similarity"] = round(similarity_pct, 2)
                rows.append(row)
        return pd.DataFrame(rows).sort_values("similarity", ascending=False).reset_index(drop=True)
