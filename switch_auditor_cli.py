#!/usr/bin/env python

"""CLI for auditing system to verify the integrity of the HIL database

Usage:
  switch_auditor_cli.py -h | --help | --version
  switch_auditor_cli.py show-info-node [PORT] [options]
  switch_auditor_cli.py show-info-vlan [VLAN] [options]
  switch_auditor_cli.py list-nodes-all [options]
  switch_auditor_cli.py list-nodes-for-project [PROJECT] [options]
  switch_auditor_cli.py switch-check-port [PORT] [options]
  switch_auditor_cli.py switch-check-vlan [VLAN] [options]

Audit Commands:
  show-info-node PORT		     Get information from HIL and Switch for PORT
  show-info-vlan VLAN		     Get information from HIL and Switch for VLAN
HIL Specific Commands:
  list-nodes-all		     list all nodes
Switch Specific Commands:
  switch-check-port PORT	     check for connected VLANs for a given port
  switch-check-vlan VLAN	     check for connected ports for a given VLAN

Options:
  -h, --help                         show this
  --quiet                            print less text
  -v, --verbose                      print more text
  --version                          show version

Arguments:
  PORT                               currently selected PORT
  VLAN                               currently selected VLAN

"""
import json
import logging
import requests

try:
    from docopt import docopt
except ImportError:
    exit("Docopt needs to be installed in order to display CLI arguments.\n" +\
         "Please run 'pip install docopt==0.6.2' or install from " +\
         "'https://github.com/docopt/docopt/'.")

LOGGER = logging.getLogger(__name__)

# URL to API
URL = "http://localhost:8000/"

def show_info_port():
    port = ARGUMENTS["PORT"]
    r_q = requests.get(URL + "show_info_port?port=" + port)
    print(r_q.text)

def show_info_vlan():
    vlan = ARGUMENTS["VLAN"]
    r_q = requests.get(URL + "show_info_vlan?vlan=" + vlan)
    print(r_q.text)

def list_nodes_all():
    r_q = requests.get(URL + "list_nodes_all")
    print(r_q.text)

def switch_check_port():
    port = ARGUMENTS["PORT"]
    r_q = requests.get(URL + "switch_check_port?port=" + port)
    print(r_q.text)

def switch_check_vlan():
    vlan = ARGUMENTS["VLAN"]
    r_q = requests.get(URL + "switch_check_vlan?vlan=" + vlan)
    print(r_q.text)
  	
def version():
    """
    :returns: version number of this CLI
    """
    # LOGGER.debug("version is called")

if __name__ == '__main__':
    LEVEL = logging.ERROR
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(module)s - %(message)s',
        level=LEVEL)

    ARGUMENTS = docopt(__doc__)
    # for debugging purposes
    LOGGER.debug(ARGUMENTS)

    if ARGUMENTS["show-info-node"]:
        show_info_port()
    elif ARGUMENTS["show-info-vlan"]:
        show_info_vlan()
    elif ARGUMENTS["list-nodes-all"]:
        list_nodes_all()
    elif ARGUMENTS["switch-check-port"]:
        switch_check_port()
    elif ARGUMENTS["switch-check-vlan"]:
        switch_check_vlan()
