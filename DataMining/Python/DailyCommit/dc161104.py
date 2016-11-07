import numpy as np

def main():
	for i in range(10):
		a = np.random.randint(100, 999)
		b = np.random.randint(100, 999)
		print str(i) + ")", a, "+", b

if __name__=="__main__":
	main()
