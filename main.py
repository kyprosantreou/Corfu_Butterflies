import streamlit as st

about_page = st.Page("about.py", title="About", icon="ℹ️")
pattern_explorer = st.Page("pattern_explorer.py", title="Butterfly Explorer", icon="🔎")
visual_search = st.Page("visual_search.py", title="Visual Butterfly Match", icon="📷")

pg = st.navigation({
    "Informations":[about_page],
    "Tools":[pattern_explorer,visual_search]
    })

pg.run()