import json
import csv

def readcsv(filen):
		allgamesa  =[]
		with open(filen, 'rb') as csvfile:
				spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
				for row in spamreader:
						allgamesa.append(row)
		return allgamesa

statenames = [['AK', 'ALASKA', 'Alaska', 3, 1],['HI', 'HAWAII', 'Hawaii', 4, 0],['AL', 'ALABAMA', 'Alabama', 9, 1],['AZ', 'ARIZONA', 'Arizona', 11, 1],['AR', 'ARKANSAS', 'Arkansas', 6, 1],['CA', 'CALIFORNIA', 'California', 55, 0],['CO', 'COLORADO', 'Colorado', 9, 0],['CT', 'CONNECTICUT', 'Connecticut', 7, 0],['DE', 'DELAWARE', 'Delaware', 3, 0],['DC', 'DISTRICT OF COLUMBIA', 'District of Columbia', 3, 0],['FL', 'FLORIDA', 'Florida', 29, 1],['GA', 'GEORGIA', 'Georgia', 16, 1],['ID', 'IDAHO', 'Idaho', 4, 1],['IL', 'ILLINOIS', 'Illinois', 20, 0],['IN', 'INDIANA', 'Indiana', 11, 1],['IA', 'IOWA', 'Iowa', 6, 1],['KS', 'KANSAS', 'Kansas', 6, 1],['KY', 'KENTUCKY', 'Kentucky', 8, 1],['LA', 'LOUISIANA', 'Louisiana', 8, 1],['ME', 'MAINE', 'Maine', 4, 0],['MD', 'MARYLAND', 'Maryland', 10, 0],['MA', 'MASSACHUSETTS', 'Massachusetts', 11, 0],['MI', 'MICHIGAN', 'Michigan', 16, 1],['MN', 'MINNESOTA', 'Minnesota', 10, 0],['MS', 'MISSISSIPPI', 'Mississippi', 6, 1],['MO', 'MISSOURI', 'Missouri', 10, 1],['MT', 'MONTANA', 'Montana', 3, 1],['NE', 'NEBRASKA', 'Nebraska', 5, 1],['NV', 'NEVADA', 'Nevada', 6, 0],['NH', 'NEW HAMPSHIRE', 'New Hampshire', 4, 0],['NJ', 'NEW JERSEY', 'New Jersey', 14, 0],['NM', 'NEW MEXICO', 'New Mexico', 5, 0],['NY', 'NEW YORK', 'New York', 29, 0],['NC', 'NORTH CAROLINA', 'North Carolina', 15, 1],['ND', 'NORTH DAKOTA', 'North Dakota', 3, 1],['OH', 'OHIO', 'Ohio', 18, 1],['OK', 'OKLAHOMA', 'Oklahoma', 7, 1],['OR', 'OREGON', 'Oregon', 7, 0],['PA', 'PENNSYLVANIA', 'Pennsylvania', 20, 1],['RI', 'RHODE ISLAND', 'Rhode Island', 4, 0],['SC', 'SOUTH CAROLINA', 'South Carolina', 9, 1],['SD', 'SOUTH DAKOTA', 'South Dakota', 3, 1],['TN', 'TENNESSEE', 'Tennessee', 11, 1],['TX', 'TEXAS', 'Texas', 38, 1],['UT', 'UTAH', 'Utah', 6, 1],['VT', 'VERMONT', 'Vermont', 3, 0],['VA', 'VIRGINIA', 'Virginia', 13, 0],['WA', 'WASHINGTON', 'Washington', 12, 0],['WV', 'WEST VIRGINIA', 'West Virginia', 5, 1],['WI', 'WISCONSIN', 'Wisconsin', 10, 1],['WY', 'WYOMING', 'Wyoming', 3, 1]]
allresultshouse14 = readcsv('resultshouse14.csv')
allresultshouse16 = readcsv('resultshouse16.csv')
allresults = readcsv('resultsbydistrict12-16.csv')
allmoney = readcsv('money18.csv')
allcrystal = readcsv('crystalball.csv')
allcook = readcsv('cookpvi.csv')

#Create list of states with number of districts
allstates = []
for i in allresults[1:]:
	instates = False
	for ii in allstates:
		if ii['name'] == i[0][:2]:
			instates = True
			ii['ncds'] += 1
	if not instates:
		allstates.append({'name':i[0][:2],'ncds':1})

#Create list of all districts
allreps = []
for i in allresults[1:]:
	this_district = {}
	if i[0][3:] == 'AL':
		this_district['name']=i[0][:2]+'-1'
	else:
		this_district['name']=i[0][:2]+'-'+str(int(i[0][3:]))
	this_district['pres08d']=i[7]
	this_district['pres08r']=i[8]
	this_district['pres12d']=i[5]
	this_district['pres12r']=i[6]
	this_district['pres16d']=i[3]
	this_district['pres16r']=i[4]
	this_district['currentrep']=i[1]
	this_district['dems']=[]
	this_district['reps']=[]
	this_district['perc14r']='0'
	this_district['perc14d']='0'
	this_district['perc16r']='0'
	this_district['perc16d']='0'
	allreps.append(this_district)

for i in allcook[1:]:
	for ii in statenames:
		i[0] = i[0].replace(ii[2],ii[0])
	i[0] = i[0].replace('West VA','WV')
	i[0] = i[0].replace(' ','-')
	i[0] = i[0].replace('-AL','-1')
	for ii in allreps:
		if ii['name']==i[0]:
			ii['cookpvi']=i[1]

