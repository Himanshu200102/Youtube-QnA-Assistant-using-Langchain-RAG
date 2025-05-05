import langchain_helper as lch
import streamlit as st
import textwrap

# Page config
st.set_page_config(page_title="YouTube Assistant", page_icon="??", layout="centered")

# Styling
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #fafafa;
    }
    .stTextArea textarea {
        background-color: #262730 !important;
        color: #fafafa !important;
    }
    .stButton>button {
        background-color: #00c4ff !important;
        color: black !important;
    }
    .stTextInput>div>input {
        background-color: #262730 !important;
        color: #fafafa !important;
    }
    .stMarkdown h1, .stMarkdown h2 {
        color: #00c4ff;
    }
    </style>
""", unsafe_allow_html=True)

st.title("?? YouTube Assistant")
st.markdown("Ask questions about any YouTube video. Paste the video URL, type your question, and get instant answers!")

# Sidebar form
with st.sidebar:
    st.header("?? Ask Away")
    with st.form(key='my_form'):
        youtube_url = st.text_area(
            label="?? YouTube Video URL",
            placeholder="https://www.youtube.com/watch?v=...",
            max_chars=100
        )
        query = st.text_area(
            label="?Your Question",
            placeholder="What is this video about?",
            max_chars=100,
            key="query"
        )
        submit = st.form_submit_button(label="?? Get Answer")

# Main interaction
if query and youtube_url:
    with st.spinner("Processing your request..."):
        db = lch.vector_db_video_url(youtube_url)
        response, docs = lch.get_response_from_query(db, query)
    st.success("? Here's the Answer:")
    st.markdown(f"""
    <div style='background-color: #262730; padding: 15px; border-radius: 10px; color: #fafafa;'>
        {textwrap.fill(response, width=80).replace('\n', '<br>')}
    </div>
    """, unsafe_allow_html=True)
