"""Streamlit frontend for RAG application."""
import streamlit as st
import requests
from typing import Optional


# API endpoint
API_URL = "http://localhost:8000"


def check_api_health() -> bool:
    """Check if the API is running."""
    try:
        response = requests.get(f"{API_URL}/health", timeout=5)
        return response.status_code == 200
    except Exception as e:
        st.error(f"Connection error: {str(e)}")
        return False


def upload_pdf(file) -> Optional[dict]:
    """Upload PDF to the backend."""
    try:
        files = {"file": (file.name, file.getvalue(), "application/pdf")}
        response = requests.post(f"{API_URL}/upload", files=files, timeout=60)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error uploading PDF: {str(e)}")
        if hasattr(e.response, 'text'):
            st.error(f"Response: {e.response.text}")
        return None


def query_document(question: str) -> Optional[str]:
    """Query the document via the backend."""
    try:
        response = requests.post(
            f"{API_URL}/query",
            json={"question": question},
            timeout=60
        )
        response.raise_for_status()
        return response.json()["answer"]
    except requests.exceptions.RequestException as e:
        st.error(f"Error querying document: {str(e)}")
        if hasattr(e, 'response') and e.response is not None:
            try:
                st.error(f"Response: {e.response.text}")
            except:
                pass
        return None


def main():
    """Main Streamlit app."""
    st.set_page_config(
    page_title="DocQuery | RAG Based Document Assistant",
    page_icon=" ",
    layout="wide"
    )

    st.markdown(
        """
        <style>
        .main-title {
            font-size: 42px;
            font-weight: 700;
            margin-bottom: 0;
        }

        .subtitle {
            font-size: 18px;
            color: #777;
            margin-top: 5px;
            margin-bottom: 25px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-title">📄 DocQuery</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">RAG based document assistant</div>',
        unsafe_allow_html=True
    )
    
    # Check API health
    with st.spinner("Checking backend connection..."):
        if not check_api_health():
            st.error("⚠️ Backend API is not running. Please start the FastAPI server first.")
            st.code("uv run uvicorn backend.main:app --reload", language="bash")
            st.info("Make sure the backend is running on http://localhost:8000")
            return
    
    # Sidebar for PDF upload
    with st.sidebar:
        st.header("Upload Document")
        uploaded_file = st.file_uploader(
            "Upload a PDF",
            type="pdf",
            help="Upload a PDF and ask questions about its contents"
        )
        
        if uploaded_file is not None:
            if st.button("Upload and Process", type="primary"):
                with st.spinner("Processing PDF..."):
                    result = upload_pdf(uploaded_file)
                    if result:
                        st.success(f"✅ {result['message']}")
                        st.info(f"Processed {result['chunks']} text chunks")
                        st.session_state.pdf_uploaded = True
                        st.session_state.pdf_filename = result['filename']
        
        if st.session_state.get("pdf_uploaded", False):
            st.success("PDF is ready for queries!")
            st.caption(f"File: {st.session_state.get('pdf_filename', 'Unknown')}")
    
    # Main content area
    if not st.session_state.get("pdf_uploaded", False):
        st.info("👈 Please upload a PDF file using the sidebar to get started.")
    else:
        st.header("Ask Away!")
        
        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []
        
        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Chat input
        if question := st.chat_input("Ask anything about your document"):
            # Add user message
            st.session_state.messages.append({"role": "user", "content": question})
            with st.chat_message("user"):
                st.markdown(question)
            
            # Get answer
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    answer = query_document(question)
                    if answer:
                        st.markdown(answer)
                        st.session_state.messages.append({"role": "assistant", "content": answer})
                    else:
                        error_msg = "Sorry, I couldn't process your question. Please try again."
                        st.error(error_msg)
                        st.session_state.messages.append({"role": "assistant", "content": error_msg})


if __name__ == "__main__":
    main()

