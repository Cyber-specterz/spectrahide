# SpectraHide 🔊

### Advanced Audio Steganography Tool

**SpectraHide** is a lightweight command-line steganography tool that allows you to hide a **text file inside a WAV audio file** without creating a separate output file.

The secret data is embedded directly into the original audio using **LSB (Least Significant Bit) steganography**.

This tool is designed for **cybersecurity learning, digital forensics practice, and steganography research**.

---

# ✨ Features

* Hide text files inside WAV audio
* Extract hidden data from audio files
* Uses **LSB Audio Steganography**
* Embeds data into the **same audio file**
* Signature-based hidden data detection
* Lightweight and fast
* Clean command line interface
* Beginner friendly
* Open source

---

# 📂 Project Structure

```
SpectraHide/
│
├── spectrahide.py
├── README.md
├── secret.txt
└── sample.wav
```

---

# ⚙️ Requirements

* Python **3.7 or higher**
* Linux / macOS / Windows

Python dependency:

```
colorama
```

---

# 📦 Installation

## 1️⃣ Clone the Repository

```
git clone https://github.com/cyberspecterz/spectrahide.git
```

## 2️⃣ Navigate to the Project Folder

```
cd spectrahide
```

---

# 🛠 Setup Guide (Recommended for Kali Linux)

Kali Linux and some Debian systems prevent installing Python packages globally.
The recommended solution is to use a **Python Virtual Environment**.

### Step 1 — Install venv

```
sudo apt install python3-venv
```

### Step 2 — Create Virtual Environment

```
python3 -m venv venv
```

### Step 3 — Activate Environment

```
source venv/bin/activate
```

Your terminal should now look like:

```
(venv) kali@kali:~/spectrahide$
```

### Step 4 — Install Dependencies

```
pip install colorama
```

Now SpectraHide is ready to use.

---

# 🚀 Usage Guide

## Hide Text File Inside Audio

Hide a text file inside an audio file:

```
python spectrahide.py hide audio.wav secret.txt
```

After running the command, the **same audio file will contain the hidden data**.

No new audio file will be created.

---

## Extract Hidden Text

Extract the hidden message from an audio file:

```
python spectrahide.py extract audio.wav recovered.txt
```

The recovered secret text will be saved as **recovered.txt**.

---

# 🧠 How SpectraHide Works

SpectraHide uses a technique called **Least Significant Bit (LSB) steganography**.

Audio files contain thousands of bytes representing sound waves.
Each byte contains a **least significant bit** that can be modified without noticeably changing the audio.

SpectraHide replaces these bits with the binary data of the secret message.

### Process

1. Convert the secret text into binary
2. Modify LSB bits of audio frames
3. Insert hidden signature markers
4. Rebuild the audio file
5. Extract data using the signature markers

The result is an audio file that **sounds identical but secretly contains hidden data**.

---

# 🎧 Supported Audio Format

Currently supported:

```
WAV (.wav)
```

Compressed formats like **MP3 or OGG** are not recommended because compression can destroy hidden data.

---

# 🧪 Example

Hide message:

```
python spectrahide.py hide music.wav message.txt
```

Extract message:

```
python spectrahide.py extract music.wav output.txt
```

---

# 📜 License

This project is released under the **MIT License**.

---

# 👨‍💻 Author

Developed by **Cyber Specterz**

Cybersecurity Research • Ethical Hacking • Security Tools

---

# ⚠️ Disclaimer

This tool is created for **educational and research purposes only**.

Do not use this tool for illegal activities.

---

# ⭐ Support

If you like this project, consider giving it a **star ⭐ on GitHub**.
