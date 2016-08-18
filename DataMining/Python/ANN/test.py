import ann
import numpy as np

def main():
	'''
	label = np.array([0.01, 0.99])
	net = ann.network([5,3,4,2])
	input_data = np.array([1,2,3,4,5])
	'''

	label = np.array([0.01, 0.99])
	net = ann.network([2,2,2])
	input_data = np.array([0.05, 0.10])

	net.backprop(input_data, label)

if __name__ == "__main__":
	main()
