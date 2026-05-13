"""
Camera streaming and vision utility for the PiDog AI JARVIS Assistant.
"""

from time import sleep


def start_camera_stream():
    print("Starting PiDog camera stream...")
    print("Camera resolution: 640x480")
    print("Frame rate: 30 FPS")

    for frame in range(1, 6):
        print(f"Processing frame {frame}...")
        sleep(0.5)

    print("Camera stream test complete.")


if __name__ == "__main__":
    start_camera_stream()
