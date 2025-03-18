import streamlit as st
from nlp import chat_with_gpt
from cv import analyze_image
from neo4j_utils import Neo4jConnector

# Initialize Neo4j connector
connector = Neo4jConnector("bolt://localhost:7687", "neo4j", "password")

st.title("Multimodal AI Customer Support Agent")

# Text-based query
user_input = st.text_input("Ask a question:")
if user_input:
    response = chat_with_gpt(user_input)
    st.write(response)

# Image-based query
uploaded_file = st.file_uploader("Upload a product image:")
if uploaded_file is not None:
    query = "Is this product covered under warranty?"
    result = analyze_image(uploaded_file, query)
    product_info = connector.get_product_info("123")  # Replace with dynamic ID
    st.write(f"Analysis result: {result}")
    st.write(f"Product info: {product_info}")