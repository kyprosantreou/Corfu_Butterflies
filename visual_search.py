import torch
import streamlit as st
from PIL import Image
import open_clip
import torch.nn.functional as F


if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"

model, preprocess, tokenizer = open_clip.create_model_and_transforms('ViT-B-32', pretrained='laion2b_s34b_b79k')
model = model.to(device)
model.eval()

def get_image_embedding(image):
    image = preprocess(image).unsqueeze(0).to(device)
    with torch.no_grad():
        image_features = model.encode_image(image)
        image_features /= image_features.norm(dim=-1, keepdim=True)
    return image_features.cpu()

def visual_search(preselected_image_path=None):
    st.title("🦋 Visual Search")
    st.markdown("Searching for butterflies based on visual similarity")

    if preselected_image_path:
        user_image = Image.open(preselected_image_path)
        st.image(user_image, caption="Selected butterfly image", use_container_width=True)
    else:
        uploaded_image = st.file_uploader("Upload a picture of a butterfly", type=["jpg", "png"])
        if not uploaded_image:
            return
        user_image = Image.open(uploaded_image)
        st.image(user_image, caption="The image you uploaded", use_container_width=True)

    # Compute embedding
    user_image_embedding = get_image_embedding(user_image)

    # Load stored embeddings
    image_embeddings, image_paths = torch.load("butterfly_embeddings.pt")

    # Compute cosine similarity
    similarities = F.cosine_similarity(user_image_embedding, image_embeddings)

    top_k = similarities.topk(5)
    top_paths = [image_paths[i] for i in top_k.indices]

    st.subheader("🔍 The 5 most similar butterflies:")
    cols = st.columns(3)
    for i, path in enumerate(top_paths):
        with cols[i % 3]:
            st.image(path, use_container_width=True)

if __name__ == "__main__":
    visual_search()