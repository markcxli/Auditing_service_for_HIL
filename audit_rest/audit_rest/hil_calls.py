#!/usr/bin/env python

import sys
import os
import schema
import pkg_resources

from hil.client.client import Client, RequestsHTTPClient
from hil.client.base import FailedAPICallException
from hil.errors import BadArgumentError
from hil.commands.util import ensure_not_root


MIN_PORT_NUMBER = 1
MAX_PORT_NUMBER = 2**16 - 1
#VERSION = pkg_resources.require('hil_audit')[0].version


class HILClientFailure(Exception):
    """Exception indicating that the HIL client failed"""


# HELPER METHODS

def hil_client_connect(endpoint_ip, name, pw):
    """Returns a HIL client object"""

    hil_http_client = RequestsHTTPClient()
    hil_http_client.auth = (name, pw)

    return Client(endpoint_ip, hil_http_client)


class HILCLI(object):

    def __init__(self):
        # some stuff to setup hil_client
        endpoint = os.getenv('HIL_ENDPOINT')
        username = os.getenv('HIL_USERNAME')
        password = os.getenv('HIL_PASSWORD')
        self.hil_client = hil_client_connect(endpoint, username, password)

    def list_nodes(self, nodes):
        if nodes == 'free':
            response = self.hil_client.node.list("free")
        else:
            response = self.hil_client.node.list("all")

        return response

    def list_projects(self):
        response = self.hil_client.project.list()
        return response

    def list_project_network(self, proj):
        response = self.hil_client.project.networks_in(proj)
        return response

    def show_network(self, net):
        response = self.hil_client.network.show(net)
        return response

    def show_node(self, node_name):
        response = self.hil_client.node.show(node_name)
        return response
