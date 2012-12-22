import sys
import time

def updateScreen(dots_int):
	q = "."
	for i in range(1, dots_int):
		q = q + "."
	sys.stdout.write("\r" + q + "   ")
	sys.stdout.flush()

f = 1
while(1):
	updateScreen(f)
	f = f + 1
	if(f==4):
		f = 1
	time.sleep(0.5)