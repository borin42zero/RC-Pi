# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain
import time

"""
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
"""

# Import SPI library (for hardware SPI) and MCP3008 library.
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

CH_LIGHTSENS = 0
PIN_LED_BLUE = 26

GPIO.setup(PIN_LED_BLUE, GPIO.OUT)
GPIO.output(PIN_LED_BLUE, GPIO.LOW)

# Software SPI configuration:
# CLK  = 18
# MISO = 23
# MOSI = 24
# CS   = 25
# mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

"""
print('Reading MCP3008 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
print('-' * 57)
# Main program loop.
while True:
    # Read all the ADC channel values in a list.
    values = [0]*8
    for i in range(8):
        # The read_adc function will get the value of the specified channel (0-7).
        values[i] = mcp.read_adc(i)
    # Print the ADC values.
    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
    # Pause for half a second.
    time.sleep(0.5)
"""

while True:
    try:
        darkness = mcp.read_adc(CH_LIGHTSENS)
        
        if darkness > 850:
            GPIO.output(PIN_LED_BLUE, GPIO.HIGH)
        else:
            GPIO.output(PIN_LED_BLUE, GPIO.LOW)
    except KeyboardInterrupt:
        GPIO.output(PIN_LED_BLUE, GPIO.LOW)
        GPIO.cleanup()

