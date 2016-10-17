# tensorflow reference : https://www.tensorflow.org/versions/r0.11/get_started/basic_usage.html

import numpy as np
import tensorflow as tf
import time

####################################################
# All of the basics including dot-product multiplication comparison between tensorflow and numpy
'''
row = 1000
mid = 2000
col = 1000

# execute ops that do not need any input
# that is, create constant Tensor objects
mat1 = tf.random_normal([row, mid])		# 1x2 matrix
mat2 = tf.random_normal([mid, col])		# 2x1 matrix

# create an ops that does something with the Tensors 
product = tf.matmul(mat1, mat2)

# launch a graph to actually execute ops
session = tf.Session()

# unlike normal programming function,
# we don't need to provide arguments explicitly.
# it automatically adds Tensor arguments.
result = session.run(product)		# result is numpy array

# close session
session.close()

# to forget about closing session,
# we can use 'with' block
start = time.time()
with tf.Session() as session:
	result = session.run(product)
end   = time.time()
print end - start

mat1 = np.random.rand(row, mid)
mat2 = np.random.rand(mid, col)

# numpy dot
start = time.time()
c = np.dot(mat1, mat2)
end   = time.time()
print end - start
'''

####################################################
# Variable example
'''
# assign values
state = tf.Variable(0, "counter")
one = tf.constant(1)
new_value = tf.add(state, one)
update    = tf.assign(state, new_value)

# initialize variable with tf.initialize_all_variables() ops
init_op = tf.initialize_all_variables()

# launch graph
with tf.Session() as session:
	session.run(init_op)
	print session.run(state)	# this should be run after init_op because it is a variable
	print session.run(one)		# this can be run without running init_op because it is just a constant

	for _ in range(3):
		session.run(update)
		print session.run(state)
'''

####################################################
# Fetch example
'''
# create constant ops
input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)

# create ops with input1, input2 and input3
interv = tf.add(input2, input3)
result = tf.mul(input1, interv)

# launch interv and result on the graph
with tf.Session() as session:
	result = session.run([interv, result])
	print result
	print len(result)
	print result[0], result[1]
'''

####################################################
# Fetch example
input1 = tf.placeholder(tf.float32)	# should be fed directly on the run()
input2 = tf.placeholder(tf.float32)	# should be fed directly on the run()
output = tf.mul(input1, input2)

with tf.Session() as session:
	result = session.run([output], feed_dict={input1:[7.], input2:[2.]})
	print type(result)
