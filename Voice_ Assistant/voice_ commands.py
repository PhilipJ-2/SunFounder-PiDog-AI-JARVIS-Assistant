"""
Voice command handler for the PiDog AI JARVIS Assistant project.
"""

COMMANDS = {
    "sit": "Makes PiDog sit.",
    "stand": "Makes PiDog stand.",
    "walk": "Starts walking behavior.",
    "stop": "Stops current movement.",
    "patrol": "Starts patrol mode.",
    "status": "Reports system status."
}


def handle_command(command):
    command = command.lower().strip()

    if command in COMMANDS:
        return f"Command recognized: {command} - {COMMANDS[command]}"

    return "Command not recognized."


if __name__ == "__main__":
    user_command = input("Enter voice command: ")
    print(handle_command(user_command))
