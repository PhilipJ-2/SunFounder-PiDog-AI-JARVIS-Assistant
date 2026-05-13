"""
Basic calibration workflow for a PiDog-style robotic dog.

This script is portfolio-safe documentation code. It explains the calibration
process without requiring direct access to the physical robot.
"""

from time import sleep


SERVOS = [
    "front_left_hip",
    "front_left_knee",
    "front_right_hip",
    "front_right_knee",
    "rear_left_hip",
    "rear_left_knee",
    "rear_right_hip",
    "rear_right_knee",
    "head_pan",
    "head_tilt",
    "tail",
]


def run_calibration_check():
    print("PiDog Basic Calibration Workflow")
    print("--------------------------------")

    for servo in SERVOS:
        print(f"Checking neutral alignment for: {servo}")
        sleep(0.3)

    print("\nCalibration checklist:")
    print("1. Confirm each servo is centered.")
    print("2. Adjust servo horn position if needed.")
    print("3. Update servo_offsets.json with correction values.")
    print("4. Re-run movement test after tuning.")
    print("5. Confirm walking motion is balanced and stable.")

    print("\nBasic calibration workflow complete.")


if __name__ == "__main__":
    run_calibration_check()
