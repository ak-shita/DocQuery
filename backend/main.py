"""FastAPI backend for RAG application."""
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
from shared.config import settings
from shared.pdf_processor import extract_text_from_pdf, split_text_into_chunks
from shared.vector_store import VectorStore
from shared.rag import RAGSystem


app = FastAPI(title="RAG API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global state
vector_store = VectorStore()
rag_system: Optional[RAGSystem] = None
UPLOAD_DIR = "uploads"


os.makedirs(UPLOAD_DIR, exist_ok=True)


class QueryRequest(BaseModel):
    """Request model for query endpoint."""
    question: str


class QueryResponse(BaseModel):
    """Response model for query endpoint."""
    answer: str


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "RAG API is running"}


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF file and process it.
    
    Args:
        file: PDF file to upload
        
    Returns:
        Success message
    """
    global vector_store, rag_system
    
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="File must be a PDF")
    
    # Read file content
    contents = await file.read()
    
    # Extract text from PDF
    text = extract_text_from_pdf(contents)
    
    if not text.strip():
        raise HTTPException(status_code=400, detail="PDF contains no extractable text")
    
    # Split into chunks
    chunks = split_text_into_chunks(
        text,
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap
    )
    
    # Create vector store
    vector_store = VectorStore()
    vector_store.create_index(chunks)
    
    # Initialize RAG system
    rag_system = RAGSystem(vector_store)
    
    # Save file locally
    filepath = os.path.join(UPLOAD_DIR, file.filename)
    with open(filepath, 'wb') as f:
        f.write(contents)
    
    return {
        "message": "PDF uploaded and processed successfully",
        "chunks": len(chunks),
        "filename": file.filename
    }


@app.post("/query", response_model=QueryResponse)
async def query_document(request: QueryRequest):
    """
    Query the uploaded document.
    
    Args:
        request: Query request with question
        
    Returns:
        Answer to the question
    """
    global rag_system
    
    if rag_system is None:
        raise HTTPException(status_code=400, detail="No PDF uploaded. Please upload a PDF first.")
    
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    
    try:
        answer = rag_system.query(request.question)
        return QueryResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

