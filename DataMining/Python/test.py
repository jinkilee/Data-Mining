from __future__ import absolute_import
from __future__ import division
#from __future__ import print_function
import argparse
import pickle

# Import data
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

def main(_):
	# load raw data
	mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)

	# set dataset
	x = tf.placeholder(tf.float32, [None, 784])
	w = tf.Variable(tf.zeros([784, 10]), name='w')
	b = tf.Variable(tf.zeros([10]))
	p = tf.matmul(x, w) + b
	y = tf.placeholder(tf.float32, [None, 10])

	# define formula
	cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(p, y))
	train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

	# initialize variables  
	cnt  = 0
	sess = tf.InteractiveSession()

	# train
	tf.initialize_all_variables().run()
	for _ in range(1000):
		cnt += 1
		batch_xs, batch_ys = mnist.train.next_batch(100)
		sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})

	train_w = sess.run(w)
	train_w = train_w.transpose()
	print train_w.shape
	pickle.dump(train_w, open("train_w.pkl", "w"))

	exit()

	# test
	correct_prediction = tf.equal(tf.argmax(p, 1), tf.argmax(y, 1))
	accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
	print sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels})
	print "correct_prediction", correct_prediction
	print "accuracy", accuracy
	
if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--data_dir', type=str, default='/tmp/data', help='Directory for storing data')
	FLAGS = parser.parse_args()
	tf.app.run()
	#main()
