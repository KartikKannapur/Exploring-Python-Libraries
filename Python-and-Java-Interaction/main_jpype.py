"""
Project Folder: Github Projects

Connection between Python and Java
"""
__author__ = 'KKN6KOR'

# #Python Module Imports
from jpype import *

# #PATH
java_system_path = "C:\\Program Files (x86)\\Java\\jre7\\bin\\client\\jvm.dll"

def main_jype_function():
    # #Start the JVM
    startJVM(getDefaultJVMPath())

    # #Java Code Here
    java.lang.System.out.println(1)


    shutdownJVM()
if __name__ == "__main__":
    main_jype_function()