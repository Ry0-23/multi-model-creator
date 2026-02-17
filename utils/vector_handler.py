import numpy as np
from typing import List, Dict, Any, Optional, Tuple
import json
from abc import ABC, abstractmethod

class VectorHandler(ABC):
    """Abstract base class for vector operations."""
    
    @abstractmethod
    def embed(self, text: str) -> np.ndarray:
        """Convert text to vector embedding."""
        pass
    
    @abstractmethod
    def embed_batch(self, texts: List[str]) -> np.ndarray:
        """Convert multiple texts to vector embeddings."""
        pass
    
    @abstractmethod
    def similarity(self, vector1: np.ndarray, vector2: np.ndarray) -> float:
        """Calculate similarity between two vectors."""
        pass


class EmbeddingHandler(VectorHandler):
    """Handles text embedding operations."""
    
    def __init__(self, model_name: str = "default"):
        self.model_name = model_name
        self.embedding_dim = 768
    
    def embed(self, text: str) -> np.ndarray:
        """Convert text to embedding vector."""
        if not text or not isinstance(text, str):
            return np.zeros(self.embedding_dim)
        
        # Placeholder: replace with actual embedding model
        return np.random.randn(self.embedding_dim).astype(np.float32)
    
    def embed_batch(self, texts: List[str]) -> np.ndarray:
        """Embed multiple texts."""
        embeddings = [self.embed(text) for text in texts]
        return np.array(embeddings)
    
    def similarity(self, vector1: np.ndarray, vector2: np.ndarray) -> float:
        """Cosine similarity between vectors."""
        dot_product = np.dot(vector1, vector2)
        norm1 = np.linalg.norm(vector1)
        norm2 = np.linalg.norm(vector2)
        
        if norm1 == 0 or norm2 == 0:
            return 0.0
        
        return float(dot_product / (norm1 * norm2))


class VectorStore:
    """Stores and retrieves vectors with metadata."""
    
    def __init__(self, embedding_handler: EmbeddingHandler):
        self.handler = embedding_handler
        self.vectors: List[np.ndarray] = []
        self.metadata: List[Dict[str, Any]] = []
    
    def add(self, text: str, meta: Optional[Dict[str, Any]] = None) -> None:
        """Add vector and metadata to store."""
        vector = self.handler.embed(text)
        self.vectors.append(vector)
        self.metadata.append(meta or {})
    
    def add_batch(self, texts: List[str], metas: Optional[List[Dict]] = None) -> None:
        """Add multiple vectors."""
        vectors = self.handler.embed_batch(texts)
        metas = metas or [{} for _ in texts]
        
        self.vectors.extend(vectors)
        self.metadata.extend(metas)
    
    def search(self, query: str, top_k: int = 5) -> List[Tuple[float, Dict]]:
        """Search for similar vectors."""
        query_vector = self.handler.embed(query)
        similarities = [
            self.handler.similarity(query_vector, vec) 
            for vec in self.vectors
        ]
        
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        return [
            (similarities[i], self.metadata[i]) 
            for i in top_indices
        ]
    
    def clear(self) -> None:
        """Clear all vectors and metadata."""
        self.vectors.clear()
        self.metadata.clear()
    
    def size(self) -> int:
        """Get number of stored vectors."""
        return len(self.vectors)