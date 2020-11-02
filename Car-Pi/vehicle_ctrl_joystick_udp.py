import RPi.GPIO as GPIO
import socket
import sys, os
#import pygame, sys, time
#from pygame.locals import *


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


# Voreinstellungen für Host und Port
# akzeptiert Nachrichten von jedem Host auf dem angeg. Port
host = ""
port_x = 5005
port_y = 5006

# Groesse Empfangspuffer (begrenzt die empfangene Nachricht)
bufsize = 8192  # 8 kByte

# UDP-Socket oeffnen
addr_x = (host, port_x)
addr_y = (host, port_y)
UDPSock_x = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPSock_y = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


UDPSock_x.bind(addr_x)
UDPSock_y.bind(addr_y)

  
#print >>sys.stderr, "waiting for messages (port: " + str(port) + ") ..."

# Endlosschleife fuer Empfang, Abbruch durch Strg-C



while True:
    (data_x, addr_x) = UDPSock_x.recvfrom(bufsize)
    (data_y, addr_y) = UDPSock_y.recvfrom(bufsize)
    #print >>sys.stderr, 'received %s bytes from %s:%d' % (len(data), addr[0], addr[1])
    # weiter verarbeiten
    #print data
    print(data_x)
    print(data_y)
    
    print("."*25)
    
    data_x = int.from_bytes(data_x,byteorder='big')
    data_y = int.from_bytes(data_y,byteorder='big')
    # print (str(data_x) + " | " + str(data_y))
    
    key_up = False
    key_left = False
    key_down = False
    key_right = False
    
    print("-"*25)
    print("-"*25)
    
    data_x=int(str(data_x).split("[")[-1].split("]")[0])
    data_y=int(str(data_y).split("[")[-1].split("]")[0])
    
    print("."*25)
    key_up = data_y > 200
    print("UP: " + str(key_up))
    key_down = data_y < 100
    print("DOWN: " + str(key_down))
    key_left = data_x > 200
    print("LEFT: " + str(key_left))
    key_right = data_x < 100
    print("RIGHT: " + str(key_right))

    print("."*25)

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
