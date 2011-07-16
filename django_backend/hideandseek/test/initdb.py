#!/usr/bin/env python

import datetime
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
import hideandseek.genUtil

players = getMap(Player.objects.all(),"name")
games = getMap(Game.objects.all(),"name")

newPlayer("crc","ncc1701d").save()
newPlayer("vowelHater","vowelHater").save()
newPlayer("asshole","asshole").save()

crc = getPlayer("crc")
vh = getPlayer("vowelHater")
ah = getPlayer("asshole")

for n in "abcdefghijklmnopqrstuvwxyz":
   u = newPlayer(n*4,n*4)
   u.save()

players = getMap(Player.objects.all(),"name")

g = newGame("vowels","vowels",players["crc"])
setPosition(g,x=1,y=1,z=1,acc=1,radius=1)
g.save()
g.players.add(players["crc"])

g = newGame("orgy","orgy",players["crc"])
setPosition(g,x=1,y=1,z=1,acc=1,radius=1)
g.save()
g.players.add(players["crc"])

games = getMap(Game.objects.all(),"name")

for(pname,player) in players.items():
    games["orgy"].players.add(player)

for p in "aeiuo":
    games["vowels"].players.add(players[p*4])
    players[p*4].hiddenFrom.add(players["vowelHater"])

for p in "abcdefghijklmnopqrstuvwxyz":
    players[p*4].hiddenFrom.add(players["asshole"])
    
