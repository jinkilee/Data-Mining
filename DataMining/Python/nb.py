# Source : http://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/

import operator
import classificationpy
import csv
import random
import os

def splitData(filename, split):
	f = open(filename, "r")
	lenf = sum(1 for line in f)
	f = open(filename, "r")
	randintarr = random.sample(range(0, lenf), lenf)
	lentrain = int(len(randintarr)*split)
	trainidx = randintarr[:lentrain]
	testidx  = randintarr[lentrain:]

	idx = 0
	train = []
	test  = []
	for i in f:
		data = i.split(",")
		if idx in trainidx:
			train.append([[data[0],data[1],data[2],data[3],data[4],data[5]], data[6][:-1]])
		else:
			test.append([[data[0],data[1],data[2],data[3],data[4],data[5]], data[6][:-1]])
		idx = idx + 1

	return train, test

def main():
	split = 0.67
	train, test = splitData("../Data/golf1.data", split)
	#train, test = splitData("../Data/golf.data", split)

	result = classificationpy.NB(train, test)
	print(result.accuracy)

if __name__=="__main__":
	main()

