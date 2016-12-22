import numpy as np

def main():
	# set data
	c1 = np.sort(np.random.randint(0, 50, 100))
	c2 = np.sort(np.random.randint(0, 100, 100))
	c3 = np.array([1]*30 + [2]*70)
	c4 = np.array([1]*20 + [2]*30 + [3]*30 + [4]*20)
	np.random.shuffle(c3)
	np.random.shuffle(c4)
	data = np.array([c3, c1, c4, c2]).T
	print data[:20]
	print "----------------------------"
	#data = np.array([c1, c2, c3, c4]).T
	
	# get mean and subtract from the data
	mean = np.array([np.mean(c3), np.mean(c1), np.mean(c4), np.mean(c2)])
	#mean = np.array([np.mean(c1), np.mean(c2), np.mean(c3), np.mean(c4)])
	newdata = data - mean

	# calculate the covariance matrix
	covdata = np.cov(newdata.T)

	# calculate the eigenvectors and eigenvalues of the covariance matrix
	evalue, evector = np.linalg.eig(covdata)

	# sort evector and evalue into descending order
	sortidx = np.argsort(evalue)[::-1]
	evector = evector[sortidx]
	evalue  = evalue[sortidx]

	# choose ndim and get new data
	ndim = 2
	newdata = np.dot(evector[:ndim], newdata.T).T

	print newdata[:20]
	#xxx = (ndim,4)
	#newdata = (4,100)
	
if __name__=="__main__":
	main()
