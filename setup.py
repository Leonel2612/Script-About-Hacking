from distutils.core import setup
import py2exe
import os
from time import sleep 
from random import randrange
import sqlite3
from pathlib import Path
import re
import datetime 


setup(
    windows=['Hackerprint.py'],
    options={
        'py2exe':{
            'bundle_files':1,
            'compressed':True,
            'optimize':2,
            'dist_dir':'dist',
            'dll_excludes':['w9xpopen.exe']
        }
    },
    zipfile=None
)
   