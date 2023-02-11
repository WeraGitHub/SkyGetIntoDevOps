
print("""

 A module is a file containing code, held in subdirectory __pycache__ from Python 3.2.
 A module might be a DLL(Windows) or shared object (Linux/UNIX .so files.)
 
 A package is a logical group of modules.
 A directory containing a set of modules is a package
 The difference is a file called __init__.py (not required after Python version 3.3
 and can contain a list of public interfaces as attribute __all__
 __all__ = ['getprocs', 'getprocsall', 'filter']
  
  
  
  
 """)


import sys  # should be at the top of the program, you can specify several modules separated by comas
# like: import sys, sys1, sys2
# or you can specify an alias for a module name
# like import mymodule_win32 as mymodule
sys.path.append('/demomodules')
print('sys.path:', sys.path)


print('\n\n\n\nImporting names\n')
# from mymodule import *             importing all the names
# from mymodule import my_func       importing specific object name(s)
# or use an alias to avoid any name collisions
# from mymodule import (my_fun1 as mf1, my_fun2 as mf2)


print('\n\n\n\nThe "main" trick\n')
def main():
    """
    Stand alone program code, usually function
    calls or tests
    """
if __name__ == "__main__":
    main()
    