<h1 align="center"><a href="https://streamlink.github.io/">Streamlink<br><img height="150" alt="Streamlink" src="https://raw.githubusercontent.com/3bdoSamy/streamlink-ar/main/icon.svg"></a></h1>

<p align="center">
  <a href="https://streamlink.github.io/install.html"><img alt="Supported Python versions" src="https://img.shields.io/pypi/pyversions/streamlink.svg?style=flat-square&maxAge=86400"></a>
  <a href="https://streamlink.github.io/changelog.html"><img alt="Latest release" src="https://img.shields.io/github/release/3bdoSamy/streamlink-ar.svg?style=flat-square&maxAge=86400"></a>
  <a href="https://github.com/3bdoSamy/streamlink-ar"><img alt="License" src="https://img.shields.io/github/license/3bdoSamy/streamlink-ar.svg?style=flat-square&maxAge=86400"></a>
  <a href="https://github.com/3bdoSamy/streamlink-ar/issues"><img alt="Open issues" src="https://img.shields.io/github/issues/3bdoSamy/streamlink-ar.svg?style=flat-square&maxAge=86400"></a>
  <a href="https://github.com/3bdoSamy/streamlink-ar/actions?query=event%3Apush"><img alt="Build status" src="https://img.shields.io/github/actions/workflow/status/3bdoSamy/streamlink-ar/test.yml?branch=main&event=push&style=flat-square&maxAge=86400"></a>
  <a href="https://codecov.io/github/3bdoSamy/streamlink-ar?branch=main"><img alt="Overall code coverage" src="https://img.shields.io/codecov/c/github/3bdoSamy/streamlink-ar.svg?branch=main&style=flat-square&maxAge=86400"></a>
</p>

---

## 🧩 Fork notice

This repository is a **fork** of the original Streamlink project:

- 🔗 Original repo: https://github.com/streamlink/streamlink

If you need full features, advanced docs, or upstream support, please use/check the original repository.

---

## 📦 Fork install quickstart (streamlink-ar)


## Fork install quickstart (streamlink-ar)

### Windows Git Bash

```bash
git clone https://github.com/3bdoSamy/streamlink-ar.git
cd streamlink-ar
py -3.10 -m venv .venv
source .venv/Scripts/activate
python -m pip install -U pip setuptools wheel
pip install -e .
streamlink-ar --version
streamlink-ar --help | grep ffmpeg-dkey
```

### Windows PowerShell

```powershell
git clone https://github.com/3bdoSamy/streamlink-ar.git
cd streamlink-ar
py -3.10 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -U pip setuptools wheel
pip install -e .
streamlink-ar --version
streamlink-ar --help | Select-String ffmpeg-dkey
```

# 👍 Features

```bash
git clone https://github.com/3bdoSamy/streamlink-ar.git
cd streamlink-ar
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip setuptools wheel
pip install -e .
streamlink-ar --version
```

### 🪟 Windows (PowerShell)

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

## ⚡ Quick start

```bash
streamlink-ar --ffmpeg-dkey key "streamurl" best
```

---

## 🙌 Need anything else?

For everything beyond this fork's small changes, please refer to the original Streamlink repo:

  [streamlink-installation-windows]: https://streamlink.github.io/install.html#windows
  [streamlink-installation-macos]: https://streamlink.github.io/install.html#macos
  [streamlink-installation-linux-and-bsd]: https://streamlink.github.io/install.html#linux-and-bsd
  [streamlink-installation-pypi-source]: https://streamlink.github.io/install.html#pypi-package-and-source-code
  [streamlink-documentation-cli]: https://streamlink.github.io/cli.html
  [streamlink-documentation-apiguide]: https://streamlink.github.io/api_guide.html
  [streamlink-documentation-apiref]: https://streamlink.github.io/api.html
  [streamlink-plugins]: https://streamlink.github.io/plugins.html
  [player-vlc]: https://www.videolan.org/vlc/
  [contributing]: https://github.com/3bdoSamy/streamlink-ar/blob/main/CONTRIBUTING.md
  [support]: https://streamlink.github.io/latest/support.html
