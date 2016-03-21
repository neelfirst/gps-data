#!/usr/bin/python

import time, sys, os.path, math, csv

class DataPt:
	def __init__(self):
		self.t = time.gmtime()
		self.lat = 0
		self.long = 0
		self.visible = 0
		self.used = 0
		self.pos = 0
		self.vel = 0
		self.tacc = 0
		self.cn = 0
		self.rawcn = [[],[]]

temp = []
dataType = 0 # 0 - time, 1 - solution, 2 - SV
dataSet = []
dataPt = DataPt()
satData = []
satData.append([])
satData.append([])

if not os.path.isfile(sys.argv[1]):
	exit("Could not find file")
with open(sys.argv[1]) as file:
	for index, line in enumerate(file, start=0):
		if 'Gps Solution' in line and dataType == 0:
			dataType = 1
		elif 'Healthy\tDGPS' in line and dataType == 1:
			dataType = 2
		elif '----------------------------------------------------' in line and dataType == 2:
			# assemble data line here
			if dataPt.used != 0:
				dataPt.cn = sum(satData[1])/len(satData[1])
			else:
				dataPt.cn = 0
			dataPt.rawcn = satData
			dataSet.append(dataPt)
			dataType = 0
			satData = []
			satData.append([])
			satData.append([])
			dataPt = DataPt()

		if dataType == 0:
			try:
				dataPt.t = time.strptime(line,"%a %b %d %H:%M:%S %Z %Y\n")
			except:
				continue
		elif dataType == 1:
			try:
				if "Sats visible" in line:
					dataPt.visible = int(line.split(':')[1])
				elif "Sats used" in line:
					dataPt.used = int(line.split(':')[1])
				elif "Latitude" in line:
					dataPt.lat = float(line.split(':')[1].split(' ')[1])
				elif "Longitude" in line:
					dataPt.long = float(line.split(':')[1].split(' ')[1])
				elif "Pos Acc" in line:
					temp = line.split(':')[1].split(' ')
					del temp[0::2]
					dataPt.pos = math.sqrt(sum(map(lambda i:i*i,[float(j) for j in temp])))
				elif "Vel Acc" in line:
					dataPt.vel = float(line.split(':')[1].split(' ')[1])
				elif "Time Acc" in line:
					dataPt.tacc = float(line.split(':')[1].split(' ')[1])
			except:
				continue			
		elif dataType == 2:
			try:
				# read in tab delimited values here
				y = line.replace(' ','').split('\t')
				if (y[4] == 'Y'):
					satData[0].append(int(y[1]))
					satData[1].append(float(y[2]))
			except:
				continue

outFile1 = open('condensed.csv','w')
outFile2 = open('spacevehicle.csv','w')
out1 = csv.writer(outFile1)
out2 = csv.writer(outFile2)

for pt in dataSet:
	tString = str(pt.t.tm_hour)+':'+str(pt.t.tm_min)+':'+str(pt.t.tm_sec)
	out1.writerow([tString,pt.lat,pt.long,pt.visible,pt.used,pt.pos,pt.vel,pt.tacc,pt.cn])
	for i in pt.rawcn:
		for index in range(len(i)):
			out2.writerow([tString,pt.rawcn[0][index],pt.rawcn[1][index]])

