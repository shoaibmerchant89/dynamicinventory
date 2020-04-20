#!/usr/bin/python

import json
import argparse
import sys
import psycopg2

try:
    import json
except ImportError:
    import simplejson as json

class baseinventory(object):

    def __index__(self):
        self.inventory = {}
        self.read_cli_args()

        if self.read_cli_args:
            hosts.list = self.retrieve_hosts()
            self.inventory = {
                "group": {
                    "hosts": hosts_list
                }
            }