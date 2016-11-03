import numpy as np

# Returned object for regression function
class Regression():
	def __init__(self, m, b, r):
		self.coef = m
		self.intercept = b
		self.r_value = r

	def set_rvalue(self, r):
		self.r_value = r

def LogOdds(x):
	return np.log(x/(1-x))

def LogisticRegression(x, y):
	xdic = {}
	lenx = len(x)
	for i in range(lenx):
		if x[i] not in xdic:
			xdic[x[i]] = [0,0]
			if 1 == y[i]:
				xdic[x[i]][1] = xdic[x[i]][1] + 1
			else:
				xdic[x[i]][0] = xdic[x[i]][0] + 1
			continue
		if 1 == y[i]:
			xdic[x[i]][1] = xdic[x[i]][1] + 1
		else:
			xdic[x[i]][0] = xdic[x[i]][0] + 1

	# To calculate probability			
	for i in xdic:
		xdic[i].append(xdic[i][1]/(xdic[i][1]+xdic[i][0]))

	xsum = 0; ysum = 0; xsqrsum = 0; ysqrsum = 0;xysum = 0
	for i in range(lenx):
		logodds = LogOdds(xdic[x[i]][2])
		xsum = xsum + x[i]
		ysum = ysum + logodds 
		xsqrsum = xsqrsum + np.power(x[i], 2)
		ysqrsum = ysqrsum + np.power(logodds, 2)
		xysum   = xysum   + x[i]*logodds

	# y = mx + b
	m = (lenx*xysum-xsum*ysum)/(lenx*xsqrsum-xsum*xsum)
	b = (xsqrsum*ysum-xsum*xysum)/(lenx*xsqrsum-xsum*xsum)
	print(m, b)

# Return Regression Object
def LinearRegression(x, y):
	N = len(x)
	if N != len(y):
		return "x and y should be same length of arrays"

	xsum = sum(x)
	ysum = sum(y)
	xysum= sum([x[i]*y[i] for i in range(N)])
	xsqrsum = sum(np.power(x,2))
	ysqrsum = sum(np.power(y,2))

	# correlation coefficient	
	SSxx = xsqrsum - N*xsum/N*xsum/N
	SSyy = ysqrsum - N*ysum/N*ysum/N
	SSxy = xysum - N*xsum/N*ysum/N
	r = np.sqrt((SSxy*SSxy)/(SSxx*SSyy))

	# y = mx + b
	m = (N*xysum-xsum*ysum)/(N*xsqrsum-xsum*xsum)
	b = (xsqrsum*ysum-xsum*xysum)/(N*xsqrsum-xsum*xsum)

	# To return result
	result = Regression(m, b, r)

	return result

# Return Regression Object
def MultiLinearRegression(x, y):
	lengthX = len(x[0]) - 1
	lengthY = len(y)
	coef = []

	# To convert into np array
	x = np.matrix(x)
	y = np.matrix(y)

	# To calculate transformation matrix -> temporarily stored in tmp
	xT  = x.transpose()
	tmp = xT * x
	tmp = np.linalg.inv(tmp) * xT * y
	for i in range(1,lengthX):
		coef.append(tmp.item(i))
	result = Regression(coef, tmp.item(0), 0)

	sumy = 0
	for i in range(lengthY):
		sumy = sumy + y.item(i)
	avgy = sumy/lengthY

	# To calculate correlation coefficient
	xlen = x.shape[1]
	realsqrsum = 0
	predsqrsum = 0
	for i in range(lengthY):
		realsqrsum = realsqrsum + np.power((y.item(i) - avgy), 2)
		#LinearSum(i, x, result)
		#predvalue  = result.intercept + result.coef[0]*x.item(xlen*i+1) + result.coef[1]*x.item(xlen*i+2)
		#predvalue  = result.intercept + result.coef[0]*x.item(xlen*i+1) + result.coef[1]*x.item(xlen*i+2) + result.coef[2]*x.item(xlen*i+3)
		predsqrsum = predsqrsum + np.power((LinearSum(i, x, result) - avgy), 2)
	tss = realsqrsum/lengthY
	ssr = predsqrsum/lengthY
	result.set_rvalue(np.sqrt(ssr/tss))

	return result

def LinearSum(idx, x, linearline):
	Sum = linearline.intercept
	length = len(linearline.coef) + 1
	xlen = length + 1
	for i in range(1, length):
		Sum = Sum + linearline.coef[i-1] * x.item(xlen*idx+i)
	return Sum
