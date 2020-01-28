"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for a in sys.argv:
    print("Argument:", a)
print('Program Name', sys.argv[0])
print('Arguments', sys.argv[1:])
print('Count of Arguments', len(sys.argv))

# Print out the OS platform you're using:
# YOUR CODE HERE
import os
platform = sys.platform
print(sys.platform)



# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
pid = os.getpid()
print(pid)
6004


# Print the current working directory (cwd):
# YOUR CODE HERE
wd = os.getcwd()
print(wd)
# C:\Users\Jason Holloway\lambda\Intro-Python-I\src


# Print out your machine's login name
# YOUR CODE HERE
import getpass
print(getpass.getuser())

