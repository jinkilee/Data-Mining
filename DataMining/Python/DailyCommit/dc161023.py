import numpy as np
import math

def get_gini(a):
	n = len(a)
	numerator   = sum([i*a[i] for i in range(n)])
	denominator = sum([a[i] for i in range(n)])*n

	if 0 == denominator:
		denominator = 0.000000001

	g = (2*numerator)/float(denominator) + (n+1)/float(n)
	return g

# mean absolute difference
def test():
	a = np.sort(np.random.randint(0,60, size=(100,)))
	norm1 = np.sort(np.random.randint(0, 6, size=(30,)))
	norm2 = np.sort(np.random.randint(25, 32, size=(35,)))
	norm3 = np.sort(np.random.randint(55, 60, size=(35,)))
	norm = np.concatenate((norm1, norm2, norm3))

	d = 60/100.
	eq = np.array([d*i for i in range(100)])

	if np.average(abs(a - eq)) >= np.average(abs(norm - eq)):
		print np.average(abs(a - eq)), np.average(abs(norm - eq))

def main():
	for i in range(1000):
		test()
	
if __name__=="__main__":
	main()
