#!/usr/bin/python
import os
import subprocess
import argparse

if __name__ == "__main__":
    main()

# check if dtm has been run on this machine
def is_first_time_start_up():
    pass

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

