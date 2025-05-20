import streamlit as st
from audio_utils import extract_embedding, get_similarity_score
import os

st.set_page_config(page_title="Audio Similarity Checker", layout="centered")
st.title("🔊 Audio Similarity Checker")

uploaded_file1 = st.file_uploader("Upload first audio file", type=["wav", "mp3"])
uploaded_file2 = st.file_uploader("Upload second audio file", type=["wav", "mp3"])

if uploaded_file1 and uploaded_file2:
    with open("temp1.wav", "wb") as f:
        f.write(uploaded_file1.read())
    with open("temp2.wav", "wb") as f:
        f.write(uploaded_file2.read())

    if st.button("🎯 Check Similarity"):
        st.info("✅ Files uploaded. Extracting embeddings...")

        emb1 = extract_embedding("temp1.wav")
        emb2 = extract_embedding("temp2.wav")

        score = get_similarity_score(emb1, emb2)

        st.subheader(f"🧠 Similarity Score: `{score:.3f}`")

        if score > 0.7:
            st.success("🎧 The audios are similar!")
        else:
            st.warning("🛑 The audios are NOT similar.")

        os.remove("temp1.wav")
        os.remove("temp2.wav")