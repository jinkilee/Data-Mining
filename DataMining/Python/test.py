import numpy as np
import math

def entropy(p):
	if 0 == p or 1 == p:
		return 0
	return p*math.log(1/p) + (1-p)*math.log(1/(1-p))

def avgEntropy(p, p1):
	result = 0
	for i in range(len(p)):
		#print(p[i], entropy(p1[0][0]), entropy(p1[0][1]))
		print(p[i]*entropy(p1[i][0]) + (1-p[i])*entropy(p1[i][1]))

def countLessEqual(data, x):
	lendata = len(data)
	count = 0
	for i in range(lendata):
		if data[i] <= x:
			count += 1
	return count
	
def countLEYes(data, y, x):
	lendata = len(data)
	count = 0
	for i in range(lendata):
		if data[i] <= x and 'yes' == y[i]:
			count += 1

	return count

def countGYes(data, y, x):
	lendata = len(data)
	count = 0
	for i in range(lendata):
		if data[i] > x and 'yes' == y[i]:
			count += 1

	return count

def measureProb(data, y):
	uniq = np.unique(data)
	lenuniq = len(uniq)
	lendata = len(data)
	prob = []
	prob1= []
	for i in range(lenuniq):
		cLE = countLessEqual(data, uniq[i])
		prob.append(cLE/lendata)
		if cLE == lendata:
			prob1.append([countLEYes(data, y, uniq[i])/cLE,"N/A"])
			continue
		prob1.append([countLEYes(data, y, uniq[i])/cLE,(countGYes(data, y, uniq[i]))/(lendata-cLE)])

	return prob, prob1

def main ():
	# Overlook
	#p  = [4/14,5/14,5/14]
	#p1 = [1,3/5,2/5]

	# Windy
	#p  = [8/14,6/14]
	#p1 = [6/8,3/6]
	#print(avgEntropy(p,p1))
	#print(entropy(5/14))

	'''
	print(((1/5)*entropy(1)) + ((4/5)*entropy(1/4)))
	print(((2/5)*entropy(1/2)) + ((3/5)*entropy(1/3)))
	print(((3/5)*entropy(2/3)) + ((2/5)*entropy(0)))
	print(((4/5)*entropy(2/4)) + ((2/5)*entropy(0)))
	print(((5/5)*entropy(2/5)) + ((2/5)*entropy(0)))
	'''
	print((14/14)*entropy(9/14))
	print("####################################")
	#data = [64, 65, 68, 69, 70, 71, 72, 72, 75, 75, 80, 81, 83, 85] # Temperature
	data = [65, 70, 80, 70, 96, 91, 95, 90, 80, 70, 90, 75, 86, 85] # Humidity
	y    = ['yes', 'no', 'yes', 'yes', 'yes', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'no']
	p, p1 = measureProb(data, y)
	print(avgEntropy(p,p1))


if __name__=="__main__":
	main()
