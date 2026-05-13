"""
Main control script for the PiDog AI JARVIS Assistant project.
"""

from patrol_mode import start_patrol
from system_status import get_system_status


def main():
    print("PiDog AI JARVIS Assistant")
    print("-------------------------")
    print("1. System Status")
    print("2. Start Patrol Mode")
    print("3. Exit")

    while True:
        choice = input("\nSelect option: ")

        if choice == "1":
            print(get_system_status())

        elif choice == "2":
            start_patrol()

        elif choice == "3":
            print("Shutting down PiDog system.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
