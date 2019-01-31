from audit_rest.client import AuditClient
import time
import datetime

last_list_node_info = {}

def do_something():
	global last_list_node_info
	# Collect all data from the hil database and our switch data
	nodes = AuditClient().list_nodes("all")
	projects = AuditClient().list_projects()
	list_node_info = {}
	for n in nodes:
		node_info = AuditClient().get_node_info(n)
		list_node_info[n] = node_info
		list_node_info[n]["switch"] = AuditClient().list_switch_vlans(n)
#	if (not last_list_node_info):
#		last_list_node_info = list_node_info
#		print list_node_info
	if (last_list_node_info == list_node_info):
		print True
	else:
		last_list_node_info = list_node_info
		print datetime.datetime.today() , " : " , list_node_info

def run_server():
	while True:
		do_something()
		time.sleep(5)

if __name__ == "__main__":
	run_server()
