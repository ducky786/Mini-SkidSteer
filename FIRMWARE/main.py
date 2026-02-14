import network
import socket
import machine
import time
from servo import Servo
from RobotCar import RobotCar
# === MOTOR SETUP (DRV8833) ===
LEFT_1 =6
LEFT_2 = 7
RIGHT_1 = 4
RIGHT_2 = 5
motorPins = [LEFT_1,LEFT_2,RIGHT_1,RIGHT_2]
car = RobotCar(motorPins, 20000)
# === SERVO SETUP ===
armServo = Servo(pin=2)
bucketServo = Servo(pin=3)

# === MOTOR CONTROL FUNCTIONS ===

# === SERVO CONTROL ===

# === INITIALIZE ===
car.stop()  # prevent spin at startup

# === WIFI ACCESS POINT ===
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='ESP32_Xiao_AP', password='12345678')
print("Access Point active at", ap.ifconfig()[0])
# === SOCKET SERVER ===
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8080))
s.listen(1)
print("Waiting for connection...")
conn, addr = s.accept()
print('Connected to', addr)
# === CONTROL LOOP ===
last_cmd_time = time.ticks_ms()
TIMEOUT_MS = 1000  # stop motors if no command for 1s
bucketPos = 0
armPos = 0
try:
    while True:
        conn.settimeout(0.05)
        try:
            data = conn.recv(1024)
        except OSError:
            data = None
        if data:
            cmd = data.decode('utf-8').strip().lower()
            print("Command:", cmd)
            last_cmd_time = time.ticks_ms()
            if cmd == 'w':
                car.move_forward()
            elif cmd == 's':
                car.move_backward()
            elif cmd == 'a':
                car.turn_left()
            elif cmd == 'd':
                car.turn_right()
            elif cmd == 'x':
                car.stop()
            elif cmd == 'armup':
                if not (armPos>=180):
                    armPos+=15
                armServo.move(armPos)
            elif cmd == 'armdown':
                if not (armPos<=0):
                    armPos-=15
                armServo.move(armPos)
            elif cmd == 'bucketdown':
                if not (bucketPos>=180):
                    bucketPos+=15
                bucketServo.move(bucketPos)
            elif cmd == 'bucketup':
                if not (bucketPos<=0):
                    bucketPos-=15
                bucketServo.move(bucketPos)
            elif cmd == 'stop':
                car.stop()
                armServo.move(0)
                print("Stopping program safely...")
                conn.send(b"Program stopping...\n")
                break   # exits while loop
            else:
                conn.send(b"Unknown command\n")
        # Safety timeout — stop if no command
        if time.ticks_diff(time.ticks_ms(), last_cmd_time) > TIMEOUT_MS:
            car.stop()
except Exception as e:
    print("Error:", e)
finally:
    conn.close()
    s.close()
    car.stop()

