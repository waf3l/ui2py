#!/usr/bin/env python
'''
Created on 28-03-2013

@author: waf3l
'''


from distutils.core import setup



setup(name = "ui2py",
    version = "0.1.1",
    license = 'free to use',
    description = "Watch Ui files and convert them to py files",
    author = "Marcin Wojtysiak",
    author_email = "wojtysiak.marcin@gmail.com",
    url = "",
    packages = ['UiConvert','UiWatch'],
    scripts = ["ui2py.py"],
    long_description = """Watch Ui files and convert them to py files.""",
    requires = [
        'pyinotify'
    ]
) 
