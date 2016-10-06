import numpy as np
import math
import time
import network

def main():
	# Load data
	train, validation, test = network.load_data_shared()
	train_data, train_label = train
	validation_data, validation_label = validation
	test_data, test_label = test

	net = network.network(train_data, (len(train_data), 28,28), (5,5))

if __name__=="__main__":
	main()
