#!usr/bin/python
import os
import time
import sys

print "Starting clock:"

while{1}:
	sys.stdout.write("\r" + str(time.strftime("%d/%m/%Y %H:%M:%S")))
	sys.stdout.flush()