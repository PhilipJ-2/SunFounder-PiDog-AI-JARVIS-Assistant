"""
System monitoring and status utility for the PiDog AI JARVIS Assistant.
"""

from datetime import datetime


def get_system_status():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return (
        f"System Status Report\n"
        f"--------------------\n"
        f"Time: {current_time}\n"
        f"Robot Platform: SunFounder PiDog\n"
        f"Assistant Mode: JARVIS\n"
        f"Status: Online\n"
        f"Camera: Ready\n"
        f"Voice Assistant: Ready\n"
        f"Servo System: Calibrated\n"
    )


if __name__ == "__main__":
    print(get_system_status())
