"""
AI behavior and response logic for the PiDog AI JARVIS Assistant.
"""

BEHAVIOR_RESPONSES = {
    "greeting": "JARVIS online. PiDog systems are ready.",
    "patrol": "Starting patrol behavior and scanning the area.",
    "status": "All primary systems are online.",
    "sleep": "Entering low-power standby mode.",
    "alert": "Alert mode activated. Monitoring surroundings."
}


def get_behavior_response(behavior_name):
    behavior_name = behavior_name.lower().strip()

    return BEHAVIOR_RESPONSES.get(
        behavior_name,
        "Behavior not recognized. Awaiting a valid command."
    )


if __name__ == "__main__":
    behavior = input("Enter behavior mode: ")
    print(get_behavior_response(behavior))
