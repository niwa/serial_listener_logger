#!/usr/bin/env python

# Load the libraries
import serial # Serial communications
import time # Timing utilities
from pathlib import Path

# Localtime or UTC date wrapper
def get_time(selector):
	if (selector=='local'):
		return time.localtime()
	else:
		return time.gmtime()

# Read the settings from the settings file
settings_file = open("./settings.txt")
# First the name of the instrument
dev_name = settings_file.readline().rstrip('\n')
# e.g. "/dev/ttyUSB0"
settings_line = settings_file.readline().rstrip('\n').split(',')
port = settings_line[0]
baud = eval(settings_line[1])
par  = settings_line[2]
byte = eval(settings_line[3])
stopbit = eval(settings_line[4])
ceol = settings_line[5]
if ceol == 'r':
	eol = b'\r'
elif ceol == 'nr':
	eol = b'\n\r'
else:
	eol = b'\n'
print(port)
# path for data files
# e.g. "/home/logger/datacpc3010/"
datapath = settings_file.readline().rstrip('\n') + dev_name
Path(datapath).mkdir(parents=True, exist_ok=True)
print(datapath)
fnamefmt = "%Y%m%d.tsv"
# Close the settings file
settings_file.close()
# Set the time constants
rec_time=get_time('UTC')
timestamp = time.strftime("%Y-%m-%d\t%H:%M:%S",rec_time)
# Previous file name
prev_file_name = datapath+time.strftime(fnamefmt,rec_time)
# Hacks to work with custom end of line
leneol = len(eol)
print(leneol)
bline = bytearray()
# Open the serial port and clean the I/O buffer
ser = serial.Serial()
ser.port = port
ser.baudrate = baud
ser.parity = par
ser.bytesize = byte
ser.stopbits = stopbit
ser.open()
ser.flushInput()
ser.flushOutput()
print("Port " + port + " flushed")
while True:
	# Get a line of data from the instrument
	while True:
		c = ser.read(1)
		bline += c
		if bline[-leneol:] == eol:
			break
	## Parse the data line
	line = bline.decode("utf-8").rstrip()
	#line = ser.readline()
	# Set the time for the record
	rec_time_s = int(time.time())
	rec_time=rec_time=get_time('UTC')
	timestamp = time.strftime("%Y-%m-%d\t%H:%M:%S",rec_time)
	file_line = timestamp+'\t'+line
	print(file_line)
	# Save it to the appropriate file
	current_file_name = datapath+time.strftime(fnamefmt,rec_time)
	current_file = open(current_file_name,"a")
	current_file.write(file_line+"\n")
	current_file.flush()
	current_file.close()
	line = ""
	bline = bytearray()
print('I\'m done')
