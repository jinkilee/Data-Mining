import preprocess
import tensorflow as tf
import numpy as np

from collections import Counter

# configure svm
svmC   = 0.1
EPOCHS = 100
BATCH_SIZE = 10
REAL_SIZE  = tf.placeholder(tf.int32)

def main():
	# get dataset
	data, label, ip = preprocess.get_data("../data/")
	data = data[:, :3]
	datasize, numfeat = data.shape

if __name__ == "__main__":
	main()

