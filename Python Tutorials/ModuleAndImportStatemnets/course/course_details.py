# Module : It is the python files we will be defining which consists of various functions and classes
# this is calles as modules

# Package: the folder in which individual modules are kept are called as packages

# we have to write these initial 3 lines of code to join the dir name with absolute path as the files seems untracked
# this is a common error that can occur

import os , sys
from os.path import dirname ,join , abspath

sys.path.insert(0,abspath(join(dirname(__file__),'..')))

from payments import payment_details

def course():
    print("This is my course details")

payment_details.payment()