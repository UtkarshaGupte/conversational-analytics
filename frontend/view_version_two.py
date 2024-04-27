import requests
import streamlit as st

def send_message_to_chatbot(message):
    response = requests.post('http://127.0.0.1:8000/chatbot', json={"message": message})
    return response.json()

# Set page config
st.set_page_config(page_title="Conversational Analytics", page_icon=":sparkles:", layout="wide")

# Define color scheme
primary_color = "#FF7A59"  # Cloudflare orange
secondary_color = "#333333"  # Dark gray
background_color = "#1E1E1E"  # Dark background

# Apply CSS styles
st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {background_color};
            color: #FFFFFF;
        }}
        .stTextInput > label {{
            color: {primary_color};
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
        .stTextArea textarea {{
            background-color: {secondary_color};
            color: #FFFFFF;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Conversational Analytics")

# Initialize conversation history in Streamlit session state
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

user_input = st.text_input("You:")

if st.button("Send"):
    # response = send_message_to_chatbot(user_input)
    # bot_response = response['response']['content']
    bot_response = "here"  # Example bot response
    st.session_state.conversation_history.append({"user": user_input, "bot": bot_response})

if st.sidebar.button("Clear Conversation"):
    st.session_state.conversation_history = []

# Display conversation history in the sidebar
history = "\n".join([f"You: {item['user']}\nBot: {item['bot']}\n" for item in st.session_state.conversation_history])
st.sidebar.text_area("Conversation History:", history, height=800)
