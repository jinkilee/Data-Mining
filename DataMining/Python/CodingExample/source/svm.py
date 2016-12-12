
#from __future__ import absolute_import
#from __future__ import division
#from __future__ import print_function

import preprocess
import tensorflow as tf
import numpy as np
import argparse

from collections import Counter
from tensorflow.examples.tutorials.mnist import input_data

# configure svm
svmC   = 0.1
EPOCHS = 100
BATCH_SIZE = 10
REAL_SIZE  = tf.placeholder(tf.int32)

# get dataset
data, label, iplist = preprocess.get_data("../data/")
datasize, numfeat = data.shape

# split dataset
idx = len(data)/3
x_train, y_train, ip_train = data[idx:], label[idx:], iplist[idx:]
x_test, y_test, ip_test = data[:idx], label[:idx], iplist[:idx]

def train_data():
	datalen = len(x_train)
	return {
		'example_id': tf.constant([str(i) for i in range(datalen)]),
		'f0': tf.constant(x_train[:,0]),
		'f1': tf.constant(x_train[:,1]),
		'f2': tf.constant(x_train[:,2]),
		'f3': tf.constant(x_train[:,3]),
	}, tf.constant(y_train)

def test_data():
	datalen = len(x_test)
	return {
          'example_id': tf.constant([str(i) for i in range(datalen)]),
		'example_id': tf.constant([str(i) for i in range(datalen)]),
		'f0': tf.constant(x_test[:,0]),
		'f1': tf.constant(x_test[:,1]),
		'f2': tf.constant(x_test[:,2]),
		'f3': tf.constant(x_test[:,3]),
	}, tf.constant(y_test)

def main(_):
	if tf.gfile.Exists(FLAGS.summaries_dir):
		tf.gfile.DeleteRecursively(FLAGS.summaries_dir)
	tf.gfile.MakeDirs(FLAGS.summaries_dir)

	f0 = tf.contrib.layers.real_valued_column('f0')
	f1 = tf.contrib.layers.real_valued_column('f1')
	f2 = tf.contrib.layers.real_valued_column('f2')
	f3 = tf.contrib.layers.real_valued_column('f3')

	model = tf.contrib.learn.SVM(feature_columns=[f0, f1, f2, f3], example_id_column='example_id', l1_regularization=0.0, l2_regularization=0.0)
	model.fit(input_fn=train_data, steps=300)
	metrics = model.evaluate(input_fn=test_data, steps=1)
	loss = metrics['loss']
	accuracy = metrics['accuracy']

	print loss
	print accuracy
	exit()

	# train dataset
	#monitor = tf.contrib.learn.python.learn.monitors.ValidationMonitor(x_test, y_test, 2)
	#model = skflow.TensorFlowLinearClassifier(n_classes=2, steps=2000)
	#model.fit(x_train, y_train, logdir='/tmp/abusing/')
	#pred = model.predict(x_test)

	'''################################################################################
	# set variables
	x = tf.placeholder("float", shape=[None, numfeat])
	y = tf.placeholder("float", shape=[None, 1])
	wgt  = tf.Variable(tf.zeros([numfeat, 1]))
	bias = tf.Variable(tf.zeros([1]))
	yraw = tf.matmul(x, wgt) + bias

	# open tensorflow session
	sess = tf.InteractiveSession()

	# initialize variables
	init = tf.initialize_all_variables()

	# set optimization function
	reg_loss = 0.5 * tf.reduce_sum(tf.square(wgt))
	hng_loss = svmC * tf.reduce_sum(tf.maximum(tf.zeros([tf.minimum(BATCH_SIZE, REAL_SIZE), 1]), 1 - y*yraw))
	svm_loss = reg_loss + hng_loss
	min_loss = tf.train.GradientDescentOptimizer(0.01).minimize(svm_loss)

	with tf.name_scope('accuracy'):
		# set prediction function
		pred = tf.sign(yraw)
		corr = tf.equal(y, pred)
		accuracy = tf.reduce_mean(tf.cast(corr, "float"))
		tf.scalar_summary('accuracy', accuracy)

	# configure tensorboard setting
	merged = tf.merge_all_summaries()
	train_writer = tf.train.SummaryWriter(FLAGS.summaries_dir, sess.graph)

	# run 'initialize_all_variables()'
	sess.run(init)

	# before training
	acc = sess.run(accuracy, feed_dict={x:data, y:label})
	print "accuracy : ", acc

	# start training
	for step in xrange(1, EPOCHS * datasize / BATCH_SIZE):
		# train data
		offset = (step * BATCH_SIZE) % datasize
		batch_data  = data[offset:offset+BATCH_SIZE]
		batch_label = label[offset:offset+BATCH_SIZE]
		realsize = batch_label.shape[0]
		sess.run(min_loss, feed_dict={x:batch_data, y:batch_label, REAL_SIZE:realsize})

		# add summary	
		summary, acc = sess.run([merged, accuracy], feed_dict={x:data, y:label, REAL_SIZE:realsize})
		train_writer.add_summary(summary, step)

		# print accuracy and loss
		print "accuracy : ", acc

	# after training
	acc = sess.run(accuracy, feed_dict={x:data, y:label})
	print "accuracy : ", acc

	# close train_writer
	#train_writer.close()
	################################################################################'''

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--fake_data', nargs='?', const=True, type=bool, default=False, help='If true, uses fake data for unit testing.')
	parser.add_argument('--max_steps', type=int, default=1000, help='Number of steps to run trainer.')
	parser.add_argument('--learning_rate', type=float, default=0.001, help='Initial learning rate')
	parser.add_argument('--dropout', type=float, default=0.9, help='Keep probability for training dropout.')
	parser.add_argument('--data_dir', type=str, default='/tmp/data', help='Directory for storing data')
	parser.add_argument('--summaries_dir', type=str, default='/tmp/mnist_logs', help='Summaries directory')
	FLAGS = parser.parse_args()
	tf.app.run()

