//
//  LocationController.m
//  HideAndSeek
//
//  Created by Carlos Garza on 7/16/11.
//  Copyright 2011 Carlos D. Garza. All rights reserved.
//

#import "LocationController.h"
#import "GlobalState.h"
#import "SphereVect.h"

@implementation LocationController
@synthesize locationMgr;


- (id)init
{
    self = [super init];
    if (self) {
        self.locationMgr = [[[CLLocationManager alloc] init]autorelease];
        self.locationMgr.delegate = self;
        //self.locationMgr.desiredAccuracy =kCLLocationAccuracyHundredMeters;
    }    
    return self;
}

-(void)locationManager:(CLLocationManager *)manager
   didUpdateToLocation:(CLLocation *)nLoc
    fromLocation:(CLLocation *)oLoc{
    double th = nLoc.coordinate.latitude;
    double ph = nLoc.coordinate.longitude;
    SphereVect *sv = [[SphereVect alloc]init];
    SphereVect *loc = GlobalState.sc.loc;
    NSMutableArray *svArry = GlobalState.sc.sphVects;
    [loc setR:0.0 Th:th Ph:ph];
    [sv setR:0.0 Th:th Ph:ph];
    [svArry addObject:sv];
    [sv release];
    GlobalState.sc.locCount += 1;
}

-(void)locationManager:(CLLocationManager *)manager
      didFailWithError:(NSError *)error{
    
}
- (void)dealloc
{
    [locationMgr release];
    [super dealloc];
}

@end
