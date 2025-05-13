import streamlit as st
from api_utils import upload_document, list_documents, delete_document

def display_sidebar():
    # Sidebar model selection
    model_options = ["gpt-4o-mini", "gpt-4o"]
    st.sidebar.selectbox("Select Model", model_options,key="model")

    # Sidebar document upload
    st.sidebar.subheader("Upload Document")
    uploaded_file = st.sidebar.file_uploader("Choose a file", type=["txt", "pdf"])
    if uploaded_file is not None:
        upload_document(uploaded_file)
        with st.spinner("Uploading..."):
            upload_response = upload_document(uploaded_file)
            if upload_response:
                st.sidebar.success(f"File '{uploaded_file.name}' uploaded successfully with ID: {upload_response['file_id']}")
            else:
                st.sidebar.error("Failed to upload document.")
    
    #Sidebar: list documents
    st.sidebar.subheader("List Documents")
    if st.sidebar.button("Refresh Documents List"):
        with st.spinner("Fetching documents..."):
            documents = list_documents()
            if documents:
                st.sidebar.write("Documents:")
                for doc in documents:
                    st.sidebar.write(f"- {doc['name']} (ID: {doc['file_id']})")
            else:
                st.sidebar.error("No documents found.")


    #Iniialize document list if it doesn't exist
    st.sidebar.header("Uploaded Documents")
    if st.sidebar.button("Refresh Document list"):
        with st.spinner("Refreshing..."):
            st.session_state.documents = list_documents()

    #Initilaize document list if not present 
    if "documents" not in st.session_state:
        st.session_state.documents = list_documents()

    documents = st.session_state.documents
    if documents:
        for doc in documents:
            st.sidebar.text(f"{doc['filename']}) (ID: {doc['file_id']},Uploaded {doc['upload_timestamp']})")
    
    #Delete document
    selected_file_id = st.sidebar.selectbox("Select Document to Delete", options = [doc["id"]
        for doc in documents], format_func=lambda doc: f"{doc['name']} (ID: {doc['file_id']})")
    if st.sidebar.button("Delete Document"):
        with st.spinner("Deleting document..."):
            delete_response = delete_document(selected_file_id)
            if delete_response:
                st.sidebar.success(f"Document with ID {selected_file_id} deleted successfully.")
            else:
                st.sidebar.error("Failed to delete document.")
    
