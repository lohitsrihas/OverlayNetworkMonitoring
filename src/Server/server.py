import psutil
import os
import subprocess
import time
import datetime
import random
import argparse
import subprocess
import re
import sys
from threading import Thread
from SocketServer import ThreadingMixIn
import multiprocessing
import socket
from subprocess import STDOUT, PIPE, Popen

def bnd():
	try:	
		while 1:
# Change the port from 2005 to any other port while running in order avoid error with bandwidth
			os.system('iperf -s -p 2005') 
			time.sleep(9)
			sys.stdout.flush()
	except KeyboardInterrupt:
		sys.exit(0)

if __name__ == '__main__':
	try:
		p1 = multiprocessing.Process(target=bnd, args=())
		p1.start()	
		p1.join()
	except KeyboardInterrupt:	
		print('Done')
		sys.exit(0)
