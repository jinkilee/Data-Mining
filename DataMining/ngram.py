from __future__ import division
from collections import Counter, OrderedDict

def unigram(text):
	count_all = Counter()
	terms_all = [term for term in text.split()]
	count_all.update(terms_all)
	for i, j in count_all.items():
		count_all[i] = j/len(terms_all)
	return {i[0]: i[1] for i in count_all.items()}

def bigrams(text):
	uni_count = Counter([u for u in text.split()])
	bi_count = Counter([b for b in zip(text.split()[:-1], text.split()[1:])])
	for i, j in bi_count.items():
		bi_count[i] = j/uni_count[i[0]]
	return {i[0]: i[1] for i in bi_count.items()}

def main():
	text = "I love CS and I love SJ and SJ also loves me"
	print(bigrams(text))

if __name__=="__main__":
	main()
