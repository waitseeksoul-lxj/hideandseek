import simplejson
from django.core import serializers
from django.http import HttpResponse

def testjson(self):
    out = {}
    points = []
    v = 1.0
    for p in xrange(0,5):
        points.append({"x":v,"y":v + 1.0})
        v += 2.0
    out["points"] = points
    content = simplejson.dumps(out)
    status = 200
    content_type = "application/json"
    resp = HttpResponse(content=content,status=status,content_type=content_type)
    return resp
