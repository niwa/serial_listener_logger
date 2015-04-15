#!/usr/bin/env python

# Load the libraries
import serial # Serial communications
import time # Timing utilities
import subprocess # Shell utilities ... compressing data files

# Set the time constants
rec_time=time.localtime()
timestamp = time.strftime("%Y-%m-%d %H:%M:%S",rec_time)
# Read the settings from the settings file
settings_file = open("./settings.txt")
# e.g. "/dev/ttyUSB0"
settings_line = settings_file.readline().rstrip('\n').split(',')
port = settings_line[0]
baud = eval(settings_line[1])
par  = settings_line[2]
byte = eval(settings_line[3])
ceol = settings_line[4]
if ceol == 'r':
	eol = b'\r'
elif ceol == 'nr':
	eol = b'\n\r'
else:
	eol = b'\n'
print(port)
# path for data files
# e.g. "/home/logger/datacpc3010/"
datapath = settings_file.readline().rstrip('\n')
print(datapath)
prev_file_name = datapath+time.strftime("%Y-%m-%d.txt",rec_time)
# Read the compressing flag
flags = settings_file.readline().rstrip().split(',')
# Close the settings file
settings_file.close()
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
ser.open()
ser.flushInput()
ser.flushOutput()
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
	rec_time=time.localtime()
	timestamp = time.strftime("%Y-%m-%d %H:%M:%S",rec_time)
	file_line = timestamp+','+line
	print(file_line)
	# Save it to the appropriate file
	current_file_name = datapath+time.strftime("%Y-%m-%d.txt",rec_time)
	current_file = open(current_file_name,"a")
	current_file.write(file_line+"\n")
	current_file.flush()
	current_file.close()
	line = ""
	bline = bytearray()
	# Compress data if required
	# Is it the last minute of the day?
	if flags[0] == 1:
		if current_file_name != prev_file_name:
			subprocess.call(["gzip",prev_file_name])
			prev_file_name = current_file_name	
print('I\'m done')
