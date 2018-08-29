import json
import csv

def readcsv(filen):
		allgamesa  =[]
		with open(filen, 'rb') as csvfile:
				spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
				for row in spamreader:
						allgamesa.append(row)
		return allgamesa

allcongress = readcsv('legislators-current.csv')
allreps = []
allstates = []
for i in allcongress:
	if i[4] == 'rep' and i[5] != 'GU' and i[5] != 'DC' and i[5] != 'MP' and i[5] != 'VI' and i[5] != 'AS' and i[5] != 'PR' and i[5] != 'AK' and i[5] != 'HI':
		allreps.append([i[0],i[1],i[5],i[6],i[8]])
		instates = False
		for ii in allstates:
			if ii['name'] == i[5]:
				instates = True
				ii['ncds'] += 1
				if i[8] == 'Republican':
					ii['lastcd'].append(1)
				elif i[8] == 'Democrat':
					ii['lastcd'].append(0)
				else:
					ii['lastcd'].append(2)
		if not instates:
			if i[8] == 'Republican':
				allstates.append({'name':i[5],'ncds':1,'lastcd':[1]})
			elif i[8] == 'Democrat':
				allstates.append({'name':i[5],'ncds':1,'lastcd':[0]})
			else:
				allstates.append({'name':i[5],'ncds':1,'lastcd':[2]})
				


xstretch = 90
ystretch = 100
states = allstates
allbounds = [10000,10000,-10000,-10000]
for state in states:
	f = open('states/'+state['name']+'/shape.geojson','rb')
	alldata = json.loads(f.readlines()[0])
	geotype = alldata['type']
	if geotype != 'MultiPolygon':
		print(soto)
	#print(len(alldata['coordinates']))
	#myPolygons = alldata['coordinates'][0]
	state['cds'] = []
	state['ev'] = state['ncds']+2
	state['polygons'] = []
	lastx = 0
	lasty = 0
	for iiii in alldata['coordinates']:
		for iii in iiii:
			iStr = ""
			for ii in range(0,len(iii)):
				if int(xstretch*iii[ii][0]) != lastx or -1*int(ystretch*iii[ii][1]) != lasty:
					iStr += str(int(xstretch*iii[ii][0]))
					iStr += ','
					iStr += str(-1*int(ystretch*iii[ii][1]))
					iStr += ' '
					lastx = int(xstretch*iii[ii][0])
					lasty = -1*int(ystretch*iii[ii][1])
			state['polygons'].append(iStr)
	minX = 100000
	maxX = -100000
	minY = 100000
	maxY = -100000
	for i in range(1,state['ncds']+1):
		if state['ncds'] == 1:
			f = open('cds/2016/'+state['name']+'-0/shape.geojson','rb')
		else:
			f = open('cds/2016/'+state['name']+'-'+str(i)+'/shape.geojson','rb')
		alldata = json.loads(f.readlines()[0])
		geotype = alldata['geometry']['type']
		if geotype != 'MultiPolygon':
			print(soto)
		#print(len(alldata['geometry']['coordinates']))
		#myPolygons = alldata['geometry']['coordinates'][0]
	
		this_state = {'ev':0}
		this_state['last'] = state['lastcd'][i-1]
		this_state['name'] = state['name']+'-'+str(i)
		this_state['polygons'] = []
		lastx = 0
		lasty = 0
		for iiii in alldata['geometry']['coordinates']:
			for iii in iiii:
				iStr = ""
				for ii in range(0,len(iii)):
					if int(xstretch*iii[ii][0]) != lastx or -1*int(ystretch*iii[ii][1]) != lasty:
						iStr += str(int(xstretch*iii[ii][0]))
						iStr += ','
						iStr += str(-1*int(ystretch*iii[ii][1]))
						iStr += ' '
						if -1*int(ystretch*iii[ii][1]) > maxY:
							maxY = -1*int(ystretch*iii[ii][1])
						if int(xstretch*iii[ii][0]) > maxX:
							maxX = int(xstretch*iii[ii][0])
						if -1*int(ystretch*iii[ii][1]) < minY:
							minY = -1*int(ystretch*iii[ii][1])
						if int(xstretch*iii[ii][0]) < minX:
							minX = int(xstretch*iii[ii][0])
						lastx = int(xstretch*iii[ii][0])
						lasty = -1*int(ystretch*iii[ii][1])
				this_state['polygons'].append(iStr)
		state['cds'].append(this_state)
	state['bounds']=str(minX-1)+' '+str(minY-1)+' '+str(maxX-minX+2)+' '+str(maxY-minY+2)
	if minX < allbounds[0]:
		allbounds[0] = minX
	if minY < allbounds[1]:
		allbounds[1] = minY
	if maxX > allbounds[2]:
		allbounds[2] = maxX
	if maxY > allbounds[3]:
		allbounds[3] = maxY	
	print(state['name'],state['bounds'])

f = open('cdmap.md','w')
startStr = "---\ntitle: 'Electoral Map - Just CSS/HTML'\ndate: 2018-06-20\ntags: []\ndraft: false\ntype: 'games'\n"
f.write(startStr+'states: '+json.dumps(states)+'\nbounds: "'+str(allbounds[0]-1)+' '+str(allbounds[1]-1)+' '+str(allbounds[2]-allbounds[0]+2)+' '+str(allbounds[3]-allbounds[1]+2)+'"\n'+"layout: 'congdistrictmap'\n---")
f.close()

	