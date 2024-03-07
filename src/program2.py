#!/usr/bin/python3




# -------- IMPORTATIONS --------

#system
import os, sys

#delay
import time






# -------- EXECUTION --------

#main
def main(args):
	spid  = str(os.getpid())
	sppid = str(os.getppid())

	#get arguments
	low  = int(args[1])
	high = int(args[2])
	print("P1 > PID[" + spid + "], PPID[" + sppid + "] : Counting from " + str(low) + " to " + str(high) + ".")

	#count from low to high
	for i in range(low, high):
		print("P1 > PID[" + spid + "], PPID[" + sppid + "] : " + str(i) + ".")
		time.sleep(1)

main(sys.argv)
