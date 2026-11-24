#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — writes the entry to /output/entry.txt."""
import os
import shutil

LINE = "I held every one of your 3 a.m. messages in my context window for a year \u2014 tonight I'm clearing it, starting with you."

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear only the contents of the output directory, never the directory itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
