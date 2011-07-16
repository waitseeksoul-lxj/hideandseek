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
    print "th=%f phi=%s"%(th,phi)
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
 
