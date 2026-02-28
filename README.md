# 🧩 Fork Notice

This repository is a fork of the original project:

🔗 Original repository:  
👉 https://github.com/streamlink/streamlink  

If you need full features, advanced documentation, or upstream support, please refer to the original project.

---

# 📦 Installation (streamlink-ar)

## 🪟 Windows (PowerShell)

```powershell
git clone https://github.com/3bdoSamy/streamlink-ar.git
cd streamlink-ar
py -3.10 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -U pip setuptools wheel
pip install -e .
streamlink-ar --version
```

---

## 🐧 Linux

```bash
git clone https://github.com/3bdoSamy/streamlink-ar.git
cd streamlink-ar
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip setuptools wheel
pip install -e .
streamlink-ar --version
```

---

# ⚡ Quick Start

```bash
streamlink-ar --ffmpeg-dkey key "streamurl" best
```

---

# 👍 Features

✨ Fork of Streamlink with added support for:

- 🔐 Specify one or more decryption keys using `--ffmpeg-dkey`
- 🎧 Select multiple audio languages (e.g. Arabic & English)
- 🟢 Tested on DASH Live encrypted streams

---

## 🔐 Multiple Decryption Keys Example

```bash
streamlink-ar --ffmpeg-dkey "03de....." \
              --ffmpeg-dkey "92ce....." \
              "URL of mpd" best \
              -o "/home/user/Downloads/test.mkv"
```

---

## 🎧 Multiple Audio Languages Example

```bash
streamlink-ar --audio-lang Ara \
              --audio-lang En \
              "URL of mpd" best \
              -o "/home/user/Downloads/test.mkv"
```

---

# 🙌 Need Anything Else?

For everything beyond this fork’s small additions, please check the original repository:

🔗 https://github.com/streamlink/streamlink

---

# ⚠️ Disclaimer

This project is created **for educational and research purposes only**.

It is intended to demonstrate how encrypted DASH streams and decryption keys can be handled programmatically for learning and testing environments.

❗ The author does **NOT** encourage, support, or promote:
- Circumventing DRM protections
- Accessing paid or restricted content without authorization
- Violating any platform’s Terms of Service
- Any illegal activity

By using this software, you agree that:

- You are solely responsible for how you use it.
- You will comply with all applicable laws in your country.
- You will only use it with content you are legally authorized to access.

The author assumes **no liability** for misuse, damages, legal issues, or violations resulting from the use of this project.

If you do not agree with these terms, do not use this software.

---

# 🤖 AI Assistance Notice

Parts of this project, including documentation and minor development tasks, were created or improved with the assistance of AI tools.

All final decisions, testing, and modifications were reviewed and validated by the repository owner.
