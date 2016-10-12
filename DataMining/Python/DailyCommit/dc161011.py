import numpy as np
from dtw import dtw
from numpy.linalg import norm

def knn(x, y, k):
	for i in x:
		for j in x:
			dist, cost, acc, path = dtw(i, j, dist=lambda i, j: norm(i - j, ord=1))
			

def main():
	# dist, cost, acc, path = dtw(a, c, dist=lambda a, c: norm(a - c, ord=1))

	x = []
	y = []
	for i in range(30):
		onedata = np.array([np.random.randint(0, 5) for i in range(np.random.randint(5, 15))]).reshape(-1, 1)
		x.append(onedata)
		y.append(np.random.randint(0,2))
	x = np.array(x)
	y = np.array(y)

	knn(x, y, k=4)

if __name__ == "__main__":
	main()
