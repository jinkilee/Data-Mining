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

	# set variables
	x = tf.placeholder("float", shape=[None, numfeat])
	y = tf.placeholder("float", shape=[None, 1])
	wgt  = tf.Variable(tf.zeros([numfeat, 1]))
	bias = tf.Variable(tf.zeros([1]))
	yraw = tf.matmul(x, wgt) + bias

	# initialize variables
	init = tf.initialize_all_variables()

	# set optimization function
	reg_loss = 0.5 * tf.reduce_sum(tf.square(wgt))
	hng_loss = svmC * tf.reduce_sum(tf.maximum(tf.zeros([tf.minimum(BATCH_SIZE, REAL_SIZE), 1]), 1 - y*yraw))
	svm_loss = reg_loss + hng_loss
	min_loss = tf.train.GradientDescentOptimizer(0.01).minimize(svm_loss)

	# set prediction function
	pred = tf.sign(yraw)
	corr = tf.equal(y, pred)
	pred_type = tf.reduce_mean(tf.cast(corr, "float"))

	# run everything
	with tf.Session() as sess:
		sess.run(init)

		# before training
		print sess.run(pred_type, feed_dict={x:data, y:label})

		# training
		for step in xrange(EPOCHS * datasize / BATCH_SIZE):
			offset = (step * BATCH_SIZE) % datasize
			batch_data  = data[offset:offset+BATCH_SIZE]
			batch_label = label[offset:offset+BATCH_SIZE]
			realsize = batch_label.shape[0]
			sess.run(min_loss, feed_dict={x:batch_data, y:batch_label, REAL_SIZE:realsize})

		# after training
		print sess.run(pred_type, feed_dict={x:data, y:label})

if __name__ == "__main__":
	main()

