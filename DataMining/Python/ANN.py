import numpy as np

class Neural_Network(object):
	# Initialize Artificial Neural Network
	def __init__(self):
		# Initialize size
		self.inputLayerSize  = 2
		self.hiddenLayerSize = 3
		self.outputLayerSize = 1

		# Initialize weight
		self.w1 = np.random.randn(self.inputLayerSize,   self.hiddenLayerSize)
		self.w2 = np.random.randn(self.hiddenLayerSize, self.outputLayerSize)

	def forward(self, X):
		self.z2 = np.dot(X, self.w1)
		self.a2 = self.sigmoid(self.z2)
		self.z3 = np.dot(self.a2, self.w2)
		yHat    = self.sigmoid(self.z3)

		return yHat
		
	# Activation function
	def sigmoid(self, z):
		return 1/(1+np.exp(-z))

	# Derivative of Sigmoid Function
	def sigmoidPrime(self, z):
		return np.exp(-z)/((1+np.exp(-z))**2)

	#Compute cost for given X,y, use weights already stored in class.
	def costFunction(self, X, y):
		self.yHat = self.forward(X)
		J = 0.5*sum((y-self.yHat)**2)
		return J

	# Compute derivative with respect to w1 and w2
	def costFunctionPrime(self, X, y):
		self.yHat = self.forward(X)

		delta3 = np.multiply(-(y-self.yHat), self.sigmoidPrime(self.z3))
		dJdw2  = np.dot(self.a2.T, delta3)

		delta2 = np.dot(delta3, self.w2.T) * self.sigmoidPrime(self.z2)
		dJdw1  = np.dot(X.T, delta2)

		return dJdw1, dJdw2

def main():
	X  = np.array([[3, 5], [5, 1], [10, 2]])
	y  = np.array([[75], [82], [93]])
	NN = Neural_Network()

	cost1 = NN.costFunction(X, y)
	print(cost1)
	dJdw1, dJdw2 = NN.costFunctionPrime(X, y)

	scalar = 3
	NN.w1  = NN.w1 + scalar*dJdw1
	NN.w2  = NN.w2 + scalar*dJdw2
	cost2 = NN.costFunction(X, y)
	print(cost2)

if __name__ == "__main__":
	main()
