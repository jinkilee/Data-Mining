import numpy as np

def calculate_error(weight, label, threshold, largerthan):
	pred = [1 if i <  threshold else -1 for i in range(len(label))] if True == largerthan else [1 if i >= threshold else -1 for i in range(len(label))]
	error_list = [w if p != y else 0 for p, y, w in zip(pred, label, weight)]
	return sum(error_list), pred

def find_minimum_error_thr(weight, label, data_length):
	threshold_of_minerror = -1	# just for initialization
	min_error = 2.0			# any number that should be larger than any possible error
	pred_of_minerror = []

	# calculate minimum error
	for lt in [True, False]:	
		for threshold in range(1, data_length):
			error, pred = calculate_error(weight, label, threshold, lt)
			if min_error > error:
				min_error = error
				threshold_of_minerror = threshold
				pred_of_minerror = pred

	# get a_value here
	a = 0.5*np.log((1-min_error)/min_error)

	return min_error, threshold_of_minerror, a, np.array(pred_of_minerror)

def update_weight(min_error, threshold_of_minerror, weight, a, label, z):
	pred = [1 if i < threshold_of_minerror else -1 for i in range(len(label))]
	sign = [-1 if p == y else 1 for p, y in zip(pred, label)]

	return np.array([(w/z)*np.exp(s*a) for w, y, s in zip(weight, label, sign)])

def predict_final_label(a_list, pred_list, label):
	final_pred = np.sign(sum([a*p for a, p in zip(a_list, pred_list)]))
	return True if True == np.array_equal(final_pred, label) else False

def main():
	# empty arrays initialization
	a_list = []
	pred_list = []

	# initialize data, label, weight
	data_len = 10
	data = np.arange(data_len)
	weight = np.array([1.0/data_len]*data_len)
	label = np.sign(np.random.uniform(-1, 1, size=data_len))
	#label = np.array([1, 1, 1, -1, -1, -1, 1, 1, 1, -1])
	i = 0

	# building weak learners and find best result
	while(True):
		# find minimum error, threshold of minimum error, a and pred
		min_error, threshold_of_minerror, a, pred = find_minimum_error_thr(weight, label, len(label))

		# check if everything is correct
		a_list.append(a)
		pred_list.append(pred)
		if True == predict_final_label(a_list, pred_list, label):
			break

		# get z_value and update weight
		z = sum(weight * np.array([np.exp(-a*y*p) for y, p in zip(label, pred)]))
		weight = update_weight(min_error, threshold_of_minerror, weight, a, label, z)

		i += 1
		print("finisehd " + str(i) + "th iteration")

	print("######################################################")
	print(weight)
	print(min_error)
	print(a_list)

if __name__=="__main__":
	main()
