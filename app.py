import streamlit as st
import pandas as pd
from langchain import LangChain

# Function to load CSV file
def load_data(file):
    data = pd.read_csv(file)
    return data

# Function to chat with LangChain
def langchain_chat(text):
    # Initialize LangChain
    lc = LangChain()
    response = lc.generate(text)
    return response

def main():
    st.title("CSV Chat with LangChain")

    # File upload
    uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])

    if uploaded_file is not None:
        # Load data
        data = load_data(uploaded_file)

        # Display data
        st.write("### Data Preview")
        st.write(data)

        # Chat interface
        st.write("### Chat with LangChain")
        user_input = st.text_input("You:", "")

        if st.button("Send"):
            if user_input.strip() != "":
                # Chat with LangChain
                response = langchain_chat(user_input)
                st.write("LangChain:", response)
            else:
                st.warning("Please enter something to chat.")

if __name__ == "__main__":
    main()
