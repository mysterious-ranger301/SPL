# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 18:35:00 2020

@author: Mysterious Ranger
SPL - subprocess library simplified
"""
import subprocess as sp, os
# WARNING: TYPOS MAY AFFECT PROGRAM
class SPL:
    def __init__(self):
        self.__instructions__ = '''This is a library that simplifies
the module 'subprocess'. This is useful if your program needs to open
other apps like notepad, calc, etc. Created by Mysterious Ranger.'''
        self.SplError = SplError
        self.__author__ = 'Mysterious Ranger'
        self.__version__ = '1.3.1'
        self.err_file_path = 'File path not found.'
        self.err_app_path = 'App path not found.'
    def openWithApp(self, file, app):
        if not self.checkpath(file):
            raise self.SplError(self.err_file_path)
        if not self.checkpath(app):
            raise self.SplError(self.err_app_path)
        sp.Popen([app, file], shell=True)
#    def openWDA(self, file, app='start'):
#        if not os.path.exists(file):
#            raise SplError
#        sp.Popen([app, file], shell=True)
    def Open(self, file, app='start'):
        if not self.checkpath(file):
            raise self.SplError(self.err_file_path)
        sp.Popen([app, file], shell=True)
    def openApp(self, path):
        if not self.checkpath(path):
            raise self.SplError(self.err_app_path)
        sp.Popen(path)
    def cmd(self, command):
        sp.call(command, shell=True)
    def checkpath(self, path):
        if os.path.exists(path):
            return True
        else:
            return False
    
class SplError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
#        self.SplError = self
    def __str__(self):
        #print('calling str')
        if self.message:
            return str(self.message)
        else:
            return 'Something was typed incorrectly. Check the code and try\
 again.'

def splObj():
    return SPL()
def cmdObj():
    return cmd()
