import numpy as np
import math
import time
import network

from network import ConvPoolLayer

def main():
	# Load data
	train, validation, test = network.load_data_shared()
	train_data, train_label = train
	validation_data, validation_label = validation
	test_data, test_label = test

	# Set ConvPoolLayer
	mini_batch_size = 10
	net = ConvPoolLayer(image_shape=(mini_batch_size, 1, 28, 28), filter_shape=(20, 1, 5, 5), poolsize=(2, 2))
	net.set_input(train_data[:mini_batch_size], train_data[:mini_batch_size], mini_batch_size)

if __name__=="__main__":
	main()
