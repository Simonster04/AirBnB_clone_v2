#!/usr/bin/python3
"""
 Contains do_pack() fabric method

"""
from fabric.api import local
from os.path import isdir
import time


def do_pack():
    """generates a .tgz archive from the content of
     'web_static' folder
    """
    try:
        if isdir('versions') is False:
            local("mkdir versions")
        tgz_file = "versions/web_static_{}.tgz".format(time.strftime("%Y%m%d%H%M%S"))
        local("tar -cvzf {} web_static".format(tgz_file))
        return tgz_file
    except:
        return None
