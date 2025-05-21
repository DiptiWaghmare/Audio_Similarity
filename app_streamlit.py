import streamlit as st
import librosa
import matplotlib.pyplot as plt
import numpy as np
import os

from audio_utils import extract_embedding, get_similarity_score

st.set_page_config(page_title="Audio Similarity Checker", layout="wide")
st.title("🔊 Audio Similarity Checker")

# Helper: Plot waveform (smaller size)
def plot_waveform_line(audio, sr, title):
    fig, ax = plt.subplots(figsize=(4, 2))  # Adjust size here
    duration = len(audio) / sr
    time_axis = np.linspace(0, duration, num=len(audio))
    ax.plot(time_axis, audio, color='maroon', linewidth=0.8)
    ax.set_title(title, fontsize=9)
    ax.set_xlabel("Time (s)", fontsize=8)
    ax.set_ylabel("Amplitude", fontsize=8)
    ax.grid(True, linestyle='--', linewidth=0.3, alpha=0.6)
    ax.tick_params(axis='both', labelsize=6)
    st.pyplot(fig)

    

# Create two columns
col1, col2 = st.columns(2)

with col1:
    uploaded_file1 = st.file_uploader("📤 Upload first audio file", type=["wav", "mp3"], key="file1")
    if uploaded_file1:
        audio_bytes1 = uploaded_file1.read()

        # Save to disk for embedding extraction
        with open("temp1.wav", "wb") as f:
            f.write(audio_bytes1)

        # Playback
        st.audio(audio_bytes1, format='audio/wav')

        # Load for waveform
        audio1, sr1 = librosa.load("temp1.wav", sr=None)
        st.markdown("##### 🎵 Speaker 1 - Waveform")
        plot_waveform_line(audio1, sr1, "Speaker 1")

with col2:
    uploaded_file2 = st.file_uploader("📤 Upload second audio file", type=["wav", "mp3"], key="file2")
    if uploaded_file2:
        audio_bytes2 = uploaded_file2.read()

        # Save to disk for embedding extraction
        with open("temp2.wav", "wb") as f:
            f.write(audio_bytes2)

        # Playback
        st.audio(audio_bytes2, format='audio/wav')

        # Load for waveform
        audio2, sr2 = librosa.load("temp2.wav", sr=None)
        st.markdown("##### 🎵 Speaker 2 - Waveform")
        plot_waveform_line(audio2, sr2, "Speaker 2")

# Similarity Button
st.markdown("---")
if uploaded_file1 and uploaded_file2:
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

        # Cleanup
        os.remove("temp1.wav")
        os.remove("temp2.wav")
