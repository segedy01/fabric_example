from fabric.api import *
from fabric.contrib.files import exists

def production(host):
    env.hosts = host
    
def staging(host):
    env.hosts = host

def create_folder(folder_name):
    folder = '/Users/andela/Documents/{}'.format(folder_name)
    run('mkdir -p {}'.format(folder))

def deploy(user, folder_name, repository):
    folder_name = '/Users/{}/Documents/{}'.format(user, folder_name) 
    run('mkdir -p {}'.format(folder_name))
    with cd(folder_name):
        pull(repository)

def push():
    pass

def checkout(branch_name, use_folder):
    if use_folder:
        folder_name = '/Users/andela/Documents/session_two/chef-zero'
        with cd(folder_name):
            do_checkout(branch_name)

def pull(repository):
    if exists('.git'):
        run('git pull')
    else:
        clone(repository)

def clone(repository):
    run('git clone {}'.format(repository))

def do_checkout(branch_name):
    if exists('.git'):
        run('git checkout {}'.format(branch_name))
    else:
        print 'Please do a clone first'