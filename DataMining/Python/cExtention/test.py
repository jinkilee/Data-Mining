import _chi2
import numpy as np
import time

'''
data = _chi2.readfile("c.txt")
data = np.array(data)
print data.shape
'''


#b = _chi2.readfile("b.txt")

#'''
def readlog(f):
	data = []
	
	for log in f:
		log  = log.split(" ")
		ip   = log[0]
		tm   = log[3][1:]
		page = log[6]
		tm   = time.strptime(log[3][1:], "%d/%b/%Y:%H:%M:%S")
		page = log[6].split("?")[0].split("/")[-1]
		data.append([ip, tm.tm_year, tm.tm_mon, tm.tm_mday, tm.tm_hour, time.mktime(tm), page])
		
	return data


data = readlog(open("c.txt", "r"))
data = np.array(data)
print data.shape
#'''
