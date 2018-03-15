from fabric.api import local, run, env
import private

env.hosts = [private.host]
env.user = private.user
env.password = private.password

def hello(name="world"):
    print("hello, {}!".format(name))
    local("ls")

def install_system_packages():
    run("apt-get -y update")
    run("apt-get -y upgrade")
    run("apt-get -y install python3")
    run("apt-get -y install python3-pip")
    run("pip3 install --upgrade pip")

def deploy():
    install_system_packages()
