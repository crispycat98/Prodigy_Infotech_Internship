# Prodigy InfoTech - My work as a Cybersecurity Intern

This repo has all the work I did during my cybersecurity internship at Prodigy InfoTech. Each task is in its own folder with a standalone Python script. The focus across all five was practical security concepts such as encryption, password analysis, input capture, and network traffic inspection.

---

## What's Inside

| Task | Topic | File |
|------|-------|------|
| Task 01 | Caesar Cipher | `Task-01-Caesar-Cipher/caesar_cipher.py` |
| Task 02 | Image Encryption via Pixel Manipulation | `Task-02-Image-Encryption/image_encrypt.py` |
| Task 03 | Password Complexity Checker | `Task-03-Password-Checker/password_checker.py` |
| Task 04 | Keylogger | `Task-04-Keylogger/keylogger.py` |


---

## Task Breakdown

### Task 01-Caesar Cipher

A classic substitution cipher which shifts each letter in a message by a given number. Supports both encryption and decryption, handles upper and lower case separately, and leaves numbers and symbols untouched.

**Run it:**
```bash
python caesar_cipher.py
```

---

### Task 02-Image Encryption (Pixel Manipulation)

Encrypts any image by XOR-ing every pixel's RGB channels with a key value you provide. Since XOR is reversible, running the same script on the encrypted image with the same key gives you back the original. Works with `.png`, `.jpg`, and most common formats.

**Dependencies:**
```bash
pip install pillow
```

**Run it:**
```bash
python image_encrypt.py
```

---

### Task 03-Password Complexity Checker

Takes a password as input (hidden from terminal) and rates its strength across six criteria i.e. length, uppercase, lowercase, digits, special characters, and a bonus for passwords over 16 characters. Prints a strength label and tells you exactly what's missing.

**Run it:**
```bash
python password_checker.py
```

---

### Task 04-Keylogger

Records keystrokes and saves them to a log file with session timestamps. Buffers every 20 keys before writing so nothing gets lost if the process exits unexpectedly. Press `ESC` to stop the logger cleanly.

> Only use this on machines you own or have explicit permission to monitor. The script asks for confirmation before starting.

**Dependencies:**
```bash
pip install pynput
```

**Run it:**
```bash
python keylogger.py
```


---

## Setup

Clone the repo and install dependencies for whichever tasks you want to run:

```bash
git clone https://github.com/YOUR_USERNAME/Prodigy-InfoTech-Internship.git
cd Prodigy-InfoTech-Internship

pip install pillow pynput
```

Python 3.8 or above should work fine across all five scripts.

---

## Ethical Use

Task 04 deals with keystroke capture is something that can cause real harm if misused. Every script that touches this territory has a confirmation prompt built in and won't proceed without it. These were built purely for learning how such tools work under the hood, not for anything outside that scope.

---

## Internship

**Organization:** Prodigy InfoTech  
**Domain:** Cybersecurity  
**Duration:** April 2026
