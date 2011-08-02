#!/usr/bin/env python

import urllib2
import json

#run python manage.py runserver 127.0.0.1:8080 from ../..
url = "http://127.0.0.1:8080/test/avgpoints"

north_pole = """
{
  "points": [
    {"y":  0,  "x": 80}, 
    {"y":  90, "x": 80}, 
    {"y": -90, "x": 80}, 
    {"y": 180, "x": 80}
  ]
}
"""

deg_160 = """
{
  "points": [
    {"y": 160, "x": -45 }, 
    {"y": 160, "x":  45 }
  ]
}"""


req = urllib2.Request(url,north_pole)
resp = urllib2.urlopen(req)
avgPoint = json.loads(resp.read())
assert avgPoint["y"] == 90.00,"Bad Average: result should have been north pole"


req = urllib2.Request(url,deg_160)
resp = urllib2.urlopen(req)
avgPoint = json.loads(resp.read())
(x,y) = (avgPoint["x"],avgPoint["y"])

assert (x,y) == (0.0,160.0), "Bad Average should have been (0.0,160.0)"
