# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 18:35:00 2020

@author: Mysterious Ranger
SPL - subprocess library simplified
"""
import subprocess as sp, os

class cmd:
    def __init__(self):
#        spl = splObj()
#        self.__author__ = spl.__author__
        self.__instructions__ = '''Unlike SPL, the cmd() class uses the command line to do things. SPL's Open() function (which was removed) isn't reliable for opening files with extensions like .mp4, .mp3, or .wav. Use the _cmdUseSlash(file, extra='.', path='.') or _cmdUseStart(file, path='.') instead. . You don't need to specify 'path', its default value is '.'. The cmd() and SPL() libraries are linked together, so you can use all the functions from both cmd() and SPL().'''
        self.__author__ = 'Mysterious Ranger'
        self.__version__ = '1.4.3'
        self.SplError = SplError
        self.err_file_path = 'File path not found.'
        self.err_app_path = 'App path not found.'
        self.mac_err = 'Command line features not available for mac.'
    def _dir(self):
        self.cmd('dir')
    def _cls(self):
        self.cmd('cls')
    def _cd(self, folder):
#        import os
        os.chdir(folder)
	# Why this is like this, is because self.cmd('cd folder') doesn't work
    def cmd(self, comm):
        sp.call(comm, shell=True)
    def _cmdUseStart(self, file, path='.'):
        self._cd(path)
        if not self.checkpath(file):
            raise self.SplError(self.err_file_path)
        self.cmd('start {0}'.format(file))
    def _cmdUseSlash(self, file, extra = '.',path='.'):
        self._cd(path)
        if not self.checkpath(file):
            raise self.SplError(self.err_file_path)
        self.cmd('{0}/{1}'.format(extra, file))
    def _pwm(self):
        return os.getcwd()
    def checkpath(self, path):
        if os.path.exists(path):
            return True
        else:
            return False

class SPL(cmd):
    def __init__(self):
        super().__init__()
#        self.__instructions__ = '''This is a library that simplifies
#the module 'subprocess'. This is useful if your program needs to open
#other apps like notepad, calc, etc. Created by Mysterious Ranger.'''
#        self.SplError = SplError
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
#    def cmd(self, command):
#        sp.call(command, shell=True)
    
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
