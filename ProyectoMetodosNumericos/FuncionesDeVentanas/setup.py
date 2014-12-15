'''
Created on 11/12/2014

@author: Jimmy Ramos
'''

import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os","parser","math","docx","lxml","PySide.QtGui","matplotlib","sympy"]}

setup(name = "Proyecto Metodos Numericos",
    version = "3.1",
    description = "Proyecto Metodos Numericos",
    options = {"build_exe": build_exe_options },
    executables = [Executable("Login.py", base = "Win32GUI")])