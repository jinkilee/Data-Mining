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


x, y = extract_data("")
num_features = 2
x = tf.placeholder("float", shape=[None, num_features])
y = tf.placeholder("float", shape=[None, 1])

wgt  = tf.Variable(tf.zeros(num_features, 1))
bias = tf.Variable(tf.zeros([1]))
yraw = tf.matmul(x, wgt) + bias
init = tf.initialize_all_variables()

# optimization
reg_loss = 0.5 * tf.reduce_sum(tf.square(wgt))

with tf.Session() as sess:
	sess.run(init)
	print sess.run(wgt)
	print sess.run(bias)
	print sess.run(reg_loss)

	'''
	for dt in data:
		dt = np.reshape(dt, (1, 2))
		print sess.run(product, feed_dict={x:dt, w:wt})
	'''

	#print [sess.run(product, feed_dict={x:dt, w:weights, b:bias}) for dt in data]













'''
with tf.Session() as sess:
	print [sess.run(tf.Tensor(xi)) for xi in x]
	#print sess.run(product, feed_dict={a:np.random.random((1, 2)), b:np.random.random((2, 1))})
	#print [sess.run(product, feed_dict={a:np.reshape(xi, (1, 2)), b:w}) for xi in x]
'''

'''
# Create 100 phony x, y data points in NumPy, y = x * 0.1 + 0.3
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

# Try to find values for W and b that compute y_data = W * x_data + b
# (We know that W should be 0.1 and b 0.3, but TensorFlow will figure that out for us.)
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b

# Minimize the mean squared errors.
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# Before starting, initialize the variables.  We will 'run' this first.
init = tf.initialize_all_variables()

# Launch the graph.
sess = tf.Session()
sess.run(init)

# Fit the line.
for step in range(201):
	sess.run(train)
	if step % 20 == 0:
		print(step, sess.run(W), sess.run(b))

# Learns best fit is W: [0.1], b: [0.3]
'''
