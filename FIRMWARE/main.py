import pygame
import socket
import time

ESP_IP = "192.168.4.1"
PORT = 8080

# === CONNECT TO ESP32 ===
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ESP_IP, PORT))
print("Connected to ESP32 at", ESP_IP)

# === INIT CONTROLLER ===
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    raise Exception("No controller detected!")

joystick = pygame.joystick.Joystick(0)
joystick.init()
print("Using controller:", joystick.get_name())

last_cmd = None
arm_pos = 90
bucket_pos = 90

def send_cmd(cmd):
    global last_cmd
    if cmd != last_cmd:  # avoid flooding same command
        sock.sendall(cmd.encode())
        last_cmd = cmd
        print("Sent:", cmd)

try:
    while True:
        pygame.event.pump()

        # LEFT stick: driving
        x_axis = joystick.get_axis(0)
        y_axis = joystick.get_axis(1)

        if y_axis < -0.5:
            send_cmd('w')
        elif y_axis > 0.5:
            send_cmd('s')
        elif x_axis < -0.5:
            send_cmd('a')
        elif x_axis > 0.5:
            send_cmd('d')
        else:
            send_cmd('x')

        # A/B/X/Y buttons: arm + bucket
        if joystick.get_button(0):  # A
            send_cmd('armdown')
        elif joystick.get_button(1):  # B
            send_cmd('armup')
        elif joystick.get_button(2):  # X
            send_cmd('bucketdown')
        elif joystick.get_button(3):  # Y
            send_cmd('bucketup')

        time.sleep(0.1)

except KeyboardInterrupt:
    send_cmd('x')
    print("\nExiting...")
finally:
    sock.close()
    pygame.quit()
