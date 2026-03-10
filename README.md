# SpectraHide 🔊

### Advanced Audio Steganography Tool

**SpectraHide** is a lightweight command-line steganography tool that allows you to hide a **text file inside a WAV audio file** without creating a separate output file.
The secret data is embedded directly into the original audio using **LSB (Least Significant Bit) steganography**.

This tool is designed for **cybersecurity learning, digital forensics practice, and steganography research**.

---

## ✨ Features

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

## 📂 Project Structure

```
SpectraHide/
│
├── spectrahide.py
├── README.md
├── secret.txt
└── sample.wav
```

---

## ⚙️ Requirements

* Python **3.7+**
* Linux / macOS / Windows

Python library:

```
colorama
```

---

## 📦 Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/cyberspecterz/spectrahide.git
```

### 2️⃣ Move into the project folder

```
cd spectrahide
```

### 3️⃣ Install required dependency

```
pip install colorama
```

---

## 🚀 Usage

### Hide Text File Inside Audio

This command hides a **text file inside an audio file**.

```
python3 spectrahide.py hide audio.wav secret.txt
```

After execution, the **same audio file will contain the hidden data**.

No new output audio file will be created.

---

### Extract Hidden Data

To extract the hidden text from an audio file:

```
python3 spectrahide.py extract audio.wav recovered.txt
```

The extracted message will be saved into **recovered.txt**.

---

## 🧠 How It Works

SpectraHide uses a technique called **Least Significant Bit (LSB) steganography**.

Audio files contain thousands of bytes representing sound waves.
Each byte has a **least significant bit** that can be modified without noticeably changing the audio.

SpectraHide replaces these bits with the binary data of the secret message.

Steps:

1. Convert secret text into binary
2. Modify LSB bits of audio frames
3. Insert hidden signature markers
4. Rebuild the audio file
5. Extract data using the signature markers

The result is an audio file that **sounds identical but secretly contains hidden data**.

---

## ⚠️ Supported Audio Format

Currently supported:

```
WAV (.wav)
```

Compressed formats like **MP3 or OGG** are not recommended because compression may destroy hidden data.

---

## 🧪 Example

Hide a message:

```
python3 spectrahide.py hide music.wav message.txt
```

Extract message:

```
python3 spectrahide.py extract music.wav output.txt
```

---

## 📜 License

This project is released under the **MIT License**.

You are free to use, modify, and distribute it.

---

## 👨‍💻 Author

Developed by **Cyber Specterz**

Cybersecurity Tools • Ethical Hacking • Research

---

## 🔐 Educational Purpose

This tool is created for **educational and research purposes only**.
Do not use it for illegal activities.

---

## ⭐ Support

If you like this project, consider giving it a **star ⭐ on GitHub**.
