# -------------------- IMPORTATIONS --------------------

#standard
import os, signal






''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Processes [0.1.1] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                 Processes by I.A.

        Processes is just an utility program that allows you to manipulate
    processes a little bit more simply than standard python does. This library
    has been made from C_Processes :
                    https://github.com/iasebsil83/C_Processes

    07/03/2024 > [0.1.0] :
    - Created processes.py from processes.c/.h.
    - Created demonstration program as well.

    BUGS : .
    NOTES : .

    Contact     : i.a.sebsil83@gmail.com
    Youtube     : https://www.youtube.com/user/IAsebsil83
    GitHub repo : https://github.com/iasebsil83

    Let's Code !                                  By I.A.
******************************************************************************************

    LICENCE :

    Python_Processes
    Copyright (C) 2024 Sebastien SILVANO

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this library.

    If not, see <https://www.gnu.org/licenses/>.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''






# -------------------- PROCESSES --------------------

#custom class
class Proc:

	#some constants
	STOP_KILL = '0'
	STOP_WAIT = '1'



	#create
	def __init__(self, exePath, args):
		self.exePath = exePath
		self.args    = args
		self.pid     = 0



	#start
	def start(self):

		#launch new process
		error = os.fork()

		#cannot create fork
		if error == -1:
			raise OSError("Unable to create a subprocess (called for \"" + self.exePath + "\").")

		#fork created
		elif error == 0:
			self.pid = os.getpid()

			#launch subprocess execution
			errorCode = os.execv(self.exePath, self.args);

			#error case
			raise OSError("New subprocess [" + str(self.pid) + "] was unable to run executable \"" + self.exePath + "\" with error code (" + str(errorCode) + ").")

		#parent fork continues
		else:
			self.pid = error



	#stop
	def stop(self, mode):

		if self.pid <= 0:
			raise OSError("Invalid pid [" + str(self.pid) + "] (must be strict positive).")

		#stop process
		if mode == Proc.STOP_KILL:
			if os.kill(self.pid, signal.SIGKILL):
				raise OSError("Could not send stop signal to process.")

		elif mode != Proc.STOP_WAIT:
			raise ValueError("Invalid stop mode.")

		#wait for process reception
		if os.waitpid(self.pid, 0)[1] == -1:
			raise OSError("Problem occured when waiting for process return status.")
