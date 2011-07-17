//
//  LocationController.h
//  HideAndSeek
//
//  Created by Carlos Garza on 7/16/11.
//  Copyright 2011 Carlos D. Garza. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <Corelocation/CoreLocation.h>

@interface LocationController : NSObject<CLLocationManagerDelegate> {
    CLLocationManager *locationManager;
}

@property(nonatomic,retain) CLLocationManager *locationManager;

-(void)locationManager:(CLLocationManager *)manager
  didUpdateTiKicatuibL:(CLLocation *)nLoc
    fromLocation:(CLLocation *)oLoc;

-(void)locationManager:(CLLocationManager *)manager
      didFailWithError:(NSError *)error;

@end
