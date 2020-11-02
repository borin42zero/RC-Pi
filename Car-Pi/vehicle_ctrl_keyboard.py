import RPi.GPIO as GPIO
import pygame, sys, time
from pygame.locals import *


GPIO.setmode(GPIO.BCM)

# EM1 --> Propulsion Motor
EM1_fwd = 12
EM1_bwd = 13

GPIO.setup(EM1_fwd, GPIO.OUT)
GPIO.setup(EM1_bwd, GPIO.OUT)

# EM2 --> Steering Motor
EM2_left = 18
EM2_right = 19

GPIO.setup(EM2_left, GPIO.OUT)
GPIO.setup(EM2_right, GPIO.OUT)

## 

"""
GPIO.output(EM1_fwd, GPIO.HIGH)
time.sleep(1)
GPIO.output(EM1_fwd, GPIO.LOW)
"""

pygame.init()
BLACK = (0,0,0)
WIDTH = 100
HEIGHT = 100
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

windowSurface.fill(BLACK)

key_up = False
key_left = False
key_down = False
key_right = False

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key in (K_w,K_UP):
                key_up = True
            if event.key in (K_a,K_LEFT):
                key_left = True
            if event.key in (K_s,K_DOWN):
                key_down = True
            if event.key in (K_d,K_RIGHT):
                key_right = True
            
        if event.type == KEYUP:
            if event.key in (K_w,K_UP):
                key_up = False
            if event.key in (K_a,K_LEFT):
                key_left = False
            if event.key in (K_s,K_DOWN):
                key_down = False
            if event.key in (K_d,K_RIGHT):
                key_right = False
        
        if event.type == QUIT:
            gpio.cleanup()
            pygame.quit()
            sys.exit()
    

    if key_up and key_left:
        print ("fwd/left")
        GPIO.output(EM1_fwd, GPIO.HIGH)
        GPIO.output(EM1_bwd, GPIO.LOW)
        GPIO.output(EM2_left, GPIO.HIGH)
        GPIO.output(EM2_right, GPIO.LOW)
    elif key_up and key_right:
        print ("fwd/right")
        GPIO.output(EM1_fwd, GPIO.HIGH)
        GPIO.output(EM1_bwd, GPIO.LOW)
        GPIO.output(EM2_left, GPIO.LOW)
        GPIO.output(EM2_right, GPIO.HIGH)
    elif key_down and key_left:
        print ("bwd/left")
        GPIO.output(EM1_fwd, GPIO.LOW)
        GPIO.output(EM1_bwd, GPIO.HIGH)
        GPIO.output(EM2_left, GPIO.HIGH)
        GPIO.output(EM2_right, GPIO.LOW)
    elif key_down and key_right:
        print ("bwd/right")
        GPIO.output(EM1_fwd, GPIO.LOW)
        GPIO.output(EM1_bwd, GPIO.HIGH)
        GPIO.output(EM2_left, GPIO.LOW)
        GPIO.output(EM2_right, GPIO.HIGH)
    elif key_up and key_down:
        print("brake")
        GPIO.output(EM1_fwd, GPIO.HIGH)
        GPIO.output(EM1_bwd, GPIO.HIGH)
        GPIO.output(EM2_left, GPIO.LOW)
        GPIO.output(EM2_right, GPIO.LOW)
    elif key_up:
        print ("fwd")
        GPIO.output(EM1_fwd, GPIO.HIGH)
        GPIO.output(EM1_bwd, GPIO.LOW)
        GPIO.output(EM2_left, GPIO.LOW)
        GPIO.output(EM2_right, GPIO.LOW)
    elif key_down:
        print ("bwd")
        GPIO.output(EM1_fwd, GPIO.LOW)
        GPIO.output(EM1_bwd, GPIO.HIGH)
        GPIO.output(EM2_left, GPIO.LOW)
        GPIO.output(EM2_right, GPIO.LOW)
    elif key_left:
        print ("left")
        GPIO.output(EM1_fwd, GPIO.LOW)
        GPIO.output(EM1_bwd, GPIO.LOW)
        GPIO.output(EM2_left, GPIO.HIGH)
        GPIO.output(EM2_right, GPIO.LOW)
    elif key_right:
        print ("right")
        GPIO.output(EM1_fwd, GPIO.LOW)
        GPIO.output(EM1_bwd, GPIO.LOW)
        GPIO.output(EM2_left, GPIO.LOW)
        GPIO.output(EM2_right, GPIO.HIGH)
    else:
        print ("idle")
        GPIO.output(EM1_fwd, GPIO.LOW)
        GPIO.output(EM1_bwd, GPIO.LOW)
        GPIO.output(EM2_left, GPIO.LOW)
        GPIO.output(EM2_right, GPIO.LOW)

gpio.cleanup()
