"""
Servo zeroing helper for PiDog-style robotics projects.
This script documents the neutral-position workflow used before tuning motion.
"""

import json
from pathlib import Path
from time import sleep

OFFSETS_FILE = Path("servo_offsets.json")


def load_offsets():
    if not OFFSETS_FILE.exists():
        print("servo_offsets.json not found. Using default zero offsets.")
        return {}

    with open(OFFSETS_FILE, "r") as file:
        return json.load(file)


def main():
    offsets = load_offsets()

    print("Starting servo zeroing check...")
    print("Loaded servo offsets:")
    for servo, offset in offsets.items():
        print(f"{servo}: {offset} degrees")

    print("\nSet each servo horn to its neutral/centered position.")
    print("Verify legs, head, and tail are aligned before running motion tests.")

    for step in range(3, 0, -1):
        print(f"Checking alignment in {step}...")
        sleep(1)

    print("Servo zeroing check complete.")


if __name__ == "__main__":
    main()
