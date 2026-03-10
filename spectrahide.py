#!/usr/bin/env python3

import os
import sys
import wave
from colorama import Fore, Style, init

init(autoreset=True)

SIGNATURE = b"SPECTRAHIDE_START"
END_MARK = b"SPECTRAHIDE_END"


def banner():
    print(Fore.CYAN + """
███████╗██████╗ ███████╗ ██████╗████████╗██████╗  █████╗ 
██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
███████╗██████╔╝█████╗  ██║        ██║   ██████╔╝███████║
╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██╔══██╗██╔══██║
███████║██║     ███████╗╚██████╗   ██║   ██║  ██║██║  ██║
╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝

        SpectraHide - Audio Steganography Tool
              Made by Cyber Specterz
""" + Style.RESET_ALL)


def hide_data(audio_file, text_file):
    if not os.path.exists(audio_file):
        print(Fore.RED + "Audio file not found")
        return

    if not os.path.exists(text_file):
        print(Fore.RED + "Text file not found")
        return

    with open(text_file, "rb") as f:
        secret = f.read()

    payload = SIGNATURE + secret + END_MARK

    with wave.open(audio_file, 'rb') as song:
        frames = bytearray(list(song.readframes(song.getnframes())))

    if len(payload) * 8 > len(frames):
        print(Fore.RED + "Audio file too small to hide data")
        return

    bit_index = 0

    for byte in payload:
        for i in range(8):
            bit = (byte >> (7 - i)) & 1
            frames[bit_index] = (frames[bit_index] & 254) | bit
            bit_index += 1

    with wave.open(audio_file, 'wb') as modified:
        modified.setparams(song.getparams())
        modified.writeframes(frames)

    print(Fore.GREEN + "Data successfully hidden inside audio")


def extract_data(audio_file, output_file):

    if not os.path.exists(audio_file):
        print(Fore.RED + "Audio file not found")
        return

    with wave.open(audio_file, 'rb') as song:
        frames = bytearray(list(song.readframes(song.getnframes())))

    extracted = bytearray()
    byte = 0
    count = 0

    for frame in frames:
        byte = (byte << 1) | (frame & 1)
        count += 1

        if count == 8:
            extracted.append(byte)
            byte = 0
            count = 0

    data = bytes(extracted)

    start = data.find(SIGNATURE)
    end = data.find(END_MARK)

    if start == -1 or end == -1:
        print(Fore.RED + "No hidden data found")
        return

    secret = data[start + len(SIGNATURE):end]

    with open(output_file, "wb") as f:
        f.write(secret)

    print(Fore.GREEN + "Hidden data extracted")


def help_menu():
    print("""
Usage:

Hide text file into audio
    python3 spectrahide.py hide audio.wav secret.txt

Extract hidden text
    python3 spectrahide.py extract audio.wav output.txt
""")


def main():
    banner()

    if len(sys.argv) < 2:
        help_menu()
        return

    mode = sys.argv[1]

    if mode == "hide":
        if len(sys.argv) != 4:
            help_menu()
            return
        hide_data(sys.argv[2], sys.argv[3])

    elif mode == "extract":
        if len(sys.argv) != 4:
            help_menu()
            return
        extract_data(sys.argv[2], sys.argv[3])

    else:
        help_menu()


if __name__ == "__main__":
    main()
