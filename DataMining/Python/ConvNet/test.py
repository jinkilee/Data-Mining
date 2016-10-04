import numpy as np
import math
import time

def main ():
	n = 999999
	a = np.random.randint(0, 10, n)
	b = np.array([2] * n)
	bs= 2.0

	######################################################################################
	# broadcasting example1
	for i in range(10):
		"""
		Normally time1 is supposed to be slower because time2 take computational advantage due to broadcasting concept.
		As 'bs = 2.0' was declared, 'c = a * bs' will use broadcasting.
		Broadcasting is implemented to use C looping instead of Python looping
		"""
		# time1
		start = time.time()
		c = a * b
		end   = time.time()
		time1 = (end - start)

		# time2
		start = time.time()
		c = a * bs
		end   = time.time()
		time2 = (end - start)

		if time1 < time2:
			print("not always")

	######################################################################################
	# broadcasting example2
	n1 = 1000
	n2 = 2000
	x  = np.arange(n1)	# [0,1,2,3]
	xx = x.reshape(n1,1)
	y  = np.ones(n2)
	z  = np.ones((n2,n1))

	'''
	for i in range(10):
		# time3 is much much much faster than time1 and time2, since it uses broadcasting
		# time1
		start = time.time()
		result1 = []
		for i in x:
			result1.append([i+j for j in y])
		result1 = np.array(result1)
		end   = time.time()
		time1 = (end - start)

		# time2
		start = time.time()
		result2 = np.array([[i+j for j in y] for i in x])
		end   = time.time()
		time2 = (end - start)

		# time3
		start = time.time()
		result3 = xx + y
		end   = time.time()
		time3 = (end - start)

		#print(time1, time2, time3)
	'''

	######################################################################################
	# broadcasting example3
	for i in range(10):
		# time1
		start = time.time()
		result1 = []
		for i in z:
			result1.append([j1 + j2 for j1, j2 in zip(i, x)])
		result1 = np.array(result1)
		end   = time.time()
		time1 = (end - start)

		# time2
		start = time.time()
		result2 = z + x
		end   = time.time()
		time2 = (end - start)

		print(time1, time2)

if __name__=="__main__":
	main()
