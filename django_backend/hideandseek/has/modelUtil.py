from django.db.models import Q
from hideandseek.aes import aes_b64encrypt,aes_b64decrypt
from hideandseek.settings import KEY
import datetime
import copy

from hideandseek.has.models import *
from hideandseek.aes import aes_b64encrypt,aes_b64decrypt
import hideandseek.genUtil

def now():
    return datetime.datetime.now()

def playerHeading(p1,p2):
    for k in ["x","y"]:
        if getattr(p1,k) == None or getattr(p2,k) == None:
            return None
    return hideandseek.genUtil.distance(p2.y,p2.x,p1.y,p2.x)

def getPlayer(name):
    qs = Player.objects.filter(name=name)
    if len(qs)<1:
        return None
    return qs[0]

def setPasswd(entity,passwd):
    entity.passwd = aes_b64encrypt(passwd,KEY)
    return entity

def getPasswd(entity):
    return aes_b64decrypt(entity.passwd,KEY)
    
def newPlayer(name,passwd):
    qs = Player.objects.filter(name=name)
    if len(qs)>=1:
        return None
    player = Player()
    player.name = name
    player.passwd = aes_b64encrypt(passwd,KEY)
    player.lastSeen = now()
    return player

def getGamesPlayerIsIn(player):
    q=Q(players=player)
    qs = Game.objects.filter(q)
    return qs

def getVisablePlayers(player,game=None):
    q  = Q(visible=True)
    q &= Q(active=True)
    if(game != None):
        q &= Q(inGame=game)
    q &= ~Q(isHiddingFrom=player)
    return Player.objects.filter(q)

def mergeProps(modelIn,props):
    for (key,val) in props.items():
        setattr(modelIn,key,val)


def getMap(qs,key):
    out = {}
    for r in qs:
        k = getattr(r,key)
        out[k]=r
    return out

def moveEntity(player,*args,**kw):
    player.lastSeen = now()
    pLog = PositionLog()
    player.x = player.y = player.z = player.acc = None
    setPosition(pLog,*args,**kw)
    setPosition(player,*args,**kw)
    pLog.placedBy = player
    pLog.evdate = now()
    pLog.save()
    player.save()

def getGame(name):
    qs = Game.objects.filter(name=name)
    if len(qs) <1:
        return None
    return qs[0]

def newGame(name,passwd,ownedBy,*args,**kw):
    g = Game()
    g.name = name
    g.passwd = aes_b64encrypt(passwd,KEY)
    g.ownedBy = ownedBy
    setPosition(g,*args,**kw)
    return g

def setEvDate(entity):
    entity.evdate = datetime.datetime.now()

def setPosition(entity,*args,**kw):
    allowed_keys = set(["x","y","z","acc","radius"])
    keys = [k for k in kw.keys() if k in allowed_keys]
    print "keys=",kw.keys()
    for key in keys:
        setattr(entity,key,kw[key])
        print key,"=",kw[key]
    return entity

def getMap(entities,key):
    out = {}
    for entity in entities:
        k = getattr(entity,key)
        out[k] = entity
    return out
