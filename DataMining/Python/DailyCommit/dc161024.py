import pickle
import numpy as np
import matplotlib.pyplot as plt

def draw_plot(blue, red, black):
	plt.figure('abc', figsize=(2, 1.5))
	plt.scatter(blue[:,1], blue[:,0], c='blue', zorder=10, cmap=plt.cm.Paired)		# scatter blue
	plt.scatter(red[:,1], red[:,0], c='red', zorder=10, cmap=plt.cm.Paired)			# scatter red
	plt.scatter(black[:,1], black[:,0], c='black',  zorder=10, cmap=plt.cm.Paired)	# scatter black
	plt.axis('tight')
	
	plt.show()

def main():
	train_w = pickle.load(open("train_w.pkl", "r"))
	
	for i in range(10):
		weight = train_w[i]
		weight = weight.reshape((28,28))
	
		pos_blue = []
		neg_red = []
		zero_black = []
		for row in range(28):
			for col in range(28):
				if 0 < weight[row][col]:
					pos_blue.append([row, col])
				elif 0 > weight[row][col]:
					neg_red.append([row, col])
				else:
					zero_black.append([row, col])
				
		pos_blue = np.array(pos_blue)
		neg_red = np.array(neg_red)		
		zero_black = np.array(zero_black)
	
		draw_plot(pos_blue, neg_red, zero_black)
	
	#print weight
	
if __name__=="__main__":
	main()
