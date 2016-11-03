import numpy as np

def dist(a, b):
	return np.linalg.norm(a-b)

def main():
	a = np.random.randint(0,  10, size=(10, 4))
	b = np.random.randint(20, 30, size=(10, 4))
	c = np.random.randint(70, 80, size=(10, 4))
	input_data = np.concatenate((a, b, c))

	weights = np.random.rand(3,4)

	# train weight of NN
	cnt = 0
	learning_rate = 0.1
	while(True):
		prev_weights = np.copy(weights)
		cnt += 1

		# compare distance and update weight
		for data in input_data:
			comp = np.array([dist(data, w) for w in weights])
			winner = comp.argmin(axis=0)
			weights[winner] = weights[winner] + learning_rate*(data - weights[winner])

		# check if weight is modified
		if True == np.array_equal(prev_weights, weights):
			break

	print weights

	# test new data with trained weight
	a = np.random.randint(0,  10, size=(10, 4))
	b = np.random.randint(20, 30, size=(10, 4))
	c = np.random.randint(70, 80, size=(10, 4))
	another_data = np.concatenate((a, b, c))

	print "------------------------------"

	# compare distance
	for data in another_data:
		comp = np.array([dist(data, w) for w in weights])
		winner = comp.argmin(axis=0)
		print data, winner

if __name__=="__main__":
	main()
