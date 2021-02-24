#!/usr/bin/python
import os
import subprocess
import argparse
from conf import *

if __name__ == "__main__":
    main()
def main():
    conf_path = conf.gen_conf.path()

# check if dtm has been run on this machine
def is_first_time_start_up():
    if (conf_path == "placeholder for non-existent"):
        return True
    else:
        return False 

# setup configuration files and generate default config file for first time use
def first_time_conf():
    pass

# pull the dotfiles from the git repo
def git_pull(repo):
    '''
    repo(String): the repo the dot files are going to be pulled down from
    '''
    command_string = f"git pull {repo}"
    subprocess.check_output(command_string, check=True, stdout=PIPE)   

