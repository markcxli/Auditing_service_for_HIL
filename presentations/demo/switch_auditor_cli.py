#!/usr/bin/env python
"""CLI for auditing system to verify the integrity of the HIL database

Usage:
  switch_auditor_cli.py -h | --help | --version
  switch_auditor_cli.py [check-state [PORT | VLAN] | check-diff [PORT | VLAN] | show-diff [PORT | VLAN]] [options]

Examples:
  switch_auditor_cli.py check-diff -v myproject -o outfile
  switch_auditor_cli.py show-diff --quiet myproject
  switch_auditor_cli.py check-state myproject

Commands:
  check-state PROJECT [PORT | VLAN]  query auditing service to get switch state
  check-diff PROJECT [PORT | VLAN]   check if there's a difference between the switch state versus HIL database
  show-diff PROJECT [PORT | VLAN]    show differences between the switches and auditing system
  check-vlan PROJECT PORT            check for connected VLANs for a given port
  check-port PROJECT VLAN            check for connected ports for a given VLAN

Options:
  -h, --help                         show this
  --quiet                            print less text
  -v, --verbose                      print more text
  --version                          show version
  -o FILE                            print the output to a file

Arguments:
  PROJECT                            currently selected project
  FILE                               output file
  PORT                               currently selected port
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
URL = "http://www.example.com"

def check_state():
    """
    :returns: switch state
    """
    r_q = requests.get("http://localhost:8000/check_state?node=" + ARGUMENTS["PORT"])
    print(r_q.text)

    # LOGGER.debug("check_state is called")

def check_diff():
    """
    :returns: Whether or not the switch state differs from HIL database
    """
    r_q = requests.get("http://localhost:8000/check_diff?node=" + ARGUMENTS["PORT"])
    print(r_q.text)

    # LOGGER.debug("check_diff is called")

def show_diff():
    """
    :returns: diff between switch state vs HIL database
    """
    r_q = requests.get("http://localhost:8000/show_diff?node=" + ARGUMENTS["PORT"])
    print(r_q.text)

    # LOGGER.debug("show_diff is called")

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
    # LOGGER.debug(ARGUMENTS)

    ARGUMENTS["PROJECT"] = "default"
    if ARGUMENTS["check-state"]:
        check_state()
    elif ARGUMENTS["check-diff"]:
        check_diff()
    elif ARGUMENTS["show-diff"]:
        show_diff()
