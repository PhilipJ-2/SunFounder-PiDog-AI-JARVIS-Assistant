"""
JARVIS-style assistant workflow for the PiDog AI project.
"""

from voice_commands import handle_command


def jarvis_response(user_input):
    user_input = user_input.lower().strip()

    if "jarvis" in user_input:
        cleaned_command = user_input.replace("jarvis", "").strip()
        if cleaned_command:
            return handle_command(cleaned_command)
        return "JARVIS online. Awaiting command."

    return "Wake word not detected."


if __name__ == "__main__":
    while True:
        command = input("Say command: ")

        if command.lower() in ["exit", "quit"]:
            print("JARVIS shutting down.")
            break

        print(jarvis_response(command))
