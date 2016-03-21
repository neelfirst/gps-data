#!/usr/bin/python

import time, sys, os.path, math

temp = []
dataType = 0 # 0 - time, 1 - solution, 2 - SV
dataSet = []
dataPt = [0]*10
satData = []
satData.append([])
satData.append([])

if not os.path.isfile(sys.argv[1]):
	exit("Could not find file")
with open(sys.argv[1]) as file:
	for line in file:
		if 'Gps Solution' in line and dataType == 0:
			dataType = 1
		elif 'Healthy\tDGPS' in line and dataType == 1:
			dataType = 2
		elif '----------------------------------------------------' in line and dataType == 2:
			# assemble data line here
			dataPt[8] = sum(satData[1])/len(satData[1])
			dataPt[9] = satData
			dataSet.append(dataPt)
			dataType = 0
			satData = []
			satData.append([])
			satData.append([])

		if dataType == 0:
			try:
				dataPt[0] = time.strptime(line,"%a %b %d %H:%M:%S %Z %Y\n")
			except:
				continue
		elif dataType == 1:
			try:
				if "Sats visible" in line:
					dataPt[3] = int(line.split(':')[1])
				elif "Sats used" in line:
					dataPt[4] = int(line.split(':')[1])
				elif "Latitude" in line:
					dataPt[1] = float(line.split(':')[1].split(' ')[1])
				elif "Longitude" in line:
					dataPt[2] = float(line.split(':')[1].split(' ')[1])
				elif "Pos Acc" in line:
					temp = line.split(':')[1].split(' ')
					del temp[0::2]
					dataPt[5] = math.sqrt(sum(map(lambda i:i*i,[float(j) for j in temp])))
				elif "Vel Acc" in line:
					dataPt[6] = float(line.split(':')[1].split(' ')[1])
				elif "Time Acc" in line:
					dataPt[7] = float(line.split(':')[1].split(' ')[1])
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
