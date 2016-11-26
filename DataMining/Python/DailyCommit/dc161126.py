import tensorflow as tf
import numpy as np

def extract_data(filename):
	out = np.loadtxt(filename, delimiter=',');

	# Arrays to hold the labels and feature vectors.
	labels = out[:,0]
	labels = labels.reshape(labels.size,1)
	fvecs = out[:,1:]

	# Return a pair of the feature matrix and the one-hot label matrix.
	return fvecs,labels

# configure svm
svmC = 0.1
BATCH_SIZE   = 100
num_epochs   = 100
num_features = 2

# load data
train_data, train_label = extract_data("../data/data.csv")
train_size, num_features = train_data.shape	# 1000, 2
train_label[train_label==0] = -1

x = tf.placeholder("float", shape=[None, num_features])
y = tf.placeholder("float", shape=[None, 1])

wgt  = tf.Variable(tf.zeros([num_features, 1]))
bias = tf.Variable(tf.zeros([1]))
yraw = tf.matmul(x, wgt) + bias
init = tf.initialize_all_variables()

# optimization
reg_loss = 0.5 * tf.reduce_sum(tf.square(wgt))
hng_loss = svmC * tf.reduce_sum(tf.maximum(tf.zeros([BATCH_SIZE, 1]), 1 - y*yraw))
svm_loss = reg_loss + hng_loss
min_loss = tf.train.GradientDescentOptimizer(0.01).minimize(svm_loss)

# evaluation
pred = tf.sign(yraw)
corr = tf.equal(y, pred)
pred_type = tf.reduce_mean(tf.cast(corr, "float"))

with tf.Session() as sess:
	sess.run(init)

	# before training
	print sess.run(pred_type, feed_dict={x:train_data, y:train_label})

	# training
	for step in xrange(num_epochs * train_size / BATCH_SIZE):
		offset = (step * BATCH_SIZE) % train_size
		batch_data  = train_data[offset:offset+BATCH_SIZE]
		batch_label = train_label[offset:offset+BATCH_SIZE]
		sess.run(min_loss, feed_dict={x:batch_data, y:batch_label})

	# after training
	print sess.run(pred_type, feed_dict={x:train_data, y:train_label})

