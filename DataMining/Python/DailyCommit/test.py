# tensorboard --logdir=/tmp/mnist_logs/ > /dev/null 2>&1 &

import argparse
import tensorflow as tf
import numpy as np

FLAGS = None

def main(_):
	epochs = 1000
	sess = tf.InteractiveSession()

	# create x and y
	x_data = np.random.random((100, 4))
	x_data[:,0] = 1.0
	weight = np.array([0.54, 0.27, 0.48, 0.38])
	y_data = x_data * weight

	numsize, numfeat = x_data.shape

	# set variables
	a = tf.Variable(tf.random_uniform([numfeat], -1.0, 1.0))

	# set formula
	x  = tf.placeholder(tf.float32, shape=[None, numfeat])
	formula = a*x

	# set squared sum of error
	with tf.name_scope('error_loss'):
		loss = tf.reduce_mean(tf.square(y_data-formula))

	# optimize formula
	opti = tf.train.GradientDescentOptimizer(0.05).minimize(loss)

	# set variables for visualizing on the tensorboard
	merged = tf.merge_all_summaries()

	# open train_writer
	train_writer = tf.train.SummaryWriter(FLAGS.summaries_dir + '/train', sess.graph)

	# initialize all variables
	init = tf.initialize_all_variables()

	# our expected answer for variable a
	print 0.54, 0.27, 0.48, 0.38
	print "----------------------"

	# run tensorflow	
	sess.run(init)
	print "Before Training", sess.run(a)

	# training for epochs times
	for i in range(epochs):
		sess.run(opti, feed_dict={x:x_data})A

	print "After Training", sess.run(a)

	# close train_writer
	train_writer.close()

if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--fake_data', nargs='?', const=True, type=bool, default=False, help='If true, uses fake data for unit testing.')
	parser.add_argument('--max_steps', type=int, default=1000, help='Number of steps to run trainer.')
	parser.add_argument('--learning_rate', type=float, default=0.001, help='Initial learning rate')
	parser.add_argument('--dropout', type=float, default=0.9, help='Keep probability for training dropout.')
	parser.add_argument('--data_dir', type=str, default='/tmp/data', help='Directory for storing data')
	parser.add_argument('--summaries_dir', type=str, default='/tmp/mnist_logs', help='Summaries directory')
	FLAGS = parser.parse_args()
	tf.app.run()
	#main()
