"""
Autonomous patrol behavior script for the PiDog AI JARVIS Assistant.
"""

from time import sleep


def start_patrol():
    print("Starting patrol mode...")

    patrol_steps = [
        "Scanning environment",
        "Walking forward",
        "Checking left side",
        "Checking right side",
        "Returning to standby position"
    ]

    for step in patrol_steps:
        print(step)
        sleep(1)

    print("Patrol mode complete.")


if __name__ == "__main__":
    start_patrol()
