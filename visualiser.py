import math

print "   4|       "
print "    |      "
print "   3|       *A(2,3)"
print "    |    "
print "   2|   "
print "    |  "
print "   1| "
print "____|__________________________________"
print "    |   1   2   3   4   5   6   7"

print "Please input a valid point within the table to display it."
print "X:"
x = input()
print "Y:"
y = input()
if(x>=0 and x<=7 and x!=0):
	if(y>=0 and y<=4 and y!=0):
		#Valid inputs, check rounding
		if(round(x,0)==float(x)):
			#X is okay
			print ("Confirmed validity of X: " + str(x))
			print ("Using X: " + str(x))
		else:
			x = round(x,1)
			print ("Rounded X to: " + str(x))
			#Rounded, we only accept .5 accuracy. Sorry.
			tmp = str(x)
			tmp = tmp[::-1]
			if(tmp[0]=="5"):
				#Okay
				print "Using X: " + str(x)
			else:
				tmp = float(tmp[0])
				if(tmp>5):
					x = math.ceil(x)
				else:
					x = math.floor(x)
			print ("Using X: " + str(x))
		##Now with Y
		
		if(round(y,0)==float(y)):
			#Y is okay
			print ("Confirmed validity of Y: " + str(y))
			print ("Using Y: " + str(y))
		else:
			y = round(y,1)
			print ("Rounded Y to: " + str(y))
			#Rounded, we only accept .5 accuracy. Sorry.
			tmp = str(y)
			tmp = tmp[::-1]
			if(tmp[0]=="5"):
				#Okay
				print "Using Y: " + str(y)
			else:
				tmp = float(tmp[0])
				if(tmp>5):
					y = math.ceil(y)
				else:
					y = math.floor(y)
			print ("Using Y: " + str(y))
		if(x==0 or y==0):
			print ("Well.. We do not accept 0 in either X or Y. We will show you the point A(1,1) instead.")
			x = 1
			y = 1
			
		#Finally. Good numbers!
		print ("Program loaded this point: A(" + str(x) + "," + str(y) + ")")
		#Visualise this in terminal. Piece of cake
		
		#Y: 11 rows
		#X: 28 columns (Valid, from (0,0))
		yr = [666,4,3.5,3,2.5,2,1.5,1,0.5,-0.5,-1]
		calculatedVisualY = yr[int(y)]
		for i in range(1,10):
			if(y == yr[i]):
				calculatedVisualY = i
		
		calculatedVisualX = 4.0 * x
		calculatedVisualX = int(calculatedVisualX)
		#Now we need to interpret the result. Visually. F*ck. First goes Y.
		yLines = ["DaKnOb made this, bitches", "   4|", "    |","   3|","    |", "   2|","    |", "   1|", "    |"]
		
		if(calculatedVisualY!=1):
			for q in range(1,calculatedVisualY):
				print (yLines[q])
			#Print X
			compiled = yLines[calculatedVisualY]
			for n in range(1,calculatedVisualX):
				compiled = compiled + " "
			compiled = compiled + "*A(" + str(x) + "," + str(y) + ")"
			print (compiled)
			#EOF Print X
			for q in range(calculatedVisualY+1,9):
				print(yLines[q])
		else:
			#Print X
			compiled = yLines[calculatedVisualY]
			for n in range(1,calculatedVisualX):
				compiled = compiled + " "
			compiled = compiled + "*A(" + str(x) + "," + str(y) + ")"
			print (compiled)
			#EOF Print X
			for q in range(2,9):
				print (yLines[q])
				
		print "____|__________________________________"
		print "    |   1   2   3   4   5   6   7"
	
	
	else:
		print "Y is out of range! (0,4]"
else:
	print "X is out of range! (0,7]"