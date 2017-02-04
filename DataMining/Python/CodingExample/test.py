import qrcode
import png
import numpy as np

from collections import Counter

def main():
	text = "GET /jk?c=33&p=dLuY3ByNIyMt1w7rKGL8VxTnbmpMUV7+OrgPFzx8Xsg=&k=1"
	img  = qrcode.make(text)
	img.save("sss.png")

	#r = png.Reader("test.png")
	#data = np.array(list(r.read()[2]))

	'''
	shape = (450, 450) # matrix size
	dtype = np.dtype('>u2') # big-endian unsigned integer (16bit)
	fid   = open("test.png", 'rb')
	data  = np.fromfile(fid, dtype)
	print data.shape

	image = data.reshape(shape)
	print image
	'''


if __name__=="__main__":
	main()
