# 🔊 Audio Similarity Checker
This is a Streamlit-based web application that allows users to upload and compare two audio files to determine how similar they sound. The tool visualizes waveforms and computes a similarity score using audio embeddings.
![app_overview](https://github.com/user-attachments/assets/90c437ce-ec07-4610-8cbe-051d04fccc66)
![Uploading_audios](https://github.com/user-attachments/assets/640d45bc-7601-4234-acd5-92c1bc55f1ac)
![Audios_similar](https://github.com/user-attachments/assets/1f2236f2-ecd5-446e-9351-dd89c788bb2a)
![Audios_not_similar](https://github.com/user-attachments/assets/be7af023-eda6-49a1-a3f6-0500c1edd4d7)



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

## Requirements
- streamlit - 1.35.0
- librosa - 0.10.1
- matplotlib - 3.8.4
- numpy - 1.26.4
- soundfile - 0.12.1
- scikit-learn - 1.4.2
- torch - 2.2.2
- torchaudio - 2.2.2
- pyannote-audio - 3.1.1


## 📥 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/DiptiWaghmare/Audio_Similarity.git
   cd audio-similarity-checker

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

Note: The pyannote-audio library downloads models from [Hugging Face](https://huggingface.co/) (e.g. pyannote/embedding). You’ll need to be logged into Hugging Face via CLI or API token, especially for some models that require authentication.

4. Run the app
   ```bash
   streamlit run app_streamlit.py
   
## 📊 Similarity Score

The similarity score is computed using pre-trained audio embeddings. If the score is above a threshold (default 0.7), the audios are considered similar.

## 🔒 Disclaimer

This tool is intended for research or demo purposes only and may not generalize perfectly to all audio types or languages.


