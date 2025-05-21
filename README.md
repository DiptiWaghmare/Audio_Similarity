# 🔊 Audio Similarity Checker

This is a Streamlit-based web application that allows users to upload and compare two audio files to determine how similar they sound. The tool visualizes waveforms and computes a similarity score using audio embeddings.

## 🧠 Features

- Upload and listen to two audio files (`.wav` or `.mp3`)
- View waveform plots for each speaker
- Extract speaker embeddings from both files
- Compute and display a similarity score
- Intuitive UI built using Streamlit

## 🚀 Live Demo

> Coming soon (you can deploy this app to [Streamlit Community Cloud](https://streamlit.io/cloud) or [Render](https://render.com))!

## 🛠️ Technologies Used

- Python
- [Streamlit](https://streamlit.io/) for UI
- [Librosa](https://librosa.org/) for audio processing
- [Matplotlib](https://matplotlib.org/) for waveform visualization
- Custom audio embedding extraction using `extract_embedding` and `get_similarity_score`

## 📥 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/audio-similarity-checker.git
   cd audio-similarity-checker
