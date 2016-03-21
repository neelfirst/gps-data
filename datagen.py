#!/usr/bin/python

import time, sys, os.path

dataType = 0 # 0 - time, 1 - solution, 2 - SV
dataSet = []
dataPt = []

if not os.path.isfile(sys.argv[1]):
	exit("Could not find file")
with open(sys.argv[1]) as file:
	for line in file:
		if 'Gps Solution' in line and dataType == 0:
			dataType = 1
			continue
		elif 'Healthy DGPS' in line and dataType == 1:
			dataType = 2
			continue
		elif '----------------------------------------------------' in line and dataType == 2:
			dataType = 0
			# assemble data line here
			continue
		
		if dataType == 0:
			try:
				data[0] = time.strptime(line,"%a %b %d %H:%M:%S %Z %Y\n")
			except:
				continue
		elif dataType == 1:
			try:
				if "Sats visible" in line:
				elif "Sats used" in line:
				elif "Latitude" in line:
					
				elif "Longitude" in line:
				elif "Pos Acc" in line:
				elif "Vel Acc" in line:
				elif "Time Acc" in line:
			except:
				continue
		elif dataType == 2:
			# read in tab delimited values here
			
			
		

# ugh need pseudocode
# 1. open file for read
# 2. assume first line is a date
# 3. read in date
# 4. check next line contains 'Gps Measurement'
# 5. switch to reading Sat info etc
# 6. check next line contains 'Space Vehicle Info'
# 7. switch to reading SV info
