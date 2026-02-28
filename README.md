# 🧩 Fork Notice

This repository is a fork of the original project:

🔗 Original repository:  
👉 https://github.com/streamlink/streamlink  

If you need full features, advanced documentation, or upstream support, please refer to the original project.

---

# 📦 Installation (streamlink-ar)

## 🪟 Windows – Git Bash

```bash
git clone https://github.com/3bdoSamy/streamlink-ar.git
cd streamlink-ar
py -3.10 -m venv .venv
source .venv/Scripts/activate
python -m pip install -U pip setuptools wheel
pip install -e .
streamlink-ar --version
```

---

## 🪟 Windows – PowerShell

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
              -o "C:\Users\User\Downloads\test.mkv"
```

---

## 🎧 Multiple Audio Languages Example

```bash
streamlink-ar --audio-lang Ara \
              --audio-lang En \
              "URL of mpd" best \
              -o "C:\Users\User\Downloads\test.mkv"
```

---

# 🙌 Need Anything Else?

For everything beyond this fork’s small additions, please check the original repository:

🔗 https://github.com/streamlink/streamlink
