import numpy as np
import math
import os
import pandas as pd
import re
import time

from collections import Counter

'''
221.167.204.167 - - [14/Oct/2016:09:17:53 +0900] "POST /wp-cron.php?doing_wp_cron=1476404273.2678720951080322265625 HTTP/1.0" 499 0 "-" "WordPress/4.5.4; http://221.167.204.167"
212.129.62.79 - - [14/Oct/2016:09:17:53 +0900] "HEAD / HTTP/1.1" 200 0 "-" "-"
212.129.62.79 - - [14/Oct/2016:09:17:53 +0900] "GET / HTTP/1.1" 200 14177 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7"
142.54.174.85 - - [14/Oct/2016:13:53:33 +0900] "GET / HTTP/1.1" 200 14177 "-" "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)"
221.167.204.167 - - [14/Oct/2016:16:07:18 +0900] "POST /wp-cron.php?doing_wp_cron=1476428838.5240740776062011718750 HTTP/1.0" 499 0 "-" "WordPress/4.5.4; http://221.167.204.167"
141.212.122.48 - - [14/Oct/2016:16:07:18 +0900] "GET / HTTP/1.1" 200 4274 "-" "Mozilla/5.0 zgrab/0.x"
178.32.52.51 - - [14/Oct/2016:16:57:07 +0900] "GET /xmlrpc.php HTTP/1.1" 405 53 "-" "-"
142.54.174.85 - - [14/Oct/2016:17:59:59 +0900] "GET / HTTP/1.1" 200 14177 "-" "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)"
221.167.204.167 - - [14/Oct/2016:21:33:54 +0900] "POST /wp-cron.php?doing_wp_cron=1476448434.3821198940277099609375 HTTP/1.0" 499 0 "-" "WordPress/4.5.4; http://221.167.204.167"
113.5.251.11 - - [14/Oct/2016:21:33:54 +0900] "GET //wp-login.php HTTP/1.1" 200 2577 "-" "Mozilla/5.0 (X11; U; Linux i686; pt-BR; rv:1.9.0.15) Gecko/2009102815 Ubuntu/9.04 (jaunty) Firefox/3.0.15"
'''

def get_md(a):
	d = 3600./len(a)
	eq = np.array([d*i for i in range(len(a))])
	return np.average(abs(a - eq))

# 'year', 'month', 'day', 'hour', 'min', 'second'
def preprocess_data(data):
	tmlog_list = np.array([time.mktime(tmlog) for tmlog in data])
	tmlog_list = tmlog_list - tmlog_list[0]
	return [max(tmlog_list) - min(tmlog_list), len(tmlog_list), get_md(tmlog_list)]

# suppose 113.5.251.11 is the attacker!!
def readlog(f):
	data = {}
	data = []
	for log in f:
		log = log.split(" ")
		ip  = log[0]
		tm  = time.strptime(log[3][1:], "%d/%b/%Y:%H:%M:%S")

		data.append([ip, tm.tm_hour, tm])
		#data.append([ip, tm.tm_year, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec])

	return data

def main ():
	datapath = "../data/"
	filelist = os.listdir(datapath)

	for onefile in filelist:
		data = readlog(open(datapath + onefile, "r"))

	x = []
	y = []
	data = pd.DataFrame(data=data, columns=['ip', 'hour', 'tm'])
	#data = pd.DataFrame(data=data, columns=['ip', 'year', 'month', 'day', 'hour', 'min', 'second'])
	for k, g in data.groupby(['ip', 'hour']):
		x.append(preprocess_data(g['tm']))
		y.append(1 if '113.5.251.11' in k else 0)
	x = np.array(x)
	y = np.array(y)

	for row in x:
		print row
	'''

	print x.shape
	print y.shape
	print x
	print Counter(y)
	'''

if __name__=="__main__":
	main()
