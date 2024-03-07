#!/usr/bin/python3




# -------- IMPORTATIONS --------

#system
import os
os.sys.path.append("../lib")

#delay
import time

#processes
from processes import Proc






# -------- EXECUTION --------

#main
def main():
	spid  = str(os.getpid())
	sppid = str(os.getppid())

	#presentation
	print("I.A. > PID[" + spid + "], PPID[" + sppid + "] : This is a basic example of process management using \"processes.py\".")

	#create subprocess 1
	print("I.A. > PID[" + spid + "], PPID[" + sppid + "] : Creating process 1.")
	p1 = Proc("/usr/bin/python3", ["python3", "program1.py", "2", "25"])

	#create subprocess 2
	print("I.A. > PID[" + spid + "], PPID[" + sppid + "] : Creating process 2.")
	p2 = Proc("/usr/bin/python3", ["python3", "program2.py", "22", "35"])



	#start subprocess 1
	print("I.A. > PID[" + spid + "], PPID[" + sppid + "] : Starting process 1 (\"/usr/bin/python3\" with command \"python3 program1.py 2 25\").")
	p1.start()

	#sleep 2s
	time.sleep(2)

	#start subprocess 2
	print("I.A. > PID[" + spid + "], PPID[" + sppid + "] : Starting process 2 (\"/usr/bin/python3\" with command \"python3 program2.py 22 35\").")
	p2.start()

	#sleep 10s
	time.sleep(10)



	#stop subprocess 1
	print("I.A. > PID[" + spid + "], PPID[" + sppid + "] : Stopping process 1 in \"kill\" mode.")
	p1.stop(Proc.STOP_KILL)
	print("I.A. > PID[" + spid + "], PPID[" + sppid + "] : Process 1 stopped.")

	#sleep 4s
	time.sleep(4)

	#stop subprocess 2
	print("I.A. > PID[" + spid + "], PPID[" + sppid + "] : Stopping process 2 in \"wait\" mode.")
	p2.stop(Proc.STOP_WAIT)
	print("I.A. > PID[" + spid + "], PPID[" + sppid + "] : Process 2 stopped.")

main()
