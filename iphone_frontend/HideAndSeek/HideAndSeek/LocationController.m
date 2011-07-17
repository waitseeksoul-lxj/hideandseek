//
//  LocationController.m
//  HideAndSeek
//
//  Created by Carlos Garza on 7/16/11.
//  Copyright 2011 Carlos D. Garza. All rights reserved.
//

#import "LocationController.h"
#import "GlobalState.h"

@implementation LocationController
@synthesize locationManager;


- (id)init
{
    self = [super init];
    if (self) {
        self.locationManager = [[CLLocationManager alloc] init];
        self.locationManager.delegate = self;
    }
    
    return self;
}

-(void)locationManager:(CLLocationManager *)manager
   didUpdateToLocation:(CLLocation *)nLoc
    fromLocation:(CLLocation *)oLoc{
    
}

-(void)locationManager:(CLLocationManager *)manager
      didFailWithError:(NSError *)error{
    
}
- (void)dealloc
{
    [locationManager release];
    [super dealloc];
}

@end
