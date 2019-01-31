#!/usr/bin/python

"""
Usage:
  switch_auditor_cli.py [list_vlans PORT]
  switch_auditor_cli.py [list_ports VLAN]

Examples:
  SwitchCalls.py list_ports 100
  SwitchCalls.py list_vlans veth-4

Arguments:
  PORT                               currently selected port
  VLAN                               currently selected VLAN
"""
import re
import logging
import ast
import subprocess
import shlex
import json

logger = logging.getLogger(__name__)

import json
import logging
try:
	from docopt import docopt
except ImportError:
	exit("Docopt needs to be installed in order to display CLI arguments.\n" +\
		 "Please run 'pip install docopt==0.6.2' or install from " +\
		 "'https://github.com/docopt/docopt/'.")

def list_vlans(port_sel):
	#shell_cmd = "sudo ovs-vsctl list port {port}".format(port=ARGUMENTS["PORT"])
	shell_cmd = "sudo ovs-vsctl show"
	args = shlex.split(shell_cmd)
	try:
		output = subprocess.check_output(args)
	except subprocess.CalledProcessError as e:
		logger.error(" %s ", e)
		raise SwitchError('Ovs command failed: ')
	port_found = 0
	output = output.split('\n')
	for x in range(0, len(output)):
		if port_found > 0:
			if output[x].find("tag") > 0:
				return (output[x].replace("tag", "VLAN").lstrip())
		if output[x].find("Port \"{port}\"".format(port=port_sel)) > 0:
			port_found = 1
		if port_found > 0 and output[x].find("Port") > 0 and output[x].find("Port \"{port}\"".format(port=port_sel)) < 0:
			port_found = 0


def list_ports(vlan_sel):
	list_nodes = []
	shell_cmd = "sudo ovs-vsctl show"
	args = shlex.split(shell_cmd)
	try:
		output = subprocess.check_output(args)
	except subprocess.CalledProcessError as e:
		logger.error(" %s ", e)
		raise SwitchError('Ovs command failed: ')
	vlan_found = 0
	output = output.split('\n')
	for x in range(0, len(output)):
		if vlan_found > 0:
			vlan_found = 0
			list_nodes.append(output[x-2].lstrip().replace("Port", "Port:").replace("\"", ""))
		if output[x].find("tag: {vlan}".format(vlan=vlan_sel)) > 0:
			vlan_found = 1
		if vlan_found > 0 and output[x].find("Port") > 0:# and output[x].find("Port \"{port}\"".format(port=ARGUMENTS["PORT"])) < 0:
			vlan_found = 0
	return list_nodes


if __name__ == '__main__':

	ARGUMENTS = docopt(__doc__)
	# for debugging purposes
	# LOGGER.debug(ARGUMENTS)
	#print ARGUMENTS

	ARGUMENTS["PROJECT"] = "default"
	if ARGUMENTS["list_vlans"]:
		list_vlans()
	elif ARGUMENTS["list_ports"]:
		list_ports()

