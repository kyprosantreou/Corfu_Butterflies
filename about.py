import streamlit as st

st.set_page_config(page_title= "Corfu Butterflies Explorer", page_icon="🦋", layout="centered")

st.markdown(
    """<h1 style='white-space: nowrap;'>🦋 Welcome to the Corfu Butterflies Explorer</h1>""",
    unsafe_allow_html=True
)
st.markdown("""
This is a web application designed to help you explore and discover the beautiful butterflies of Corfu, Greece. 
Whether you're a butterfly enthusiast, a nature lover, or just curious about these fascinating creatures, this app
has something for you!
The app is divided into two main sections:
- 🔎🦋**Butterfly Explorer**: Browse and filter butterflies based on their color, pattern, and extra features.
- 📷**Visual Butterfly Match**: Upload a picture of a butterfly and find similar butterflies from our database.
""")

st.image("bg.png", use_container_width=True)
