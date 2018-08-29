import time
import sys
import random
import csv
import math


allAngles = [-37.5,-15,15,37.5,52.5,75,105,127.5,142.5,165,195,217.5,232.5,255,285,307.5,322.5,345,375]
anglenumer = [0,1,1,1,1,2,3,5,1,7,5,4,3,5,7,11]
angledenom = [1,6,4,3,2,3,4,6,1,6,4,3,2,3,4,6]

allstr = "["
for idx,i in enumerate(allAngles):
	istr = ""
	istr += '"'
	istr += str((int(math.cos(((i+allAngles[idx+1]*2.)/3)*3.14159/180)*200)))
	istr += ","
	istr += str(-(int(math.sin(((i+allAngles[idx+1]*2.)/3)*3.14159/180)*200)))
	istr += ' '
	istr += str((int(math.cos(((allAngles[idx+2]*2.+allAngles[idx+3])/3)*3.14159/180)*200)))
	istr += ","
	istr += str(-(int(math.sin(((allAngles[idx+2]*2.+allAngles[idx+3])/3)*3.14159/180)*200)))
	istr += '"'
	allstr += '{"points": '+istr
	allstr += ', "numer": '+str(anglenumer[idx])
	allstr += ', "denom": '+str(angledenom[idx])
	allstr += ', "needle": "'+str((int(math.cos(((allAngles[idx+1]+allAngles[idx+2]*1.)/2)*3.14159/180)*200)))+","+str(-(int(math.sin(((allAngles[idx+1]+allAngles[idx+2]*1.)/2)*3.14159/180)*200)))
	allstr += '"},'
	print(allstr)


	


