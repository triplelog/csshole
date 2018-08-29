import time
import sys
import random
import csv
import math


def writecsv(parr, filen):
        with open(filen, 'ab') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for i in range(0,len(parr)):
                        try:
                                spamwriter.writerow(parr[i])
                        except:
                                print parr[i], i


def readcsv(filen):
        allgamesa  =[]
        with open(filen, 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in spamreader:
                        allgamesa.append(row)
        return allgamesa

alldata = readcsv('top100us.csv')
allcities = []
somecities = alldata[1:11]
for i in somecities:
	this_object = {"name":"","left":0,"top":0,"distances":[]}
	this_object['name']=i[0].replace(' ','_')
	this_object['left']=int(585+(float(i[5])+96.7)*((310-585)/(-118+96.7)))
	this_object['top']=int(-80+(float(i[4])-25.78)*((-436+80)/(23.22)))
	for ii in somecities:
		this_object['distances'].append(int(((int(-80+(float(i[4])-25.78)*((-436+80)/(23.22)))-int(-80+(float(ii[4])-25.78)*((-436+80)/(23.22))))**2+(int(585+(float(i[5])+96.7)*((310-585)/(-118+96.7)))-int(585+(float(ii[5])+96.7)*((310-585)/(-118+96.7))))**2)**.5))
	allcities.append(this_object)
print(allcities)





