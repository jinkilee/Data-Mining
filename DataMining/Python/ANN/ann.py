import numpy as np


def sigmoid(z):
	return 1.0/(1.0+np.exp(-z))
	
def sigmoid_prime(z):
	return sigmoid(z)*(1-sigmoid(z))

class network():
	def __init__(self, size):
		self.depth = len(size)
		self.size  = size
		self.num_hlayer = self.depth - 2
		#self.weights = [np.random.randn(y, x) for x, y in zip(size[:-1], size[1:])]
		#self.biases  = [np.random.randn(i) for i in size[1:]]
		self.weights = [np.array([[0.15, 0.2],[0.25, 0.30]]), np.array([[0.40, 0.45],[0.50, 0.55]])]
		self.biases  = np.array([0.35, 0.60])

		# Empty list
		self.nets  = []
		self.outs  = []
		self.dels  = []
		self.delta_weights = []

	def print_weight(self):
		for weight in self.weights:
			print(weight)

	def print_bias(self):
		for bias in self.biases:
			print(bias)

	def feedforward(self, input_data):
		self.outs.append(input_data)
		for w, b in zip(self.weights, self.biases):
			self.nets.append(np.dot(w, self.outs[-1]) + b)
			self.outs.append(sigmoid(self.nets[-1]))

	def backprop(self, input_data, label):
		self.feedforward(input_data)
		self.dels.append((self.outs[-1]-label)*self.outs[-1]*(1-self.outs[-1]))

		# first round
		self.dels[-1] = self.dels[-1].reshape((self.dels[-1].size,1))
		self.outs[-2] = self.outs[-2].reshape((self.outs[-2].size,1))
		self.delta_weights.append(np.dot(self.dels[-1], self.outs[-2].transpose()))

		# second round
		## sum matrix
		print(np.dot(self.weights[-1].transpose(), self.dels[-1]))
		#self.outs[-3] = self.outs[-3].reshape((self.outs[-3].size,1))

		#print(self.outs[-2])
		#print(np.dot((np.dot(self.weights[-1], self.dels[-1]) * self.outs[-2]),(self.outs[-3].reshape(self.outs[-3].size,1).transpose())))

	'''
	def feedforward(self, input_data):
		input_data = sigmoid(np.dot(self.weights[0], input_data) + self.biases[0])
		for i in range(1, self.depth-1):
			input_data = sigmoid(np.dot(self.weights[i], input_data) + self.biases[i])
		return input_data

	def backprop(self, input_data, label):
		# Initialization
		nets  = [np.zeros(i,) for i in self.size[1:]]
		outs  = [np.zeros(i,) for i in self.size[1:]]
		delta = [np.zeros(i,) for i in self.size[1:]]
		delta_weights = [np.zeros((y, x)) for x, y in zip(self.size[:-1], self.size[1:])]

		# Feedforward
		nets[0] = np.dot(self.weights[0], input_data) + self.biases[0]
		outs[0] = sigmoid(nets[0])
		for i in range(1, self.depth-1):
			nets[i] = np.dot(self.weights[i], outs[i-1]) + self.biases[i]
			outs[i] = sigmoid(nets[i])

		# Backpropagation
		delta[-1] = (outs[-1] - label) * (outs[-1] * (1 - outs[-1]))	# (2,)
		delta_weights[-1] = np.dot(delta[-1].reshape((self.size[-1],1)), outs[-2].reshape((1,self.size[-2])))
		
		# This loop starts from 2 and ends at 3
		for layer in range(2, self.depth):
			print(self.size[-layer])
			#delta[-layer] = (outs[-layer] - label) * (outs[-layer] * (1 - outs[-layer]))
	'''
	#def backprop(self, input_data, label):
