"""Vector store for document embeddings."""
import os
import pickle
from typing import List, Optional
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from shared.config import settings


class VectorStore:
    """Manages document embeddings and similarity search."""
    
    def __init__(self):
        """Initialize the vector store with embedding model."""
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index: Optional[faiss.Index] = None
        self.texts: List[str] = []
        self.dimension = 384  # Dimension for all-MiniLM-L6-v2
        
    def create_index(self, texts: List[str]):
        """
        Create a FAISS index from text chunks.
        
        Args:
            texts: List of text chunks to index
        """
        self.texts = texts
        
        if not texts:
            return
        
        # Generate embeddings
        embeddings = self.embedding_model.encode(texts, show_progress_bar=True)
        embeddings = np.array(embeddings).astype('float32')
        
        # Create FAISS index
        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(embeddings)
        
    def search(self, query: str, k: int = 5) -> List[tuple]:
        """
        Search for similar documents.
        
        Args:
            query: Query text
            k: Number of results to return
            
        Returns:
            List of tuples (text, distance)
        """
        if self.index is None or len(self.texts) == 0:
            return []
        
        # Generate query embedding
        query_embedding = self.embedding_model.encode([query])
        query_embedding = np.array(query_embedding).astype('float32')
        
        # Search
        distances, indices = self.index.search(query_embedding, min(k, len(self.texts)))
        
        results = []
        for idx, distance in zip(indices[0], distances[0]):
            if idx < len(self.texts):
                results.append((self.texts[idx], float(distance)))
        
        return results
    
    def save(self, filepath: str):
        """Save the vector store to disk."""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'wb') as f:
            pickle.dump({
                'texts': self.texts,
                'index': self.index
            }, f)
    
    def load(self, filepath: str):
        """Load the vector store from disk."""
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                data = pickle.load(f)
                self.texts = data['texts']
                self.index = data['index']

