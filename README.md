# 🎬 YouTube Transcript Downloader

Download the transcript of any YouTube video and save it as a clean text file — automatically organized with timestamps.

---

## ✨ Features

* 📄 Fetches full video transcript
* 🧠 Supports standard YouTube links, Shorts, and Embed URLs
* 🕒 Auto-generates timestamped filenames
* 📂 Saves transcripts in a dedicated `txt/` folder
* ⚡ One-click run with auto dependency installation
* 🖥️ Cross-platform support (Windows / Linux / macOS)

---

## 📦 Project Structure

```
youtube-transcript-downloader/
│
├── app.py
├── requirements.txt
├── run.bat        # Windows auto-run
├── run.sh         # Linux/Mac auto-run
├── txt/           # Saved transcripts
└── README.md
```

---

## 🚀 Quick Start

### 🪟 Windows

1. Download or clone this repository
2. Double-click:

```
run.bat
```

The script will automatically:

* Create a virtual environment
* Install dependencies
* Launch the app

---

### 🐧 Linux / macOS

Run in terminal:

```bash
chmod +x run.sh
./run.sh
```

---

## 🧰 Manual Setup (Optional)

If you prefer manual control:

```bash
git clone https://github.com/Rakib61491/Youtube_Transcript.git
cd youtube-transcript-downloader

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
python app.py
```

---

## 📝 Usage

1. Run the application
2. Paste a YouTube video URL when prompted:

```
Enter YouTube video URL:
```

3. Transcript will be saved automatically:

```
txt/2026-02-11_14-30-05.txt
```

---

## 🔗 Supported URL Formats

* Standard watch links
* Shortened `youtu.be` links
* Embed links
* Shorts URLs

Examples:

```
https://www.youtube.com/watch?v=VIDEO_ID
https://youtu.be/VIDEO_ID
https://www.youtube.com/shorts/VIDEO_ID
```

---

## 📚 Requirements

* Python 3.8+
* Internet connection

Dependencies:

```
youtube_transcript_api==1.2.4
```

---

## ⚠️ Notes

* Transcript must be available on the video
* Auto-generated captions are supported
* Private / restricted videos will not work

---

## 🛠️ Built With

* Python
* youtube-transcript-api

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 🤝 Contributing

Pull requests, improvements, and feature ideas are welcome.

---

## ⭐ Support

If you found this useful, consider giving the repo a star ⭐
