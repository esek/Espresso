#!/usr/bin/env python

def nfc_reader():
	import RPi.GPIO as GPIO
	import time

	timeout = 1800 # (s)
	counter = 0 #(s)
	from mfrc522 import SimpleMFRC522
	reader = SimpleMFRC522() #define object reader to read
	GPIO.cleanup() 
	value = 0

	#loop for reading nfc reader
	while counter < timeout:	
		try:
			id = reader.read() #read the nfc reader into variable "id"
			value = id	 
		except Exception as e:
			#prints exception
			print(e) 
		finally:
			time.sleep(1) #1s delay for timeout
			counter += 1 #increment counter for timeout
			if value != 0:	
				return value