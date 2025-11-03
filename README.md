# Windows 0.3 Python Simulator
## Description

Windows 0.3 is a fun Python-based simulation of a command-line operating system.
It lets users “boot” into a minimal OS environment, type commands, play mini-games, check RAM usage, run a basic AI chatbot, and explore a fake internet—all in the console.

It’s designed for learning Python, experimenting with loops, conditionals, and functions, while having a bit of chaotic fun.

## Features

Boot PC simulation (RAM or storage mode)

Fake command-line interface with commands: help, winver, msinfo32, clock.exe, flip a coin, and more

Mini-games like guessing numbers

Basic calculators (+, -, *, /)

AI chatbot (ekdmp) with keyword detection and personality responses

Fake LAN/Internet browser with 3 URLs

Warnings for high RAM usage and BSOD-like events

Fun ASCII art boot screen

## Installation

### Clone the repo
git clone https://github.com/CoolGuy158Wwindows0.3.git

cd Windows0.3

### Run the Python script
python "windows 0.3.py"
### or on some systems
py "windows 0.3.py"

### Optional: make it a .exe file
pip install pyinstaller
pyinstaller --onefile --console "windows 0.3.py"
# The exe will be in dist/windows0.3.exe

### Usage

Type boot to start the simulation.

Choose between RAM or storage mode.

Use commands like help to explore what Windows 0.3 can do.

Type exit to quit certain commands or shut off to close the OS simulation.

Commands Overview

help – Lists all available commands

run – Simulates running a floppy disk

ram usage – Displays current RAM usage

msinfo32 – Shows hardware info

winver – Displays software info

flip a coin – Simulates a coin flip

clock.exe – Shows current time

calculatora.exe, calculators.exe, calculatorm.exe, calculatord.exe – Basic arithmetic

game.exe – Number guessing game

ekdmp – Early keyword detection AI chatbot

And more… type help in the program for full list

## Notes

RAM usage increases as commands are executed. Warnings are displayed when nearing full usage.

Certain commands are intentionally destructive or limited for fun, like del_sys32.

AI chatbot responses are randomized and context-sensitive.

## License

This project is for educational purposes. Feel free to modify and explore the code.

