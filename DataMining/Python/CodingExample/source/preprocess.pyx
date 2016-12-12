import numpy as np
import pandas as pd
import time, os
import scipy.stats

ndist_list = []		# list used for normalization

def shuffle_data(x, y):
	idx = range(len(x))
	np.random.shuffle(idx)
	return x[idx], y[idx]
	
def dopage_rate(url_list):
	dofile_list = [url for url in url_list if url[-2:] == 'do']
	return len(dofile_list)/float(len(url_list))
	
def frequency(data):
	data = np.asarray(data, dtype=int)
	data = np.asarray(np.bincount(data))
	data = data / float(data.sum())

	return np.std(data)

def get_mad(data):
	# https://en.wikipedia.org/wiki/Median_absolute_deviation
	dif = data - np.median(data)
	return np.std(dif * dif)
	
def readlog(f):
	data = []
	
	for log in f:
		log  = log.split(" ")
		ip   = log[0]
		tm   = time.strptime(log[3][1:], "%d/%b/%Y:%H:%M:%S")
		page = log[6].split("?")[0].split("/")[-1]
		data.append([ip, tm.tm_year, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm, page])
		
	return data
	
def get_data(datapath, train=True):
	filelist = os.listdir(datapath)

	# preprocess data and create x and y to build a model
	x = []
	y = []
	for onefile in filelist:
		data = readlog(open(datapath + onefile, "r"))

		data = pd.DataFrame(data=data, columns=['ip', 'year', 'month', 'day', 'hour', 'tm', 'page'])
		for k, g in data.groupby(['ip', 'year', 'month', 'day', 'hour']):
			x.append(preprocess_data(k[0], g['tm'], g['page']))
			if True == train:
				y.append([k[0],1] if '221.167.204.167' in k else [k[0],0])
			else:
				y.append(k[0])
	x = np.array(x)
	y = np.array(y)
	
	# transform to pandas array
	x = pd.DataFrame(data=x, columns=['ip', 'max-min', 'log_cnt', 'frequency', 'mad', 'do_rate'])
	x = np.array(x[['log_cnt', 'frequency', 'mad', 'do_rate']])
	x = x.astype('float')

	datasize, numfeat = x.shape
	x , y = shuffle_data(x, y)	
	ip, y = y[:,0], y[:,1]
	y = np.array([int(i) for i in y])
	ip, y = ip.reshape((datasize, 1)), y.reshape((datasize, 1))
	return x, y, ip

def preprocess_data(ip, time_data, url_list):
	tmlog_list = np.array([time.mktime(tmlog) for tmlog in time_data])
	tmlog_list = tmlog_list % 3600
	return [ip, tmlog_list[-1] - tmlog_list[0], tmlog_list.shape[0], frequency(tmlog_list), get_mad(tmlog_list), dopage_rate(url_list)]
	
def normalize_data(data, train=True):
	nfeature = data.shape[1]
	
	if True == train:
		# create normal distribution of each feature
		for i in range(nfeature):
			avg = np.median(data[:, i])
			std = np.std(data[:, i])
			ndist = scipy.stats.norm(avg, std)
			ndist_list.append(ndist)
		
	# normalize data
	new_data = []
	for onedata in data:
		new_data.append([ndist_list[i].cdf(onedata[i]) for i in range(nfeature)])
	
	return np.array(new_data)

#x, y, ip = get_data("../data/")
