import sys
import numpy as np

# Cross validation
def cross_validation(X, y, k):
	# Error if length of X and y differs
	if len(X) != len(y):
		print("Invalid X and y : length differs")
		return

	# Get size of subset
	subset_size = len(X) / k

	# Yield ith dataset
	for i in range(k):
		# Divide into train:test word vector dataset
		testX  = X[i*subset_size:][:subset_size]
		trainX = np.concatenate((X[:i*subset_size], X[(i+1)*subset_size:]))

		# Divide into train:test sentiment dataset
		testy  = y[i*subset_size:][:subset_size]
		trainy = np.concatenate((y[:i*subset_size], y[(i+1)*subset_size:]))

		yield(testX, trainX, testy, trainy)

def main():
	# Get k from parameter
	k = int(sys.argv[1])

	X = np.random.rand(10, 3)
	y = np.random.randint(2, size=10)

	# Give whole dataset(X and y) to cross_validation function
	sample = cross_validation(X, y, k)
	for subset in sample:
		[testX, trainX, testY, trainy] = [subset[j] for j in range(4)]
		
		# Do whatever you want with testX, trainX, testy, trainy
		# ... your code ...

if __name__ == "__main__":
	main()
