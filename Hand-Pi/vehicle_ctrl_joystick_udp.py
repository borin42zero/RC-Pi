# !/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Voreinstellungen für Host und Port
host = "pi4.fritz.box"
port_x = 5005
port_y = 5006

# Die zu sendenden Daten
# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


# # UDP-Socket oeffnen
addr_x = (host, port_x)
addr_y = (host, port_y)
UDPSock_x = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPSock_y = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Nachricht senden
while 1:
    try:
        data_x = int(mcp.read_adc(0)/4)
        UDPSock_x.sendto(bytes([data_x]), addr_x)
        data_y = int(mcp.read_adc(1)/4)
        UDPSock_y.sendto(bytes([data_y]), addr_y)
        print(str(data_x) + " | " + str(data_y))
    except KeyboardInterrupt:
        UDPSock_x.close()
	UDPSock_y.close()

