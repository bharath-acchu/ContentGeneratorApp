import streamlit as st
from frontend.api import generate_prompt, get_history

st.set_page_config(page_title="Content Generator", layout="wide")

# Login block using session_state
if "user_id" not in st.session_state:
    st.session_state.user_id = None

# Show login if user_id is not set
if st.session_state.user_id is None:
    st.title("🔐 Login to Continue")
    user_id_input = st.text_input("Enter your User ID to start:")
    
    if st.button("Login"):
        if user_id_input.strip():
            st.session_state.user_id = user_id_input.strip()
            st.success(f"Logged in as {st.session_state.user_id}")
            st.rerun()
        else:
            st.warning("User ID cannot be empty.")
    st.stop()

# 👋 Logged in - show main UI
user_id = st.session_state.user_id
st.title("🧠 Content Generator")
st.markdown(f"Welcome, **{user_id}**!")

# 🚪 Optional logout
if st.sidebar.button("🚪 Logout"):
    st.session_state.user_id = None
    st.rerun()

# Sidebar for history
with st.sidebar:
    st.header("🕓 History")
    history = get_history(user_id)
    if history:
        for h in history:
            with st.expander(h["query"]):
                st.markdown("**🎨 Casual:**")
                st.write(h["casual_response"])
                st.markdown("**🧾 Formal:**")
                st.write(h["formal_response"])
                st.caption(f"🗓️ {h['created_at']}")
    else:
        st.info("No history found.")

# Main panel
query = st.text_area("Enter your topic here:")

if st.button("Generate"):
    if not query.strip():
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating..."):
            output = generate_prompt(user_id, query)
            st.subheader("🎨 Casual Response")
            st.write(output["casual_response"])
            st.subheader("🧾 Formal Response")
            st.write(output["formal_response"])
