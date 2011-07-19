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
        self.locationMgr = [[CLLocationManager alloc] init];
        self.locationMgr.delegate = self;
    }
    
    return self;
}

-(void)locationManager:(CLLocationManager *)manager
   didUpdateToLocation:(CLLocation *)nLoc
    fromLocation:(CLLocation *)oLoc{
    double th = nLoc.coordinate.latitude;
    double ph = nLoc.coordinate.longitude;
    SphereVect *loc = GlobalState.sc.loc;
    GlobalState.sc.locCount += 1;
    [loc setR:0.0 Th:th Ph:ph];
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
