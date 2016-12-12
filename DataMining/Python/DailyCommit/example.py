
import tensorflow as tf

# define placeholder
phd_x = tf.placeholder(tf.int32, shape=(2, 3))
phd_f = phd_x + 1

# to print constant
with tf.Session() as sess:
	# feed_dict MUST BE USED to feed phd_x into phd_f
	# feed_dict has a form of python dictionary 
	print sess.run(phd_f, feed_dict={phd_x:[[1, 2, 3],[4, 5, 6]]})
	


'''

'''
