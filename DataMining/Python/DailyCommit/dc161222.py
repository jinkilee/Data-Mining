import numpy as np
import pickle

def group_by(data, columns=None):
	allcol = data[0].keys()
	kcol   = columns
	vcol   = [c for c in allcol if c not in kcol]

	list_data = []
	for onedata in data:
		newkey = ":".join([onedata[key] for key in kcol])
		onedata['key'] = newkey
		#list_data.append(onedata.values() + [newkey])

	# get unique keys
	unikeys = np.unique([onedata['key'] for onedata in data])

	# iterate all unikeys through data
	grouped = {}
	for onekey in unikeys:
		onedf = [onedata for onedata in data if onedata['key'] == onekey]
		grouped[onekey] = {v:[df[v] for df in onedf] for v in vcol}

	return grouped.items()

def main():
	data = pickle.load(open("splunk.pkl", "rb"))
	grouped_data = group_by(data, columns=['clientip', 'date_year', 'date_month', 'date_mday', 'date_hour'])

	count = 0
	for k, v in grouped_data:
		count += len(v['_time'])
		print k, len(v['_time'])
		#print k, len(v['tm'])
		#print "-------------------------------"
	print count


if __name__ == "__main__":
	main()
