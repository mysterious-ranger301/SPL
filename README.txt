Hey there! If you have downloaded this module, you might be wondering
why I made this and what it does. I'll tell you now:
So first of all, unpack the .zip file and you'll see the .py file and
this README.txt file. You can use this module in any of your Python
programs (I assume your version if Py3 and you have Windows, but I think it should work
with Py2). What this module does, is it lets your program open
files with their appropriate apps. For example, you say spl.Open('Test.txt'),
Python will open that file in, say, notepad. For macOSX users, I have a version for macOS, 
(github.com/mysterious-ranger301/SPL_for_mac) but
most of the features rely on Windows, and only Windows, so the command line features will be disabled. Replace
them with the appropriate function definitions (I couldn't do it because I don't have a mac).
And as for Linux, I also have a version for you too, but again, command line features will be disabled by default.
(github.com/mysterious-ranger301/SPL_for_linux)
Another feature is you can use the command line with this module.
Say you type:
spl.cmd('pip3 install numpy')
Python would just install numpy!
Now to how you actually use it:
import SPL # import the module
mySplObj = SPL.splObj() # sets mySplObj with the class SPL
Features:
mySplObj._dir() # displays files/folder in the current directory
mySplObj._cls() # clears screen (you might want this if your output is too messy)
._cd(folder) # changes Python working directory to "folder" (also enter mySplObj._cd(folder),
I'm just not putting the mySplObj there)
.cmd(command) # lets you use the command line! (again, enter commands appropriate for your system)
._cmdOpenFile(file) # more reliable than .Open(file), uses command line to do it.
.checkpath(path) # same as os.path.exists(path), needed for other functions
.openWithApp(file_path, path_of_app) # lets you open a file with app (you have to enter
the path of the app to do it)
.Open(file, app='start') # opens file with default app (but you can change it by
saying .Open('Test.txt', 'C:\\Windows\\System32\\notepad.exe'))
.openApp(app_path) # opens app (enter app path to do it)
And that's all! There's even an error class - SplError! You can raise it if you want:
raise SPL.SplError('An exception Occured')
I will also constantly release newer versions of this module and put old ones in the "old" branch.
Sorry for the very long explanation,
Mysterious Ranger
Enjoy!
