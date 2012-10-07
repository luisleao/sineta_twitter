#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import tweetstream
import serial


SERIAL_PORT = "/dev/tty.usbmodem1411"
SERIAL_SPEED = 9600
USER = "LOGIN"
PASSWORD = "SENHA"
WORDS = ["Brasil"] 



def main():
	ser = serial.Serial(SERIAL_PORT, SERIAL_SPEED)
	ser.write("2\n") #move the servo two times
	
	while True:
		with tweetstream.FilterStream(USER, PASSWORD, track=WORDS) as stream:
			print "CONECTADO!"			
			
			for tweet in stream:
				if ser.isOpen():
					ser.write("1\n")
				#print tweet
				print ">>> %s: %s"  % (tweet["user"]["screen_name"], tweet["text"])
				print ""
			print "\n\n\n"
		
		print "reconnecting..."
	print "END."

if __name__ == '__main__':
	main()


