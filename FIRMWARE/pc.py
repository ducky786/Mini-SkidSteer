import pygame
import socket
import sys
import time

# === ESP32 CONNECTION SETTINGS ===
ESP32_IP = "192.168.4.1"   # Default IP when connected to ESP32 AP
ESP32_PORT = 8080

# === CONNECT TO ESP32 ===
print("Connecting to ESP32...")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((ESP32_IP, ESP32_PORT))
    print(f"Connected to ESP32 at {ESP32_IP}:{ESP32_PORT}")
except Exception as e:
    print("Connection failed:", e)
    sys.exit()

# === INITIALIZE PYGAME ===
pygame.init()
pygame.joystick.init()

# Detect controller
if pygame.joystick.get_count() == 0:
    print("No controller detected! Plug one in and try again.")
    sys.exit()

controller = pygame.joystick.Joystick(0)
controller.init()
print("Controller detected:", controller.get_name())

# === HELPER FUNCTION ===
def send_command(cmd):
    """Send a command string to the ESP32."""
    try:
        sock.send(cmd.encode())
        print("Sent:", cmd)
    except Exception as e:
        print("Lost connection:", e)
        pygame.quit()
        sys.exit()

# === MAIN LOOP ===
print("\n--- Controller active ---")
print("Use left stick to move, buttons to control arm & bucket\n")

running = True
last_cmd = ""

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # === LEFT STICK for driving ===
    x_axis = controller.get_axis(0)  # left/right
    y_axis = controller.get_axis(1)  # forward/backward

    if y_axis < -0.5:
        cmd = "w"     # forward
    elif y_axis > 0.5:
        cmd = "s"     # backward
    elif x_axis < -0.5:
        cmd = "a"     # left
    elif x_axis > 0.5:
        cmd = "d"     # right
    else:
        cmd = "x"     # stop

    # Only send when command changes (to reduce network spam)
    if cmd != last_cmd:
        send_command(cmd)
        last_cmd = cmd

    # === BUTTONS for arm/bucket ===
    # Adjust these if your controller has different layout
    if controller.get_button(0):  # A
        send_command("armup")
        time.sleep(0.2)
    if controller.get_button(1):  # B
        send_command("armdown")
        time.sleep(0.2)
    if controller.get_button(2):  # X
        send_command("bucketup")
        time.sleep(0.2)
    if controller.get_button(3):  # Y
        send_command("bucketdown")
        time.sleep(0.2)

    time.sleep(0.05)

# === CLEANUP ===
pygame.quit()
sock.close()
print("Disconnected.")
