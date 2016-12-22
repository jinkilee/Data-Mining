import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

def main():
	epochs = 400

	# create data
	data = np.random.random((100,4))
	data[:,0] = 1.0
	weight = np.array([0.54, 0.27, 0.48, 0.38])
	y = data * weight
	numsize, numfeat = data.shape

	x = tf.placeholder(tf.float32, shape=[None, numfeat])
	a = tf.Variable(tf.random_uniform([numfeat], -1.0, 1.0))
	formula = a * x

	#loss = tf.reduce_sum(tf.square(y-formula))
	loss = tf.reduce_mean(tf.square(y-formula))
	opti = tf.train.GradientDescentOptimizer(0.5).minimize(loss)

	init = tf.initialize_all_variables()

	# run tensorflow
	with tf.Session() as sess:
		sess.run(init)

		# train formula
		print "Before Training", sess.run(a)
		for i in range(epochs):
			sess.run(opti, feed_dict={x:data})
			print i, "th loss", sess.run(loss, feed_dict={x:data})
		print "After Training", sess.run(a)

if __name__=="__main__":
	main()
