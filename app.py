import streamlit as st
import google.generativeai as genai

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Medical AI Chatbot", page_icon="🏥")
st.title("🏥 Medical AI Assistant")

# --- SECRET KEY LOAD KARNA ---
# Check if key is in secrets.toml (for localhost) or Streamlit Cloud Secrets
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
else:
    # If not found (e.g., running locally without secrets), ask in sidebar
    api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

# --- CHAT LOGIC ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! I am a medical AI. How can I help?"}]

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle user input
if prompt := st.chat_input("Describe symptoms..."):
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    if not api_key:
        st.info("Please add your API key to continue.")
        st.stop()

    try:
        genai.configure(api_key=api_key)
        # Using the fast model you selected
        model = genai.GenerativeModel("gemini-2.5-flash-lite-preview-09-2025")
        
        chat = model.start_chat(history=[])
        response = chat.send_message(prompt)
        
        st.chat_message("assistant").write(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})

    except Exception as e:
        st.error(f"Error: {e}")

# --- FOOTER (YOUR NAME) ---
# This part puts your name at the bottom of the app
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #666; font-size: 14px;">
        Made with ❤️ by <strong>Atiur Rahaman</strong>
    </div>
    """,
    unsafe_allow_html=True
)