import streamlit as st
import logging
from llama_index.vector_stores import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Streamlit app UI
st.title("Document Query App")
st.sidebar.title("Settings")

# Sidebar options
embedding_model = st.sidebar.selectbox(
    "Select Embedding Model",
    ["all-mpnet-base-v2", "all-MiniLM-L6-v2"]
)

chunk_size = st.sidebar.slider("Chunk Size", min_value=512, max_value=2048, value=1024)
chunk_overlap = st.sidebar.slider("Chunk Overlap", min_value=10, max_value=200, value=50)

# Upload Document
uploaded_file = st.file_uploader("Upload Document", type=["txt", "pdf"])
if uploaded_file is not None:
    st.success("File uploaded successfully!")

# Query Input
query = st.text_input("Enter your query:")
if query:
    st.info(f"Processing your query: {query}")
    # Dummy response for Streamlit demo
    st.write("Response: This is a placeholder for the LLM output.")

st.sidebar.markdown("### About")
st.sidebar.info("This app uses LlamaIndex and HuggingFace embeddings to process documents.")

