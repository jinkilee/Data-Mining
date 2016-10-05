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
	def __init__(self, layers, mini_batch_size):
		self.layers = layers
		self.mini_batch_size = mini_batch_size
		self.params = [param for layer in self.layers for param in layer.params]
		#self.x = T.matrix("x")
		#self.y = T.matrix("y")
		init_layer = self.layers[0]
		#init_layer.set_input(self.x, self.x, self.mini_batch_size)
		#for i in xrange(1, len(self.layers)):
			#prev_layer, layer = self.layers[j-1], self.layers[j]
			#layer.set_input(prev_layer.output, prev_layer.output_dropout, self.mini_batch_size)
		#self.output = self.layers[-1].output
		#self.output_dropout = self.layers[-1].output_dropout


class ConvPoolLayer(object):
	def __init__(self, filter_shape, image_shape, poolsize=(2, 2), activation_fn=sigmoid):
		"""
		`filter_shape` is a tuple of length 4, whose entries are the number of filters,
		the number of input feature maps, the filter height, and the filter width.

		`image_shape` is a tuple of length 4, whose entries are the mini-batch size,
		the number of input feature maps, the image height, and the image width.

		`poolsize` is a tuple of length 2, whose entries are the y and x pooling sizes.
		"""
		self.filter_shape = filter_shape
		self.image_shape = image_shape
		self.poolsize = poolsize
		self.activation_fn = activation_fn
		# initialize weights and biases
		n_out = filter_shape[0]*np.prod(filter_shape[2:])/np.prod(poolsize)
		self.w = np.asarray(np.random.normal(loc=0, scale=np.sqrt(1.0/n_out), size=filter_shape), dtype=np.float64)
		self.b = np.asarray(np.random.normal(loc=0, scale=1.0, size=(filter_shape[0],)), dtype=np.float64)
		self.params = [self.w, self.b]

	def set_input(self, inpt, inpt_dropout, mini_batch_size):
		self.inpt = inpt.reshape(self.image_shape)

		conv_out = conv.conv2d(
			input = self.inpt,
			filters = self.w,
			filter_shape = self.filter_shape,
			image_shape  = self.image_shape
		)

		print(conv_out)

		'''
		pooled_out = downsample.max_pool_2d(
			input = conv_out, 
			ds = self.poolsize, 
			ignore_border = True
		)
		self.output = self.activation_fn(pooled_out + self.b.dimshuffle('x', 0, 'x', 'x'))
		self.output_dropout = self.output # no dropout in the convolutional layers
		'''


		'''
		train_mb = theano.function(
			[i], cost, updates=updates,
			givens={
				self.x:
					training_x[i*self.mini_batch_size: (i+1)*self.mini_batch_size],
				self.y:
					training_y[i*self.mini_batch_size: (i+1)*self.mini_batch_size]
			}) 
		'''
