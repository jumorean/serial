import serial
import serial.tools.list_ports
import time
import matplotlib.pyplot as plt
port_list = list(serial.tools.list_ports.comports())
print(len(port_list))
for s in port_list:
	print(s)
ser = serial.Serial("COM3", 115200)
# while(True):
# 	ch = ser.read()
# 	print(ch.decode(), end='')
ser.close()

