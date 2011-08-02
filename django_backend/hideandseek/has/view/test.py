import simplejson
from django.core import serializers
from django.http import HttpResponse
from hideandseek.fileUtil import load_cpickle, save_cpickle
from hideandseek.responses import *
from genUtil import *
import json

def jsonout(self):
    out = {}
    points = []
    v = 1.0
    for p in xrange(0,5):
        points.append({"x":v,"y":v + 1.0})
        v += 2.0
    out["points"] = points
    resp = JsonResponse(entity=out)
    return resp

def jsonin(self):
    obj = self.loadJson()
    if not obj.has_key("points"):
        return BadRequest(errormsg="You need to provide points")
    return JsonResponse(entity=obj)
    
        
def avgpoints(self):
    obj = self.loadJson()
    sphPoints = []
    if not obj.has_key("points"):
        return BadRequest(errormsg="You need to provide points")
    for point in obj["points"]:
        if not point.has_key("x"):
            return BadRequest(errormsg="point element missing x attribute")
        if not point.has_key("y"):
            return BadRequest(errormsg="point element missing y value")
        sphPoints.append( (point["x"],point["y"]) )
    sphVect = avgsph(sphPoints)
    avgPoint = {"x":sphVect[0],"y":sphVect[1]}
    return JsonResponse(entity=avgPoint)
        
