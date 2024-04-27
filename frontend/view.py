import streamlit as st
import pandas as pd
import sqlite3
# import matplotlib.pyplot as plt

# Function to connect to the SQLite database
@st.cache
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
    # Title of the application
    st.title('Text to SQL Query Converter')

    # Text input for user query
    user_query = st.text_area("Enter your text query", "Type your query here...")

    # Button to execute the query
    if st.button('Run Query'):
        # Placeholder to handle basic natural language to SQL conversion
        # For example purposes, assuming user types SQL directly
        # A proper NLP model or parsing mechanism is required here for actual text to SQL
        try:
            # Run the user query
            data = run_query(user_query)
            # Display data as a table
            st.write("### Query Results", data)
            
            # Display data graphically
            st.write("### Graphical Representation")
            # fig, ax = plt.subplots()
            if len(data.columns) == 2:  # simple case for one independent variable and one dependent variable
                ax.plot(data.iloc[:, 0], data.iloc[:, 1])
                ax.set_xlabel(data.columns[0])
                ax.set_ylabel(data.columns[1])
                ax.set_title('Line Plot')
            else:
                st.write("Graphical representation not available for more than 2 columns.")
            st.pyplot(fig)
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
