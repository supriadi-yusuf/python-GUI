there are some alternatives to create GUI application in python. tkinter is one of them.
to create GUI, we need python3x-tkinter library.

we can search for the library that matched with python3 version with
command : sudo yum search python3 | grep tkinter

since python3 in my machine is version 3.6, I use python36-tkinter.x86_64.

to check if the module has been installed or not with command :
sudo yum info python36-tkinter.x86_64

if the library is not installed yet then install the library with command :
sudo yum install python36-tkinter.x86_64

source codes here are based on tutorial in https://tkdocs.com/tutorial/
