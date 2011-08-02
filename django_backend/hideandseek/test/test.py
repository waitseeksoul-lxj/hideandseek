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
from hideandseek.genUtil import *
from hideandseek.fileUtil import *

def now():
    return datetime.datetime.now()

def rndPoint():
    out = {}
    out["x"] = rnd.uniform(-180.00,180.00)
    out["y"] = rnd.uniform(-90.00,90.00)
    h = heading(0.0,0.0,out["x"],out["y"])
    out["z"] = h["dir"]
    out["acc"] = h["dist"]
    return out

def mergeModel(modelIn,props):
    for (key,val) in props.items():
        setattr(modelIn,key,val)

def rndword(num):
    out = ""
    for x in xrange(0,num):
        out += "%s"%(rnd.choice(alpha))
    return out

def rndPlayer():
    return newPlayer(rndword(8),rndword(8))

def rndDate(start,end):
    tstart = time.mktime(start.timetuple())
    tend  = time.mktime(end.timetuple())
    evdate = rnd.uniform(tstart,tend)
    return datetime.datetime.fromtimestamp(evdate)

def newPositionLog(players):
    p = PositionLog()
    start = datetime.datetime(2010,1,1)
    end   = datetime.datetime(2011,7,12)
    mergeModel(p,rndPoint())
    mergeModel(p,{"evdate":rndDate(start,end)})
    mergeModel(p,{"placedBy":rnd.choice(players)})
    return p

games = getMap(Game.objects.all(),"name")

moveEntity(players["crc"],y=29.51722,x=-98.31389,z=0.0,acc=0.01)
moveEntity(players["vowelHater"],y=29.417,x=-98.5,z=0.0,acc=0.01)
moveEntity(players["asshole"],y=29.5667,x=-98.26444,z=0.0,acc=0.01)

for i in xrange(0,1024):
    p = rndPlayer()
    p.save()
    print i

playerList = Player.objects.all()
players = getMap(playerList,"name")


p = []
for i in xrange(0,512*1024):
    if i%1024 == 0:
        print i>>10
    pl = newPositionLog(playerList)
    pl.save()

