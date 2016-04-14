import numpy as np
import regressionpy

def main():
	'''
	x = [4.1,6.5,12.6,25.5,29.8,38.6,46,52.8,59.6,66.3,74.7]
	y = [2.2,4.5,10.4,23.1,27.9,36.8,44.3,50.7,57.5,64.1,72.6]
	'''

	x = []
	y = []
	f = open("../Data/logistic.data", "r")
	#f = open("../Data/test1.data", "r")
	#f = open("../Data/abalone.data", "r")
	for i in f:
		data = i.split(",")
		'''
		# Simple Linear Regression
		x.append(float(data[1]))
		y.append(float(data[0]))
		'''
		
		# Multi Linear Regression
		if 'yes\n' == data[1]:
			y.append(1)
		if 'no\n' == data[1]:
			y.append(0)
		x.append(int(data[0]))
		#x.append([1, float(data[5]), float(data[6]), float(data[7])])

	'''
	# Simple Linear Regression
	a = regressionpy.LinearRegression(x, y)
	print("coefficient and intercept : ", a.coef, a.intercept)
	print("r_value : ", a.r_value)
	#fit = np.polyfit(x, y, 1)
	#fit_fn = np.poly1d(fit)
	#print(fit_fn)

	# Multi Linear Regression
	a = regressionpy.MultiLinearRegression(x, y)
	print("Coefficient : ", a.coef)
	print("Intercept : ", a.intercept)
	print("r_value : ", a.r_value)
	'''
	regressionpy.LogisticRegression(x, y)

if __name__=="__main__":
	main()
