#!/usr/bin/env python

import datetime
import time
import sys
import os
import random

rnd = random.Random()
dir_name = os.path.dirname(os.path.abspath("__file__"))
parent_dir = os.path.abspath(os.path.join(dir_name,"../.."))
sys.path.insert(0,parent_dir)

alpha = "abcdefghijklmnopqrstuvwxyz"
from django.core.management import setup_environ
from hideandseek import settings
setup_environ(settings)

from django.contrib.auth.models import User
from hideandseek.has.models import *
from hideandseek.has.modelUtil import *
from hideandseek.aes import aes_b64encrypt,aes_b64decrypt
import hideandseek.genUtil

def getFuncs(module,names):
    out = []
    for name in names.split(","):
        func = getattr(module,name)
        out.append(func)
    return tuple(out)


m = hideandseek.genUtil
reload(m)
func_names  = "heading,sph2car,car2sph,vlen,vsmul,norm,"
func_names += "avgsph"
cmd = "(%s) = getFuncs(hideandseek.genUtil,\"%s\")"%(func_names,func_names)
exec(cmd)

p = [(80,0),(80,90),(80,-90),(80,180)] #Should avg to north pole

p = [(-45,160),(45,160)] #should avg to (0,160)

avgsph(p)
