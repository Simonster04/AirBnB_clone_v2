#!/usr/bin/python3
"""
 Contains do_deploy function
"""
from fabric.api import *
from fabric.operations import *
from os.path import isfile
env.hosts = ["104.196.213.138", "3.80.40.75"]


def do_deploy(archive_path):
    """ Distributes an archive to your web servers """
    if not isfile(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        file = archive_path.split('/')[-1]
        folder = file.split('.')[0]
        path = "/data/web_static/releases/"
        run("sudo mkdir -p {}{}".format(path, folder))
        run("sudo tar -xzf /tmp/{} -C {}{}".format(file, path, folder))
        run("sudo rm /tmp/{}".format(file))
        run("sudo mv {0}{1}/web_static/* {0}{1}".format(path, folder))
        run("sudo rm -rf {}{}/web_static/".format(path, folder))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}{}/ /data/web_static/current".format(path, folder))
        return True
    except:
        return False
