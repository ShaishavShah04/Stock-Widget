'''
download file
'''

# This file will download all requirements into the user's python.

import subprocess, os, platform, sys
import sys

# Pip
osEnv = platform.system()
if osEnv == 'Windows':
    os.system("python -m pip install -U pip")
else:
    os.system('sudo apt install python3-pip')
#
subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "lxml"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "HTMLParser"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])

