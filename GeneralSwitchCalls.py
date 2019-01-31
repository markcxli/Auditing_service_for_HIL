from random import randint
from SwitchCalls import SwitchCalls

class GeneralSwitchClass(SwitchCalls):
	"""
	"""

	def get_port_networks(self, ports):
        ''' 
		return networks the ports are connected to 

		ports is a list of ports
		
		return should be key value pair dictionary
		key should be port
		value should be list of networks
		'''
		response = {}
		 for port in ports:
		 	r = randint(0,5)
		 	response[port] = randint(0, 9)
		 	for i in range(0,r-1):
		 		response{port}.append(randint(0, 9))

 		return response



	def get_network_ports(self, networks):
		''' 
		return ports connected to a network 
		
		networks is a list of networks

		return should be key value pair dictionary
		key should be network
		value should be list of ports
		'''
		response = {}
		 for net in networks:
		 	r = randint(0,5)
		 	response[net] = randint(0, 9)
		 	for i in range(0,r-1):
		 		response{net}.append(randint(0, 9))

 		return response