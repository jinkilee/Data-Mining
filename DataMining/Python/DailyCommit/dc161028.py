# To execute this script,
# mpi4py should be installed preceding to openmpi or Microsoft MPI
# and then you can run with the following command line
# C:\> mpiexec -np 4 python myscript.py
# This will execute your "myscript.py" with 4 processors

import time
import os
from mpi4py import MPI


comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def func(filename):
	filename = filename.split(".")[0]
	return "hello" + filename
	
def main():
	datapath = "../data/mpitest/"
	filename =  datapath + str(rank) + ".txt"
	transtr = func(str(rank) + ".txt")
	print filename, transtr

if __name__=="__main__":
	main()
