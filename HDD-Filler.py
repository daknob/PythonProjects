#!usr/bin/python
import os

os.system("mkdir ~/Desktop/hdd")
filepath = "~/Desktop/"
filename = "bytes.deleteme"

f = open(filepath+filename, "w+")
f.write("")
f.close()

v = 0

print "Starting..."

while {1}:
	try:
		openfile = open(filepath+filename, "a+")
		openfile.write("1")
		openfile.close()
		if (v>1000000000): #Not precise enough, but it works okay
			s = v / 1000000000
			print "HDD Covered: " + str(s) + " GB"
		elif(v>1000000):
			s = v / 1000000
			print "HDD Covered: " + str(s) + " MB"
		elif(v>1000):
			s = v / 1000
			print "HDD Covered: " + str(s) + " KB"
		else:
			print "HDD Covered: " + str(v) + " Bytes"
		v = v + 1
	except:
		print "Your HDD is full! Deleting written data..." #Could be permission error as well, but never mind :P
		os.system("rm -vfR " + filepath + filename)
		print "System has unlinked the appropriate files."
		break