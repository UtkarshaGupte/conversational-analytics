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
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {{
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

# Initialize multiple conversation histories
if 'chat_sessions' not in st.session_state:
    st.session_state.chat_sessions = {}
if 'current_session' not in st.session_state:
    st.session_state.current_session = None

# Sidebar for chat session management
with st.sidebar:
    st.header("Chat Sessions")
    session_names = list(st.session_state.chat_sessions.keys())
    session_name = st.selectbox("Select Chat Session", options=session_names, index=len(session_names)-1 if session_names else 0)
    if st.button("New Chat Session"):
        new_session_name = f"Session {len(session_names) + 1}"
        st.session_state.chat_sessions[new_session_name] = []
        st.session_state.current_session = new_session_name
    elif session_name:
        st.session_state.current_session = session_name
    if st.button("Clear Current Chat"):
        if st.session_state.current_session and st.session_state.current_session in st.session_state.chat_sessions:
            st.session_state.chat_sessions[st.session_state.current_session] = []

# Input for new messages
user_input = st.text_input("You:")
if st.button("Send"):
    # bot_response = "here"  # Example bot response, replace with actual call to send_message_to_chatbot(user_input)
    bot_response = send_message_to_chatbot(user_input)
    if st.session_state.current_session:
        st.session_state.chat_sessions[st.session_state.current_session].append({"user": user_input, "bot": bot_response})

# Display current session chat
if st.session_state.current_session:
    history = "\n".join(
        f"You: {item['user']}\nBot: {item['bot']}\n"
        for item in st.session_state.chat_sessions[st.session_state.current_session]
    )
    st.text_area("Conversation History:", history, height=800)
else:
    st.warning("No active chat session. Please select or create a new session.")
