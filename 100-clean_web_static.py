#!/usr/bin/python3
"""
 Contains do_clean() function
"""
from fabric.api import *
from fabric.operations import *
from os.path import isfile, isdir
import time

env.hosts = ["104.196.213.138", "3.80.40.75"]


def do_clean(number=0):
    """ Deletes out-of-date archives """
    if number == 0:
        number = 1
    with cd.local('./versions/'):
        len = int(sudo("ls | wc -l"))
        local("sudo ls -tr1 | head -n +{} | xargs -d '\n' rm -rf --".
              format(len - int(number)))
    with cd('/data/web_static/releases/'):
        len = int(sudo("ls | wc -l"))
        run("sudo ls -tr1 | head -n +{} | xargs -d '\n' rm -rf --".
            format(len - int(number)))
