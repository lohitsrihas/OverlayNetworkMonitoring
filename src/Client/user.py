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


def ping():
	try:
		os.system('ping 192.168.1.9')
		time.sleep(50)
		sys.stdout.flush()
	except KeyboardInterrupt:
		sys.exit(0)
		
def cpu():
	try:
		while 1:   
			cpu = psutil.cpu_percent()		
			print("CPU:",cpu)
			time.sleep(1)
			sys.stdout.flush()
	except KeyboardInterrupt:
		sys.exit(0)

def mem():
	try:
		while 1:
			mem = psutil.virtual_memory()
			print(mem)
			time.sleep(1)
			sys.stdout.flush()
	except KeyboardInterrupt:
		sys.exit(0)
	
def bnd():
	try:	
		while 1:
			os.system('iperf -c <server_ip_address> -p 2013')
			time.sleep(1)
			sys.stdout.flush()
	except KeyboardInterrupt:
		sys.exit(0)

def disk():
	try:	
		while 1:
			disk = psutil.disk_io_counters()
			print(disk)
			time.sleep(1)
			sys.stdout.flush()
	except KeyboardInterrupt:
		sys.exit(0)




if __name__ == '__main__':
	try:	
		p1 = multiprocessing.Process(target=ping, args=())
		p2 = multiprocessing.Process(target=cpu, args=())
		p3 = multiprocessing.Process(target=mem, args=())
		p4 = multiprocessing.Process(target=disk, args=())
		p5 = multiprocessing.Process(target=bnd, args=())

		p1.start()
		p2.start()
		p3.start()
		p4.start()
		p5.start()
	
		p1.join()
		p2.join()
		p3.join()
		p4.join()
		p5.join()
	except KeyboardInterrupt:
		print('Done')
		sys.exit(0)
