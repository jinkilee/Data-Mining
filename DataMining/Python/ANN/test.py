import ann
import numpy as np

def main():
	# [0, 1] -> 1
	# [1, 0] -> 0
	label = np.array([
		[0, 1],
		[0, 1],
		[0, 1],
		[0, 1],
		[1, 0],
		[1, 0],
		[1, 0],
		[1, 0]
	])

	input_data = np.array([
		[0, 1],
		[1, 0],
		[1, 0],
		[0, 1],
		[1, 1],
		[0, 0],
		[1, 1],
		[0, 0],
	])

	test_data = np.array([
		[0, 0],
		[1, 1],
		[1, 0],
		[0, 1]
	])

	net = ann.network([2,4,2])
	net.SGD(input_data, label, 3000, 0.1)
	result = net.evaluate(test_data)

	print(result)

	'''
	#label = np.array([0.01, 0.99])
	net = ann.network([2,2,2])
	input_data = np.array([0.05, 0.10])
	net.feedforward_eval(input_data)
	#net = ann.network([2,2,2,2])
	'''

if __name__ == "__main__":
	main()
