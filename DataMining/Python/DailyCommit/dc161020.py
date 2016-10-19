import numpy as np
from sklearn.preprocessing import normalize

def normalize_data(data):
	data = data.transpose()
	data = normalize(data)
	return data.transpose()

	subsize = len(data)/k

def kfold_cross_validation(k, data):
	num = 0
	subset_size = len(data)/k
	while num < k:
		yield num*subset_size, subset_size
		num += 1

def generate_x(n):
	x1 = np.random.randint(0, 10, size=(n,))
	x2 = np.random.randint(0, 1000, size=(n,))
	x = np.concatenate(([x1], [x2]))
	return x.transpose()

def main():
	n = 100
	x = generate_x(n)
	y = np.random.randint(0, 2, size=(n,))

	x = normalize_data(x)
	for i, ss in kfold_cross_validation(10, x):
		x_test = x[i:i+ss]
		y_test = y[i:i+ss]
		x_train = np.concatenate((x[:i], x[i+ss:]))
		y_train = np.concatenate((y[:i], y[i+ss:]))

		print x_test.shape
		print y_test.shape
		print x_train.shape
		print y_train.shape
		print "####################"


if __name__=="__main__":
	main()
