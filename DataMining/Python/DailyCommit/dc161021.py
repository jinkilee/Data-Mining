import numpy as np
from sklearn.preprocessing import normalize

def get_gini(a):
	n = len(a)
	numerator   = sum([i*a[i] for i in range(n)])
	denominator = sum([a[i] for i in range(n)])*n

	if 0 == denominator:
		denominator = 0.000000001

	g = (2*numerator)/float(denominator) + (n+1)/float(n)
	return g

def main():
	a = np.sort(np.random.randint(0, 100, size=(10,)))
	a = np.zeros(10)
	print a
	print get_gini(a)

	a = np.ones(10) + 1090
	print a
	print get_gini(a)

if __name__=="__main__":
	main()
