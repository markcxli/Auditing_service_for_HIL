
from client import AuditClient
#import hil.hil.cli
import time
import datetime
import sqlite3
import os
import subprocess

import itertools, sys

#data = str(raw_input(''))
#	if len(data) > 0:
#		print ("this is curren num:" + str(num))
#subprocess.call(["python", "print.py"])
#print ("main process worked")


#### SERVER 1  daemon  #######################

# 1 READ FROM HIL DB
# 2 READ FROM update_checker DB
# 3 detect changes 
# 4 write new changes to update_checker DB

#### SERVER 2 #######################
# READ FROM update_checker DB, print results

# package 



last_list_node_info = {}

conn = sqlite3.connect('HIL_updates.db')
c=conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS recent_updates(m_time TEXT , node TEXT,  switch, TEXT)')

spinner = itertools.cycle(['-', '/', '|', '\\'])

def do_something():
	global last_list_node_info
	# Collect all data from the hil database and our switch data
	nodes = AuditClient().list_nodes("all")
	projects = AuditClient().list_projects()
	list_node_info = {}
	for n in nodes:
		node_info = AuditClient().get_node_info(n)
		list_node_info[n] = node_info
		if last_list_node_info.has_key(n):
#		list_node_info[n]["switch"] = AuditClient().list_switch_vlans(n)
#	if (not last_list_node_info):
#		last_list_node_info = list_node_info
#		print list_node_info
			#if (last_list_node_info[n] == list_node_info[n]):
			pass
		else:
			# just make a string of all the node names
			m_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			c.execute('INSERT INTO recent_updates (m_time, node, switch) VALUES (?, ?, ?)', (m_time, n,n))
			print ("new change: "+m_time+' '+n+' '+" ".join(list_node_info[n]))

			conn.commit()

			last_list_node_info = list_node_info
	sys.stdout.write(spinner.next())  # write the next character
	sys.stdout.flush()                # flush stdout buffer (actual character display)
	sys.stdout.write('\b')            # erase the last written char

def run_server():
	while True:
		do_something()
		time.sleep(1)

if __name__ == "__main__":
	run_server()



