"""
Object tracking and vision behavior script for the PiDog AI JARVIS Assistant.
"""

from time import sleep


def track_object(target="person"):
    print(f"JARVIS vision system searching for: {target}")

    tracking_steps = [
        "Initializing camera",
        "Scanning frame",
        "Detecting movement",
        "Locking onto target",
        "Tracking target position"
    ]

    for step in tracking_steps:
        print(step)
        sleep(0.75)

    print(f"Object tracking complete for target: {target}")


if __name__ == "__main__":
    target_object = input("Enter target object: ")
    track_object(target_object)
