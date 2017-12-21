##############
## Script listens to serial port and writes contents into a file
##############
## requires pySerial to be installed 
#This code reads the data from the Arduino connected using a USB into the Raspberry Pi. The serial port is the usb port in this case 
import serial
import time
import pandas as pd


def getSerial():
	serial_port = '/dev/ttyACM0'                            # save the name of the serial port in serial_port
	baud_rate = 9600 #In arduino, Serial.begin(baud_rate)   #The rate at which the data will be transmitted
	write_to_file_path = "output.txt"                       #Name the file that you want to write the data into

	output_file = open(write_to_file_path, "w+")            #Opens up the text file for reading and writing
	ser = serial.Serial(serial_port, baud_rate)             #Opens up the usb port that the arduino is connected to at the given baud rate
	c = 0													#Counter
	t_end = time.time() + 30 # 30 seconds					#How long do you want to read for

	id_weight = {}											#Create an empty dictionary
	weight = 0												#Initialize weight to zero
	while time.time() < t_end:								#Loop until time end
		c += 1												#Increase counter by 1
		line = ser.readline()								#Reads a single line from the serial port
		line = line.encode("ascii") #ser.readline returns a binary, convert to string	
		if line[0] == 'W': #If the line begins with W
			weight = float(line[2:])  # read the weight
			#output_file.write("weight: " + line)
		if line[0] == 'I': #if line begins with I
			id = line[3:-2]   #read the id
			#output_file.write("id: " + line)
                        id_weight[id] = weight #Create key value pair in weight dictionary
	return id_weight    #Return the dictionary
