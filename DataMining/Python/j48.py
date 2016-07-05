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
			train.append([[data[0],data[1],data[2],data[3]], data[4][:-1]])
		else:
			test.append([[data[0],data[1],data[2],data[3]], data[4][:-1]])
		idx = idx + 1

	return train, test

def main():
	split = 0.67
	#train, test = splitData("../Data/golf1.data", split)
	#train, test = splitData("../Data/weather.data", split)
	train = [[['sunny', '80', '90', 'TRUE'], 'no'], [['overcast', '83', '86', 'FALSE'], 'yes'], [['rainy', '70', '96', 'FALSE'], 'yes'], [['rainy', '68', '80', 'FALSE'], 'yes'], [['overcast', '64', '65', 'TRUE'], 'yes'], [['sunny', '69', '70', 'FALSE'], 'yes'], [['rainy', '75', '80', 'FALSE'], 'yes'], [['sunny', '75', '70', 'TRUE'], 'yes'], [['overcast', '72', '90', 'TRUE'], 'yes']]
	test = [[['sunny', '85', '85', 'FALSE'], 'no'], [['rainy', '65', '70', 'TRUE'], 'no'], [['sunny', '72', '95', 'FALSE'], 'no'], [['overcast', '81', '75', 'FALSE'], 'yes'], [['rainy', '71', '91', 'TRUE'], 'no']]

	result = classificationpy.J48(train, test)

if __name__=="__main__":
	main()

