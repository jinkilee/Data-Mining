import numpy as np
import math
import os
import pandas as pd
import re
import time

from collections import Counter
from sklearn import svm

# 'year', 'month', 'day', 'hour', 'min', 'second'
def preprocess_data(data):
	tmlog_list = [time.mktime(tmlog) for tmlog in data]
	return [max(tmlog_list) - min(tmlog_list), len(tmlog_list)]

# suppose 113.5.251.11 is the attacker!!
def readlog(f):
	data = {}
	data = []
	for log in f:
		log = log.split(" ")
		ip  = log[0]
		tm  = time.strptime(log[3][1:], "%d/%b/%Y:%H:%M:%S")
		data.append([ip, tm.tm_hour, tm.tm_min, tm])

	return data

def main ():
	datapath = "../data/"
	filelist = os.listdir(datapath)

	for onefile in filelist:
		data = readlog(open(datapath + onefile, "r"))

	x = []
	y = []
	data = pd.DataFrame(data=data, columns=['ip', 'hour', 'min', 'tm'])
	for k, g in data.groupby(['ip', 'hour', 'min']):
		x.append(preprocess_data(g['tm']))
		y.append(1 if '113.5.251.11' in k else 0)

	x = np.array(x)
	y = np.array(y)

	model = svm.SVC()
	model.fit(x, y)
	
	print model.predict(x)

if __name__=="__main__":
	main()
