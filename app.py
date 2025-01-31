import sys
import termios
import tty
import time
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C

# Initialize motors
motor_left = LargeMotor(OUTPUT_B)  # Port 2
motor_right = LargeMotor(OUTPUT_C)  # Port 3

# Function to get a single keypress
def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        sys.stdin.flush()
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key

# Instructions
print("Use W/A/S/D to control the EV3. Release the key to stop. Press Q to quit.")

try:
    while True:
        key = get_key()

        if key == "w":  # Move forward
            motor_left.on(50)
            motor_right.on(50)
            print("Moving forward")

        elif key == "s":  # Move backward
            motor_left.on(-50)
            motor_right.on(-50)
            print("Moving backward")

        elif key == "a":  # Turn left
            motor_left.on(-30)
            motor_right.on(30)
            print("Turning left")

        elif key == "d":  # Turn right
            motor_left.on(30)
            motor_right.on(-30)
            print("Turning right")

        elif key == "q":  # Quit program
            motor_left.off()
            motor_right.off()
            print("Exiting...")
            break

        else:
            # If no key is pressed, stop the motors
            motor_left.off()
            motor_right.off()
            print("Stopping")

        time.sleep(0.1)  # Small delay to prevent CPU overload

except KeyboardInterrupt:
    print("\nManual exit (Ctrl+C). Stopping motors...")
    motor_left.off()
    motor_right.off()
