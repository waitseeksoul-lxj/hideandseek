#!/usr/bin/env python

from math import sin, cos, asin, atan2, acos, sqrt, fmod, pi

erad = 6356780.0  #Earth radius In meters
r2d = 180.0/pi
d2r = pi/180.0
meter2mile = 0.00062137119223733392
#distance between 2grid points  points in meters

def heading(lat1,lon1,lat2,lon2):
    lat1 *= d2r
    lon1 *= d2r
    lat2 *= d2r
    lon2 *= d2r
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    t1 = sin(dlat/2.0);
    t2 = sin(dlon/2.0);
    a = t1*t1+cos(lat1)*cos(lat2)*t2*t2
    d = 2*asin(min(1,sqrt(a)))*erad
    y = sin(dlon)*cos(lat2)
    x = cos(lat1)*sin(lat2) - sin(lat1)*cos(lat2)*cos(dlon)  
    b = fmod(2*pi + atan2(y,x),2*pi)*r2d
    return {"dir":b,"dist":d}

def meters2miles(meters):
    return meters*meter2mile


def sph2car(lat,lon):
    th = pi/2 - lat*d2r 
    phi = lon*d2r
    x = erad * sin(th) * sin(phi)
    y = erad * cos(th)
    z = erad * sin(th) * cos(phi)
    return (x,y,z)

def car2sph(x,y,z):
    r = sqrt(x*x+y*y+z*z)
    th = acos(y/r)
    phi = atan2(x,z)
    lat = (pi/2 - th)*r2d
    lon = phi*r2d
    return(lat,lon)
 
def vlen(*vl):
    sum = 0.0
    for v in vl:
        sum += v*v
    return sqrt(sum)

def vsmul(s,*vl):
    out = []
    for v in vl:
        out.append(s*v)
    return tuple(out)

def avg(*vl):
    sum = 0.0
    n = 0
    for v in vl:
        sum += v
        n += 1
    if n == 0:
        return None
    return sum/float(n)

def norm(*vl):
    out = []
    d = 1/vlen(*vl)
    return vsmul(d,*vl)

def addvect(v1,v2):
    out = []
    if len(v1) != len(v2):
        return None
    for i in xrange(0,len(v1)):
        out.append(v1[i]+v2[i])
    return tuple(out)

def avgsph(points):
    sum_vect = (0.0,0.0,0.0)
    n = 0
    for p in points:
        cv = sph2car(*p)
        u = norm(*cv)
        sum_vect = addvect(sum_vect,u)
        n += 1
    avg_vect = norm(*sum_vect)
    sph = vsmul(erad,*avg_vect)
    return car2sph(*sph)
