import gzip
import pickle
import numpy as np
import sys

def sigmoid(x, c=1):
	w = np.array([1,2,3]) * c
	b = 0.5 * c
	y = sum(x*w + b)
	y = 1/(1+np.exp(-y))

	print(y)

	if y >= 0.5:
		return 1
	if y <  0.5:
		return 0


def main():
	'''
	with gzip.open('data/mnist.pkl.gz', 'rb') as f:
		train_set, valid_set, test_set = pickle.load(f)
	'''

	x = np.array([1,2,3])
	C = int(sys.argv[1])
	print(sigmoid(x, C))

if __name__ == "__main__":
	main()
