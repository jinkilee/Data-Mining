import tensorflow as tf
import numpy as np

#a = tf.placeholder(tf.float32, shape=(10, 10))
#b = tf.placeholder(tf.float32, shape=(10, 10))

#a = tf.placeholder_with_default([[1,2,3,4,5,6], [1,2,3,4,5,6]] , [2, 6])
#b = tf.placeholder_with_default([[1,2], [1,2], [1,2], [1,2], [1,2], [1,2]] , [6, 2])

#x = tf.Variable(np.random.random((1, 2)))
data  = [[1, 2],[2, 1],[1, 1],[2, 2],[8, 8],[9, 9],[8, 9],[9, 8]]
data  = np.reshape(data, (len(data), 1, 2))
label = [-1, -1, -1, -1, 1, 1, 1, 1]

x = tf.placeholder(tf.float32, shape=(1, 2))
w = tf.placeholder(tf.float32, shape=(2, 1))
#b = tf.placeholder(tf.float32, shape=(1, 1))
product = tf.matmul(x, w)

weights = tf.Variable(tf.random_normal([2, 1], stddev=0.35), name="weights")
bias    = tf.Variable(tf.zeros([1, 1]), name="biases")
init = tf.initialize_all_variables()

with tf.Session() as sess:
	sess.run(init)
	#xi = np.random.rand(1, 2)
	#yi = np.random.rand(2, 1)
	#print sess.run(product, feed_dict={x:xi, y:yi})

	'''
	for dt in data:
		dt = np.reshape(dt, (1, 2))
		print sess.run(product, feed_dict={x:dt, w:wt})
	'''
	print sess.run(weights)
	print sess.run(bias)

	for dt in data:
		print dt
		print sess.run(product, feed_dict={x:dt, w:weights})
		#sess.run(product, feed_dict={x:dt, w:weights, b:bias})

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