for i in allcrystal[1:]:
	i[2] = i[2].replace('AL','1')
	for ii in allreps:
		if ii['name']==i[1]+'-'+i[2]:
			ii['crystal']=i[7]
			if i[7] == '1':
				ii['crystalstring']='Solid D'
			elif i[7] == '2':
				ii['crystalstring']='Likely D'
			elif i[7] == '3':
				ii['crystalstring']='Leans D'
			elif i[7] == '4':
				ii['crystalstring']='Tossup'
			elif i[7] == '5':
				ii['crystalstring']='Leans R'
			elif i[7] == '6':
				ii['crystalstring']='Likely R'
			elif i[7] == '7':
				ii['crystalstring']='Solid R'
			if i[5]=='Yes' and i[6]!='No':
				ii['incumbent']='Yes'
			else:
				ii['incumbent']='No'
			ii['incparty']=i[4]
for i in allmoney:
	
	if i[19]=='0':
		i[19]='1'
	for ii in allreps:
		if ii['name']==i[18]+'-'+i[19]:
			if i[3] == '1' and float(i[5])>99999:
				ii['dems'].append({'name':i[1][:20],'raised':str(int(float(i[5])/1000))+'K','spent':str(int(float(i[7])/1000))+'K'})
			elif i[3] == '2' and float(i[5])>99999:
				ii['reps'].append({'name':i[1][:20],'raised':str(int(float(i[5])/1000))+'K','spent':str(int(float(i[7])/1000))+'K'})

for i in allresultshouse14[1:]:
	if i[10] == 'R' or i[10] == 'D':
		if str(int(i[3][:2]))=='0':
			dname = i[1]+'-1'
		else:
			dname = i[1]+'-'+str(int(i[3][:2]))
		for ii in allreps:
			if ii['name']==dname:
				if i[16] != '':
					if i[10] == 'R':
						ii['perc14r']=i[16].replace('%','')
					elif i[10] == 'D':
						ii['perc14d']=i[16].replace('%','')

for i in allresultshouse16[1:]:
	if i[10] == 'R' or i[10] == 'D':
		if len(i[3]) > 0:
			if str(int(i[3][:2]))=='0':
				dname = i[1]+'-1'
			else:
				dname = i[1]+'-'+str(int(i[3][:2]))
			for ii in allreps:
				if ii['name']==dname:
					if i[16] != '':
						if i[10] == 'R':
							ii['perc16r']=i[16].replace('%','')
						elif i[10] == 'D':
							ii['perc16d']=i[16].replace('%','')

precision = .5		
xstretch = 90*precision
ystretch = 100*precision
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
	if state['name'] == 'AK':
		xstretch = 27*precision
		ystretch = 30*precision
	else:
		xstretch = 90*precision
		ystretch = 100*precision
	if state['name'] == 'AK':
		xadd = -6500*precision
		yadd = -950*precision
	elif state['name'] == 'HI':
		xadd = 4600*precision
		yadd = -500*precision
	else:
		xadd = 0
		yadd = 0
	for iiii in alldata['coordinates']:
		for iii in iiii:
			iStr = ""
			for ii in range(0,len(iii)):
				if int(xstretch*iii[ii][0])+xadd != lastx or -1*int(ystretch*iii[ii][1])+yadd != lasty or int(xstretch*iii[ii][0])+xadd != lastx or -1*int(ystretch*iii[ii][1])+yadd != lasty:
					iStr += str(int(xstretch*iii[ii][0])+xadd)
					iStr += ','
					iStr += str(-1*int(ystretch*iii[ii][1])+yadd)
					iStr += ' '
					lastx = int(xstretch*iii[ii][0]+xadd)
					lasty = -1*int(ystretch*iii[ii][1]+yadd)
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
		
		this_state['name'] = state['name']+'-'+str(i)
		this_district = {}
		for ii in allreps:
			if this_state['name'] == ii['name']:
				this_district = ii
		
		this_state['last'] = int(this_district['crystal'])
		this_state['hover'] = this_district
		this_state['polygons'] = []
		lastx = 0
		lasty = 0
		for iiii in alldata['geometry']['coordinates']:
			for iii in iiii:
				iStr = ""
				for ii in range(0,len(iii)):
					if int(xstretch*iii[ii][0])+xadd != lastx or -1*int(ystretch*iii[ii][1])+yadd != lasty or int(xstretch*iii[ii][0])+xadd != lastx  or -1*int(ystretch*iii[ii][1])+yadd != lasty :
						iStr += str(int(xstretch*iii[ii][0])+xadd)
						iStr += ','
						iStr += str(-1*int(ystretch*iii[ii][1])+yadd)
						iStr += ' '
						if -1*int(ystretch*iii[ii][1])+yadd > maxY:
							maxY = -1*int(ystretch*iii[ii][1])+yadd
						if int(xstretch*iii[ii][0])+xadd > maxX:
							maxX = int(xstretch*iii[ii][0])+xadd
						if -1*int(ystretch*iii[ii][1])+yadd < minY:
							minY = -1*int(ystretch*iii[ii][1])+yadd
						if int(xstretch*iii[ii][0])+xadd < minX:
							minX = int(xstretch*iii[ii][0])+xadd
						lastx = int(xstretch*iii[ii][0])+xadd
						lasty = -1*int(ystretch*iii[ii][1])+yadd
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
startStr = "---\ntitle: 'U.S. House Races Map - Just CSS/HTML'\ndescription: 'Create your own map to predict 2018 U.S. House races. View information about each district to pick a winner.'\ndate: 2018-06-20\ntags: []\ndraft: false\ntype: 'games'\n"
f.write(startStr+'states: '+json.dumps(states)+'\nbounds: "'+str(allbounds[0]-1)+' '+str(allbounds[1]-1)+' '+str(allbounds[2]-allbounds[0]+2)+' '+str(allbounds[3]-allbounds[1]+2)+'"\n'+"layout: 'congdistrictmap'\n---")
f.close()

	