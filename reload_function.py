'''
The reload function reloads an imported module in python. The only precondition is that the argument passed
to it must be a module that has already been successfully imported within the program.
Import the importlib module where the reload function seats
'''

import importlib
import sample 

importlib.reload(sample)
importlib.reload(sample)
importlib.reload(sample)

import filechanges

def changes():
    try:
        importlib.reload(filechanges)
        filechanges.print_changes()
    except:
        pass

for i in range(5):
    changes()
    input("Hit enter to reload.....")

