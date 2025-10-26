import network
import socket
import machine
import time

# === MOTOR SETUP ===
# Left motor
A1 = machine.Pin(10, machine.Pin.OUT)
A2 = machine.Pin(9, machine.Pin.OUT)
# Right motor
B1 = machine.Pin(8, machine.Pin.OUT)
B2 = machine.Pin(7, machine.Pin.OUT)

# === SERVO SETUP ===
arm = machine.PWM(machine.Pin(6))
arm.freq(50)
bucket = machine.PWM(machine.Pin(5))
bucket.freq(50)

# === HELPER FUNCTIONS ===
def stop():
    A1.off(); A2.off(); B1.off(); B2.off()

def forward():
    A1.on(); A2.off(); B1.on(); B2.off()

def backward():
    A1.off(); A2.on(); B1.off(); B2.on()

def left():
    A1.off(); A2.on(); B1.on(); B2.off()

def right():
    A1.on(); A2.off(); B1.off(); B2.on()

def move_arm(pos):
    duty = int((pos / 180 * 102) + 26)
    arm.duty(duty)

def move_bucket(pos):
    duty = int((pos / 180 * 102) + 26)
    bucket.duty(duty)

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
arm_pos = 90
bucket_pos = 90
move_arm(arm_pos)
move_bucket(bucket_pos)

try:
    while True:
        data = conn.recv(1024)
        if not data:
            continue
        cmd = data.decode('utf-8').strip().lower()
        print("Command:", cmd)

        if cmd == 'w':
            forward()
        elif cmd == 's':
            backward()
        elif cmd == 'a':
            left()
        elif cmd == 'd':
            right()
        elif cmd == 'x':
            stop()
        elif cmd == 'armup':
            arm_pos = min(arm_pos + 10, 180)
            move_arm(arm_pos)
        elif cmd == 'armdown':
            arm_pos = max(arm_pos - 10, 0)
            move_arm(arm_pos)
        elif cmd == 'bucketup':
            bucket_pos = min(bucket_pos + 10, 180)
            move_bucket(bucket_pos)
        elif cmd == 'bucketdown':
            bucket_pos = max(bucket_pos - 10, 0)
            move_bucket(bucket_pos)
        else:
            conn.send(b"Unknown command\n")

except Exception as e:
    print("Error:", e)
finally:
    conn.close()
    s.close()
    stop()
