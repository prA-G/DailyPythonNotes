# Why the need of creating different scripts of student and teacher?
# To maintain the code
# For better understanding
# Best practice is to keep different components in different scripts.


# Each scripts we created as single file with .py extenxion is called MODULE.
# Inside module >> There can be functions, class, variables or some python code.

# Examples >> students_details.py >> teachers_detail.py >> Module


# PACKAGES : collection of modules organised in directory.
# Each directory can have multiple python scripts.
# Example << Student << teacher << Packages.

# versions before python3.3 to make a package it was necessary to include __init__.py to initialize the package and expose required module and functions
# But not required any more.


# LIBRARY : Collection of pre-written code to perform common tasks
# Collection of multiple packages and modules
# Examples : Library&Packages is library which include two packages student and teacher.


def student():
    print("This is student details.")
student()


# importing teachers_details module form Teacher package

from Teacher import teachers_details   # from is use with packages and import with module.
import os, sys  # provide functionality to interact with OS
# sys provides access to system specific parameters and functions such as python
from os.path import dirname, join, abspath


# print(__file__) # gives you path of current scripts.
# print("The path to script : ", dirname(__file__))  # gives you directory conatining current script
# print("The directory of the script : ", join(dirname(__file__),"..")) # two or more path name components, inserting '/' as needed
# print("The directory of the script : ", abspath(join(dirname(__file__),"..")))  # converts the relative path to absolute path

parent_dir_path = abspath(join(dirname(__file__), ".."))
sys.path.insert(0, parent_dir_path) # at index 0, add this directory to the beginning f module search path

def student():
    print("This is student details.")
teachers_details.teacher()