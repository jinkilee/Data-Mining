import numpy as np
import gzip
import cPickle

from theano.tensor.nnet import conv

def load_data_shared(filename="mnist.pkl.gz"):
	f = gzip.open(filename, 'rb')
	train_data, validation_data, test_data = cPickle.load(f)
	f.close()

	def shared(data):
		shared_x = np.asarray(data[0], dtype=np.float64)
        	shared_y = np.asarray(data[1], dtype=np.int64)

        	return shared_x, shared_y

	return [shared(train_data), shared(validation_data), shared(test_data)]

def sigmoid():
	print("sigmoid")

class network(object):
	def __init__(self, input_data, input_size, loc_size):
		# reshape data into size
		self.input_data = np.reshape(input_data, input_size)
		self.weight = np.random.random(loc_size)
		print(self.weight.shape)
