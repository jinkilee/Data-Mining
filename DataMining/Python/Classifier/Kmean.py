import numpy as np
import io
import csv
import time

def MinIdx(disttocentre):
	minidx = 0
	mindist = disttocentre[0]
	disttocentrelen = len(disttocentre)
	for i in range(disttocentrelen):
		if mindist > disttocentre[i]:
			minidx = i
			mindist = disttocentre[i]

	return minidx

def FindClosestCentre(centre, point):
	disttocentre = []
	centrelen = len(centre)

	for i in range(centrelen):
		disttocentre.append(Euclidean(point, centre[i]))

	#print "distance : ", disttocentre
	return MinIdx(disttocentre)

def Euclidean(x, y):
	length = len(x)
	dist = 0

	for i in range(length):
		dist = dist + np.power(x[i]-y[i], 2)

	return np.sqrt(dist)

def Recluster(data, permcentre):
	datalen = len(data)
	centreidx = [[],[],[],[],[],[],[],[],[],[],[],[]]

	#print("Permanent Centres : ", permcentre)
	for i in range(datalen):
		closestcentre = FindClosestCentre(permcentre, data[i])
		centreidx[closestcentre].append(i)

	#print(centreidx)
	return centreidx

def UpdateCentre(centre, centreidx, data, closestcentre):
	numofcluster = len(centreidx)
	numofdataincluster = [len(centreidx[i]) for i in range(numofcluster)]
	newcentre = []

	#print(numofdataincluster) [1,5,2]
	for i in range(numofcluster):
		newcentreXsum = 0
		newcentreYsum = 0
		for j in range(numofdataincluster[i]):
			newcentreXsum = newcentreXsum + data[centreidx[i][j]][0]
			newcentreYsum = newcentreYsum + data[centreidx[i][j]][1]
		#print("newcentre : ", newcentreXsum/numofdataincluster[i], newcentreYsum/numofdataincluster[i])
		newcentre.append([newcentreXsum/numofdataincluster[i], newcentreYsum/numofdataincluster[i]])

	#print("newcentre : ", newcentre)
	return newcentre

def Kmean(data, centreidx):
	datalen = len(data)
	iternum = 0

	# Initialize centre
	centre = []
	tmp = []
	centreidxlen = len(centreidx)
	for i in range(centreidxlen):
		centre.append(data[centreidx[i][0]])

	while(centre != tmp):
		tmp = centre
		for i in range(datalen):
			# Avoid points in centre
			if data[i] in centre:
				continue
			# Perform Euclidean distance
			closestcentre = FindClosestCentre(centre, data[i])

			# Add closestcentre index into centreidx
			if i in centreidx[closestcentre]:
				continue
			centreidx[closestcentre].append(i)

		'''
		print("#######################################")
		print("centreidx : ", centreidx)
		print("centre : ", centre)
		print("data : ", data)
		print("closestcentre : ", closestcentre)
		'''

		# Update centre
		centre = UpdateCentre(centre, centreidx, data, closestcentre)
		#print("newcentre : ", centre)

		# Reclustering with permanently updated centre
		centreidx = Recluster(data, centre)
		#print("#######################################")
		iternum = iternum + 1
		print(iternum, centre==tmp)
		#print(centre)

	return centreidx

def ReadData():
	input_data = open('../Data/AADF-data-major-roads.csv', 'r')
	#input_data = open('../Data/5000Sample.csv', 'r')
	input_data.readline()
	data = []
	answer = []

	# Read Data
	for i in input_data:
		oneline = io.StringIO(i)
		oneline_data = csv.reader(oneline, delimiter=',')

		for attr in oneline_data:
			data.append([int(attr[6]), int(attr[7])])
			answer.append(attr[2])
	# Return Data
	return data, answer

def getAccuracy(centreidx, answer):
	region_list = ["East Midlands","East of England","London","Merseyside","North East","North West","Scotland","South East","South West","Wales","West Midlands","Yorkshire and The Humber"]

	for i in range(12):
		length = len(centreidx[i])
		region = region_list[i]
		count = 0

		for j in range(length):
			if region == answer[centreidx[i][j]]:
				count = count + 1
		print(region, count, length)


def main():
	'''
	data = [ [2, 10], [2, 5], ]
	centreidx = [[0], [3], [6]]
	'''
	data,answer = ReadData()
	centreidx = [[436],[435],[433],[250048],[480],[452],[430],[441],[445],[99],[446],[439]]

	start = time.time()
	print("Kmean Started")

	centreidx = Kmean(data, centreidx)
	getAccuracy(centreidx, answer)

	end = time.time()
	print("Kmean Finished ", end-start)


if __name__=="__main__":
	main()
