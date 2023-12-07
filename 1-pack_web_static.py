#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""
from fabric.api import local
import time

def do_pack():
	"""generates a .tgz archive from content of the web static file"""
	try:
	    local("mkdir -p versions")
	    local("tar -cvzf versions/web_static_{}.tgz web_static/".
		  format(time.strftime("%Y%m%d%H%M%S")))
	    return ("versions/web_static_{}.tgz".format(time.
							strftime("%Y%m%d%H%M%S")))
	except:
	    return None
