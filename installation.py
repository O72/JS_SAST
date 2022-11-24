import subprocess
"""
This file will install all of the integrated tools and packages to ensure everything that is supported is installed in 
the system.
"""

def requirements():
    """
    This function is used to install the required python packages on the target system
    """
    subprocess.run(["pip3", "-r", "install", "requirements.txt"], shell=False)

def install_bandit():
    """
    This function is used to install bandit tool on the target system
    """
    subprocess.run(["pip3", "install", "bandit"], shell=False)

def install_gosec():
    """
    This function is used to install bandit tool on the target system
    """
    subprocess.run(["curl -sfL https://raw.githubusercontent.com/securego/gosec/master/install.sh | sh -s v2.14.0"], shell=False)
