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
		self.weights = [np.random.randn(y, x) for x, y in zip(size[:-1], size[1:])]
		self.biases  = [np.random.randn(i) for i in size[1:]]

		#self.weights = [np.array([[0.15, 0.2],[0.25, 0.30]]), np.array([[0.40, 0.45],[0.50, 0.55]]), np.array([[0.20, 0.40],[0.60, 0.80]])]
		#self.biases  = np.array([0.35, 0.60, 0.85])
		#self.weights = [np.array([[0.15, 0.2],[0.25, 0.30]]), np.array([[0.40, 0.45],[0.50, 0.55]])]
		#self.biases  = np.array([0.35, 0.60])

		# Empty list
		self.nets  = []
		self.outs  = []
		self.dels  = [0] * (self.depth-1)
		self.delta_weights = [0] * (self.depth-1)

	def print_weight(self):
		for weight in self.weights:
			print(weight)

	def print_bias(self):
		for bias in self.biases:
			print(bias)

	def SGD(self, input_data, label, epoch, learning_rate):
		for epo in range(epoch):
			sample_idx = (np.random.randint(0, len(input_data), 5))
			sample_input_data = input_data[sample_idx]
			sample_label      = label[sample_idx]

			for si, sl in zip(sample_input_data, sample_label):
				self.feedforward(si)
				self.backprop(si, sl)
				# update weights
				for layer in range(self.depth-1):
					self.weights[layer] = self.weights[layer] - learning_rate * self.delta_weights[layer]

	def feedforward_eval(self, input_data):
		for w, b in zip(self.weights, self.biases):
			input_data = sigmoid(np.dot(w, input_data) + b)
		return input_data

	def feedforward(self, input_data):
		self.outs.append(input_data)
		for w, b in zip(self.weights, self.biases):
			self.nets.append(np.dot(w, self.outs[-1]) + b)
			self.outs.append(sigmoid(self.nets[-1]))

	def backprop(self, input_data, label):
		self.dels[-1] = (self.outs[-1]-label) * self.outs[-1] * (1-self.outs[-1])

		# first round
		self.dels[-1] = self.dels[-1].reshape((self.dels[-1].size,1))
		self.outs[-2] = self.outs[-2].reshape((self.outs[-2].size,1))
		self.delta_weights[-1] = np.dot(self.dels[-1], self.outs[-2].transpose())

		for layer in range(2, self.depth):
			self.dels[-layer] = np.dot(self.weights[-layer+1].transpose(), self.dels[-layer+1]) * self.outs[-layer]*(1-self.outs[-layer])
			self.outs[-layer-1] = self.outs[-layer-1].reshape((self.outs[-layer-1].size,1))
			self.delta_weights[-layer] = np.dot(self.dels[-layer], self.outs[-layer-1].transpose())

	def evaluate(self, test_data):
		result = []
		for onedata in test_data:
			result.append(self.feedforward_eval(onedata))

		result = np.array(result)
		return result


