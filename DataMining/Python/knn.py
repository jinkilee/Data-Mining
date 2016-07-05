# Source : http://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/

import operator
import classificationpy
import csv
import random
import matplotlib.pyplot as plt
import numpy as np

def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'r') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])

def main():
	x = [[1,1], [1,0], [0,2], [2,4], [3,5]]
	x = np.array(x)
	x = x.transpose()

	c = [[0.6667,2.5], [1,4.5]]

	plt.scatter(x[0], x[1], marker="o")
	plt.scatter(c[0], c[1], marker="o", color="red")
	plt.show()

if __name__=="__main__":
	main()

