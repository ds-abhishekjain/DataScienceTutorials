# Module : It is the python files we will be defining which consists of various functions and classes
# this is calles as modules

# Package: the folder in which individual modules are kept are called as packages

import os , sys
from os.path import dirname ,join , abspath

sys.path.insert(0,abspath(join(dirname(__file__),'..')))

from course import course_details

def payment():
    print("This is my payment details")

course_details.course()

# this code will give an error as we have already used the packages in payment and now os is confused why
# we want to do vice versa as it makes no sense

