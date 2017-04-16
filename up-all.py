#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
"""
@aut
"""

from subprocess import call
from multiprocessing import Pool
import threading
import argparse
import os

"""
cmd flag parsing
"""
flagParser = argparse.ArgumentParser(description="PHP project updater for development.")
flagParser.add_argument('-p', nargs=None, type=str, help='path is root directory', metavar='PATH')
args = flagParser.parse_args()
rootPath = args.p


gitCmd = "git checkout develop; git pull origin develop"
composerInstall = "composer install"


def projects():
    """
    Get psp directories names
    """
    import os
    dirs = os.listdir(rootPath)
    psp_dirs = []
    for d in dirs:
        if is_project_php(d):
            psp_dirs.append(d)
    return psp_dirs

def update_project(directory):
    """
    Update projects
    """
    import subprocess

    from subprocess import Popen

    path = '{}{}'.format(rootPath, directory)
    p = Popen('cd {}; {}'.format(path, gitCmd), shell=True)
    p.wait()
    print('cd {}; {}'.format(path, gitCmd))
    if p.returncode == 0:
        composer_p = Popen('cd {}; {}'.format(path, composerInstall), shell=True)
        composer_p.wait()
        print('cd {}; {}'.format(path, composerInstall))
        if composer_p.returncode == 0:
            print('{} project is ready !!!\n'.format(directory))
            return True
  #  raise Exception('{} project could not updated !'.format(directory))

def is_project_php(directory):
    """
    Adds commants
    """
    dir_project = '{}/{}'.format(rootPath, directory)
    git_dir = '{}{}/.git'.format(rootPath, directory)
    composer_json = '{}/{}/composer.json'.format(rootPath, directory)
    return os.path.exists(dir_project) and os.path.exists(git_dir) and os.path.exists(composer_json)


php_dirs = projects()
threads = []
for d in php_dirs:
    threads.append(threading.Thread(target=update_project, args=(d,), kwargs=None))

for t in threads:
    t.start()

for t in threads:
    t.join()