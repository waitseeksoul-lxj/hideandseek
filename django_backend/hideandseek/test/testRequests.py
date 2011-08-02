#!/usr/bin/env python

import datetime
import time
import sys
import os

dir_name = os.path.dirname(os.path.abspath("__file__"))
parent_dir = os.path.abspath(os.path.join(dir_name,"../.."))
sys.path.insert(0,parent_dir)

from django.core.management import setup_environ
from hideandseek import settings
setup_environ(settings)

from django.contrib.auth.models import User
from hideandseek.has.models import *
from hideandseek.has.modelUtil import *
from hideandseek.aes import aes_b64encrypt,aes_b64decrypt
from hideandseek.genUtil import *
from hideandseek.fileUtil import *

def load_request():
    load_cpickle("~/req.db")
