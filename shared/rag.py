"""RAG (Retrieval Augmented Generation) implementation."""
from langchain_ollama import ChatOllama

from shared.config import settings
from shared.vector_store import VectorStore


class RAGSystem:
    """RAG system for querying documents."""

    def __init__(self, vector_store: VectorStore):
        """Initialize RAG system."""
        self.vector_store = vector_store

        self.llm = ChatOllama(
            model=settings.llm_model,
            temperature=0.2,
        )

    def query(self, question: str, top_k: int = 5) -> str:
        """Answer a question using retrieved document context."""

        # Retrieve relevant document chunks
        results = self.vector_store.search(question, k=top_k)

        if not results:
            return "No relevant documents found. Please upload a PDF first."

        # Build context from retrieved documents
        context_parts = []

        for text, distance in results:
            context_parts.append(text)

        context = "\n\n".join(context_parts)

        # Build RAG prompt
        prompt = f"""You are a helpful document assistant.

Answer the user's question using ONLY the information
contained in the provided document context.

If the context does not contain enough information,
say that the information is not available in the document.

Be concise and accurate.

DOCUMENT CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

        # Generate answer using local LLM
        response = self.llm.invoke(prompt)

        return response.content