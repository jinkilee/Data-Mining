class CodingExample:
	@staticmethod
	def is_anagrams(a, b):
		if sorted(a) == sorted(b):
			return True
		else:
			return False

	@staticmethod
	def is_palindrome(sentence):
		hidx = 0
		tidx = len(sentence) - 1
		sentence = sentence.lower()
		while(hidx <= tidx):
			# head check
			if(False == sentence[hidx].isalpha()):
				hidx += 1
				continue

			# tail check
			if(False == sentence[tidx].isalpha()):
				tidx -= 1
				continue

			# check if palindrome
			if sentence[hidx] != sentence[tidx]:
				return False

			hidx += 1
			tidx -= 1

		return True


def main():
	#print(CodingExample.is_anagrams('arthorse', 'orchestra'))
	#print(CodingExample.is_palindrome('Neelsees Leon.'))

if __name__ == "__main__":
	main()
