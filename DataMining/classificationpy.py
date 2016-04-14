import numpy as np
import math
import operator

class Classification():
	def __init__(self, accuracy):
		self.accuracy = accuracy

def splitbyAttr(data, n):
	dicdata = {}
	lendata = len(data)
	model = []
	for i in range(lendata):
		key = data[i][0][n]
		if key not in dicdata:
			dicdata[key] = 1
			continue
		dicdata[key] += 1

	idx = 0
	for k,v in dicdata.items():
		yescount = 0
		for i in range(v):
			if "yes" == data[idx][1]:
				yescount += 1
			idx = idx + 1
		model.append([v/lendata, yescount/v])

	return model

# rainy,75,80,FALSE,yes
def J48(train, test):
	attrtype = ["nominal", "numeric", "numeric", "nominal"]
	lenattr  = len(attrtype)

	model = []
	for i in range(lenattr):
		if "nominal" == attrtype[i]:
			model.append(splitbyAttr(train, i))
		if "numeric" == attrtype[i]:
			continue
	print(model)

def calculateProb(x, avgx, stdx):
	varx = np.power(stdx,2)
	power = np.power((int(x)-avgx),2)/(2*varx)
	return 1/(np.sqrt(2*math.pi)*stdx)*np.exp(-1*power)

def measureNormDist(data, n):
	lendata = len(data)
	avgx = sum([int(data[i][0][n]) for i in range(lendata)])/lendata
	varx = sum([np.power(int(data[i][0][n])-avgx,2) for i in range(lendata)])/(lendata-1)
	stdx = np.sqrt(varx)

	return [avgx, stdx]

def measureProb(data, n):
	dicx = {}
	lenx = len(data)

	for i in range(lenx):
		key = data[i][0][n]
		if key not in dicx:
			dicx[key] = 1
		else:
			dicx[key] += 1

	for k,v in dicx.items():
		dicx[k] = v/lenx

	return dicx

def predictNumeric(x, model):
	# model : [avg, std]
	return calculateProb(x, model[0], model[1])

def predictNominal(x, model):
	for k,v in model.items():
		if x == k:
			return v

	if x not in model:
		return 0

def predictClass(x, yesmodel, nomodel, yesprob):
	attrtype = ['nominal','numeric','nominal','numeric','nominal','nominal']
	lenattr  = len(attrtype)
	totalprob = [1,1]
	for i in range(lenattr):
		if "nominal" == attrtype[i]:
			totalprob[0] = totalprob[0] * predictNominal(x[0][i], yesmodel[i])
			totalprob[1] = totalprob[1] * predictNominal(x[0][i], nomodel[i])
			#print(predictNominal(x[0][i], yesmodel[i]), predictNominal(x[0][i], nomodel[i]), totalprob)
		if "numeric" == attrtype[i]:
			totalprob[0] = totalprob[0] * predictNumeric(x[0][i], yesmodel[i])
			totalprob[1] = totalprob[1] * predictNumeric(x[0][i], nomodel[i])
			#print(predictNumeric(x[0][i], yesmodel[i]), predictNumeric(x[0][i], nomodel[i]), totalprob)

	if totalprob[0]*yesprob > totalprob[1]*(1-yesprob):
		return "yes"
	elif totalprob[1]*(1-yesprob) > totalprob[0]*yesprob:
		return "no"
	else:
		print("hello")
		return "yes"

def splitbyClass(train):
	lentrain = len(train)
	yestrain = []
	notrain  = []
	for i in range(lentrain):
		if 'yes' == train[i][1]:
			yestrain.append(train[i])
		else:
			notrain.append(train[i])

	return yestrain, notrain
	

def NB(train, test):
	yestrain, notrain = splitbyClass(train)
	yesprob = len(yestrain)/(len(yestrain) + len(notrain))
	yesmodel = []
	nomodel = []

	# To build a model
	attrtype = ['nominal','numeric','nominal','numeric','nominal','nominal']
	lenattr  = len(attrtype)
	for i in range(lenattr):
		if "nominal" == attrtype[i]:
			yesmodel.append(measureProb(yestrain, i))
			nomodel.append(measureProb(notrain, i))
		if "numeric" == attrtype[i]:
			yesmodel.append(measureNormDist(yestrain, i))
			nomodel.append(measureNormDist(notrain, i))

	# To predict test set
	prediction  = []
	lentest = len(test)
	for i in range(lentest):
		#print("predicted as : ", predictClass(test[i], yesmodel, nomodel))
		prediction.append(predictClass(test[i], yesmodel, nomodel, yesprob))

	result = Classification(getAccuracy(test, prediction))
	return result

def kNN(train, test, k):
	lenTest  = len(test)
	prediction = []
	for i in range(lenTest):
		neighArr = getNeighbor(train, test[i], k)
		result   = getResponse(neighArr)
		prediction.append(result)

	result = Classification(getAccuracy(test, prediction))
	return result

def getAccuracy(test, prediction):
	lenTest = len(test)
	lenPred = len(prediction)

	# To verify test and prediction set length
	if lenTest != lenPred:
		print("Error: test set and prediction set should have same length")
		return

	correct = 0
	for i in range(lenTest):
		if test[i][-1] == prediction[i]:
			correct = correct + 1

	return correct/lenTest

def getResponse(neighbors):

	# To count vote
	vote = {}
	lenNeigh = len(neighbors)
	for i in range(lenNeigh):
		response = neighbors[i][-1]
		if response not in vote:
			vote[response] = 1
			continue
		vote[response] = vote[response] + 1

	# To sort vote dictionary
	# sortedVote = sorted(list(vote.values()), reverse=True)
	sortedVote = sorted(vote.items(), key=operator.itemgetter(1), reverse=True)
	
	return sortedVote[0][0]

def getNeighbor(train, test, k):
	# To calculate distance
	lenTrain = len(train)
	distArr = []
	for i in range(lenTrain):
		distArr.append([train[i], euclideanDistance(train[i], test, 4)])

	# To return k nearest data
	neighArr = []
	distArr.sort(key=operator.itemgetter(1))
	for i in range(k):
		neighArr.append(distArr[i][0])

	return neighArr

def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)
