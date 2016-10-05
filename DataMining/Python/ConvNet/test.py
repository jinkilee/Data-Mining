import numpy as np
import math
import time
import network

from network import ConvPoolLayer

def main():
	mini_batch_size = 10
	net = ConvPoolLayer(image_shape=(mini_batch_size, 1, 28, 28), filter_shape=(20, 1, 5, 5), poolsize=(2, 2))

if __name__=="__main__":
	main()
