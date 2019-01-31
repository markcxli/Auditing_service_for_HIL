from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from client import AuditClient

#import pdb; pdb.set_trace()

@api_view(['GET'])
def show_info_port(request):
	if 'port' in request.query_params:
		port = request.query_params["port"]
		node_info = AuditClient().get_node_info(port)
		returnstr = "HIL DB: \n"
		returnstr += "Project: " + node_info["project"]
		returnstr += '\n'
		returnstr += "Network: " + str(node_info["network"])
		returnstr += '\n'
		returnstr += "VLAN: " + str(node_info["vlan"])
		returnstr += '\n'
		returnstr += "-----------------------------"
		returnstr += '\n'
		returnstr += "Switch: \n"
		returnstr += str(AuditClient().list_switch_vlans(port))
		return HttpResponse(returnstr + '\n')
	else:
		return HttpResponse('Need port parameter\n')

@api_view(['GET'])
def show_info_vlan(request):
	if 'vlan' in request.query_params:
		vlan = request.query_params["vlan"]
		returnstr = "HIL DB: \n"
		nodes = AuditClient().list_nodes("all")
		#import pdb; pdb.set_trace()
		list_vlan_nodes = []
		for n in nodes:
			node_info = AuditClient().get_node_info(n)
			for x in node_info["vlan"]:
				for v in x:
					if (vlan in v):
						list_vlan_nodes.append(n)
		returnstr += str(list_vlan_nodes)
		returnstr += '\n'
		returnstr += "-----------------------------"
		returnstr += '\n'
		returnstr += "Switch: \n"
		returnstr += str(AuditClient().list_switch_ports(vlan))
		return HttpResponse(returnstr + '\n')
	else:
		return HttpResponse('Need vlan parameter\n')

@api_view(['GET'])
def list_nodes_all(request):
		returnstr = "HIL DB: \n"
		returnstr += str(AuditClient().list_nodes("all"))
		returnstr += '\n'
		return HttpResponse(returnstr + '\n')

@api_view(['GET'])
def switch_check_port(request):
	if 'port' in request.query_params:
		port = request.query_params["port"]
		returnstr = "Switch: \n"
		returnstr += str(AuditClient().list_switch_vlans(port))
		return HttpResponse(returnstr + '\n')
	else:
		return HttpResponse('Need port parameter\n')

@api_view(['GET'])
def switch_check_vlan(request):
	if 'vlan' in request.query_params:
		vlan = request.query_params["vlan"]
		returnstr = "Switch: \n"
		returnstr += str(AuditClient().list_switch_ports(vlan))
		return HttpResponse(returnstr + '\n')
	else:
		return HttpResponse('Need vlan parameter\n')

@api_view(['GET'])
def audit_version(request):
	return HttpResponse("BETA 04_02_18\n")
