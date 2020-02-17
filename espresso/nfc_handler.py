#!/usr/bin/env python

#Fungerande kod <3

import RPi.GPIO as GPIO
import time

#Variables n stuff
i = 0
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()
GPIO.cleanup()
values = {}

#loop
while True:
		
	print(i)
	try:
		id, text = reader.read()
		print(id)
		values[i] = id
	#	print(text)
	except Exception as e:
		print(e)
	finally:
		print("cleanup")
		#GPIO.cleanup()
	time.sleep(1)
	print("loop")
	print(values)
	i += 1
