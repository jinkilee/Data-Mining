import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

from dtw import dtw
from numpy.linalg import norm
from sklearn.svm import OneClassSVM

def main():
	n = 1000
	data = []
	for i in range(n):
		data.append(np.array([np.random.randint(0, 5000) for i in range(np.random.randint(20, 150))]))
	data = np.array(data)

	# making all the data into 5 dimensions
	# howto : boxplot
	x = []
	y = []
	for i in data:
		sorted_i = sorted(i)
		x.append([max(sorted_i), np.percentile(sorted_i, 75), np.median(sorted_i), np.percentile(sorted_i, 25), min(sorted_i)])
		y.append(0)
	x = np.array(x)

	'''
	# making all the data into 5 dimensions
	# howto : distance
	start = time.time()
	data_i = 0
	cnt = 1
	x = np.zeros((n, n))
	for i in data:
		data_j = data_i
		for j in data[cnt:]:
			dist = dtw(i, j, dist=lambda i, j: norm(i - j, ord=1))[0]
			x[data_i][data_j+1], x[data_j+1][data_i] = dist, dist
			data_j += 1
		cnt += 1
		data_i += 1
	end = time.time()
	print(end - start)
	'''

	# build model with x
	model = OneClassSVM()
	model.fit(x)

	# create test dataset
	test = []
	for i in range(10):
		test.append(np.array([np.random.randint(0, 10000) for i in range(np.random.randint(20000, 30000))]))
	test = np.array(test)

	# transform test dataset
	x = []
	y = []
	for i in test:
		sorted_i = sorted(i)
		x.append([max(sorted_i), np.percentile(sorted_i, 75), np.median(sorted_i), np.percentile(sorted_i, 25), min(sorted_i)])
		y.append(0)
	x = np.array(x)

	# predict test dataset
	pred = model.predict(x)

	'''
	we can "predict" with boxplot.. maybe.. just simply
	'''

if __name__=="__main__":
	main()
