import streamlit as st
import pandas as pd
import sqlite3
from matplotlib import pyplot as plt

# Function to connect to the SQLite database
@st.cache_data
def get_connection():
    return sqlite3.connect('example.db')

# Function to execute query and return results
def run_query(query):
    conn = get_connection()
    result = pd.read_sql_query(query, conn)
    conn.close()
    return result

# Main function for the Streamlit app
def main():
    # Set the page configuration
    st.set_page_config(page_title="Text to SQL Query Converter", page_icon=":sparkles:", layout="wide")

    # Define the color scheme
    primary_color = "#FF7A59"  # Cloudflare orange
    secondary_color = "#333333"  # Dark gray

    # Apply the color scheme
    st.markdown(
        f"""
        <style>
            .stApp {{
                background-color: {secondary_color};
                color: #FFFFFF;
            }}
            .stTextArea > label {{
                color: {primary_color};
            }}
            .stButton > button {{
                background-color: {primary_color};
                color: #FFFFFF;
            }}
            .stMarkdown h1 {{
                color: {primary_color};
            }}
            .stMarkdown h2 {{
                color: {primary_color};
            }}
            .stMarkdown h3 {{
                color: {primary_color};
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Create two columns
    col1, col2 = st.columns([1, 4])

    # Chat history panel in the first column
    with col1:
        st.markdown("### Chat History")
        chat_history = []  # Initialize an empty list to store chat history

        # Function to add a new message to the chat history
        def add_message(role, content):
            chat_history.append({"role": role, "content": content})
            for chat in chat_history:
                st.markdown(f"**{chat['role']}:** {chat['content']}")

        # Add a dummy message to the chat history
        add_message("User", "Type your query here...")

    # Main app content in the second column
    with col2:
        st.title('Text to SQL Query Converter')
        user_query = st.text_area("Enter your text query")

        if st.button('Run Query'):
            try:
                data = "Hi"
                st.write("### Query Results", data)
                # Add the user query and response to the chat history
                add_message("User", user_query)
                add_message("Assistant", str(data))
            except Exception as e:
                st.error(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()