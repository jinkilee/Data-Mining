'''
#######################################################
# fib.pyx
def fib(n):
    """Print the Fibonacci series up to n."""
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a + b

#######################################################
# setup.py
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_models = cythonize("fib.pyx"))

shell> python setup.py build_ext --inplace

#######################################################
# test.py
import fib
fib.fib(2000)
'''

import numpy as np
import dot
import time

def main():
	row = 1000
	mid = 2000
	col = 1000
	a = np.random.rand(row, mid)
	b = np.random.rand(mid, col)
	#c = np.zeros((row, col))

	# method1
	start = time.time()
	c1    = dot.dot1(a, b)
	end   = time.time()
	t1    =end - start

	# method2
	start = time.time()
	c2    = dot.dot2(a, b)
	end   = time.time()
	t2    =end - start

	# method3
	start = time.time()
	c3    = np.dot(a, b)
	end   = time.time()
	t3    =end - start

	print "dot1", t1
	print "dot2", t2
	print "dot3", t3
	print t1/t2, t2/t3
	
if __name__ == "__main__":
	main()
