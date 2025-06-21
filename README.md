# SoundScope

<p align="center">
  <img src="static/assets/logo.png" alt="SoundScope Logo" width="120"/>
</p>

<p align="center">
  <b>Modern web app for real-time audio analysis & visualization</b><br>
  <i>Upload MP3s, play in-browser, and watch a live loudness graph synced to your music.</i>
</p>

---

## 🚀 Features

- <b>MP3 Upload & Playback:</b> Instantly upload and play your audio files in the browser.
- <b>Real-Time Loudness Analysis:</b> See per-second loudness (dB) calculated live as your music plays.
- <b>Live Visualization:</b> Interactive, modern bar chart updates in sync with playback.
- <b>Responsive UI:</b> Clean, glassmorphism-inspired design for desktop & mobile.

---

## 🖼️ Screenshots

<p align="center">
  <img src="static/assets/download.jpg" alt="SoundScope Screenshot" width="600"/>
</p>

---

## ⚙️ Tech Stack

- <b>Backend:</b> Python, Flask, Flask-SocketIO, pydub, numpy
- <b>Frontend:</b> HTML5, CSS3, Chart.js, JavaScript (ES6)
- <b>Audio Analysis:</b> Per-second RMS/dB calculation

---

## 📝 Getting Started

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/SoundScope.git
cd SoundScope
```

### 2. Install dependencies

```sh
pip install -r requirements.txt
```

### 3. Run the application

```sh
python app.py
```

The app will be available at [http://localhost:5000](http://localhost:5000)

---

## 📂 Project Structure

```
SoundScope/
├── app.py                # Main Flask app
├── requirements.txt      # Python dependencies
├── analysis/             # Audio analysis modules
├── static/               # Static files (CSS, JS, images)
├── templates/            # HTML templates
├── uploads/              # Uploaded audio files
└── static_data/          # Example audio files
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!<br>
Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

<p align="center">
  <b>SoundScope</b> | Real-Time Audio Analysis & Visualization
</p>