'''
download file
'''

import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "lxml"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "HTMLParser"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])

