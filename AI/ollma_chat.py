"""
Local AI chatbot interaction script for the PiDog AI JARVIS Assistant.

This portfolio-safe example shows the structure for connecting a PiDog
robotics project to a local Ollama-style AI assistant workflow.
"""

import json
from pathlib import Path

CONFIG_FILE = Path("ai_config.json")


def load_config():
    if not CONFIG_FILE.exists():
        return {
            "assistant_name": "JARVIS",
            "default_model": "llama3",
            "response_style": "short"
        }

    with open(CONFIG_FILE, "r") as file:
        return json.load(file)


def generate_ai_response(user_prompt):
    config = load_config()
    assistant_name = config.get("assistant_name", "JARVIS")
    model = config.get("default_model", "llama3")

    return (
        f"{assistant_name} using {model}: "
        f"I received your command: '{user_prompt}'. "
        f"Processing robotic assistant response."
    )


if __name__ == "__main__":
    while True:
        prompt = input("Ask JARVIS: ")

        if prompt.lower() in ["exit", "quit"]:
            print("JARVIS AI session ended.")
            break

        print(generate_ai_response(prompt))
