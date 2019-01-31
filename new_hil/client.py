#!/usr/bin/env python

import sys
import os

from hil_calls import HILCLI

import SwitchCalls

class AuditClient(object):	

	def list_nodes(self, list_type):
		response = HILCLI().list_nodes(list_type)
		return response

	def list_projects(self):
		response = HILCLI().list_projects()
		return response

	def list_project_network(self, project):
		response = HILCLI().list_project_network(project)
		return response

	def show_network(self, network):
		response = HILCLI().show_network(network)
		return response

	def show_node(self,node_name):
		response = HILCLI().show_node(node_name)
		return response

	def get_node_info(self, node_name):
		response = {}
		node_info = HILCLI().show_node(node_name)
		if (node_info["project"] != None):
			response["project"] = node_info["project"]
			network = self.list_project_network(response["project"])
			response["network"] = network
			vlan = []
			for n in network:
				vlan.append(AuditClient().show_network(n)["channels"])
			response["vlan"] = vlan
		else:
			response["project"] = ""
			response["network"] = []
			response["vlan"] = [[]]
		return response
		
# -------- SWITCH FUNCTIONS ------------

	def list_switch_vlans(self, port):
		response = SwitchCalls.list_vlans(port)
		return response

	def list_switch_ports(self, vlan):
		response = SwitchCalls.list_ports(vlan)
		return response

