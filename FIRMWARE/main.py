import board
import pwmio
import time

#---MOTOR SETUP---
left_in1 = pwmio.PWMOut(board.D1, frequency=1000)
left_in2 = pwmio.PWMOut(board.D2, frequency=1000)
right_in1 = pwmio.PWMOut(board.D3, frequency=1000)
right_in2 = pwmio.PWMOut(board.D4, frequency=1000)

def set_left_motor(forward=True, power=40000):
    if forward:
        left_in1.duty_cycle = power
        left_in2.duty_cycle = 0
    else:
        left_in1.duty_cycle = 0
        left_in2.duty_cycle = power

def set_right_motor(forward=True, power=40000):
    if forward:
        right_in1.duty_cycle = power
        right_in2.duty_cycle = 0
    else:
        right_in1.duty_cycle = 0
        right_in2.duty_cycle = power

def stop():
    left_in1.duty_cycle = 0
    left_in2.duty_cycle = 0
    right_in1.duty_cycle = 0
    right_in2.duty_cycle = 0

while True:
    cmd = input("Command: ").lower()

    if cmd == "w":
        set_left_motor(True)
        set_right_motor(True)
    elif cmd == "s":
        set_left_motor(False)
        set_right_motor(False)
    elif cmd == "a":
        set_left_motor(False)
        set_right_motor(True)
    elif cmd == "d":
        set_left_motor(True)
        set_right_motor(False)

    time.sleep(0.5)
    stop()
