import spacy
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Corfu Butterflies Explorer", page_icon="🦋")

# Load data
df = pd.read_csv("butterflies.csv")

# Load spaCy NLP model
try:
    nlp = spacy.load("en_core_web_sm")
except:
    import subprocess
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")
    
# Extract keywords using spaCy 
def extract_keywords_with_spacy(query, df):
    doc = nlp(query.lower())
    all_values = set(df['color'].dropna().str.lower().unique().tolist() +
                     df['pattern'].dropna().str.lower().unique().tolist() +
                     df['extra_features'].dropna().str.lower().unique().tolist())

    extracted = []
    for token in doc:
        if token.text in all_values:
            extracted.append(token.text)
    return extracted

def pattern_explorer():
    # Streamlit UI
    st.title("🦋 Butterfly Explorer")

    # Sidebar filters
    st.sidebar.header("Filter butterflies")

    # Text input for search query
    search_query = st.sidebar.text_input("🔎 Search Query", placeholder="e.g. blue color and black dots")
    st.sidebar.markdown("---")

    selected_color = st.sidebar.selectbox("Select Color", ["All"] + sorted(df['color'].dropna().unique().tolist()))
    selected_pattern = st.sidebar.selectbox("Select Pattern", ["All"] + sorted(df['pattern'].dropna().unique().tolist()))
    selected_features = st.sidebar.selectbox("Select Extra Feature", ["All"] + sorted(df['extra_features'].dropna().unique().tolist()))

    # Filtering
    filtered_df = df.copy()

    if selected_color != "All":
        filtered_df = filtered_df[filtered_df['color'].str.contains(selected_color, case=False, na=False)]

    if selected_pattern != "All":
        filtered_df = filtered_df[filtered_df['pattern'].str.contains(selected_pattern, case=False, na=False)]

    if selected_features != "All":
        filtered_df = filtered_df[filtered_df['extra_features'].str.contains(selected_features, case=False, na=False)]

    # Apply spaCy query filtering
    if search_query:
        # Extract relevant keywords from the user's search query
        query_keywords = extract_keywords_with_spacy(search_query, df)
        if query_keywords:
            # Filter the DataFrame by checking if each keyword is present in specified columns
            filtered_df = filtered_df[
                filtered_df.apply(
                    lambda row: all(
                        any(keyword in str(row[col]).lower() for col in ['color', 'pattern', 'extra_features'])
                        for keyword in query_keywords
                    ),
                    axis=1
                )
            ]
        else:
            # Inform the user if no keywords were matched and reset the DataFrame
            st.info("🔎 Your search didn't match any known keywords (colors, patterns or features).")
            filtered_df = pd.DataFrame(columns=df.columns)

    # Display the number of butterflies found
    st.subheader(f"Found {len(filtered_df)} butterflies")

    if filtered_df.empty:
        # Warn the user if there are no matches
        st.warning("😕 No butterflies match your filters or search query.")
    else:
        # Use a 3-column layout to present the results
        cols = st.columns(3)
        for i, (_, row) in enumerate(filtered_df.iterrows()):
            with cols[i % 3]:
                # Show each butterfly image with its color, pattern, and extra features in the caption
                st.image(row["image"],
                         caption=f"{row['color']} | {row['pattern']} | {row['extra_features']}",
                         use_container_width=True)

if __name__ == "__main__":
    pattern_explorer()