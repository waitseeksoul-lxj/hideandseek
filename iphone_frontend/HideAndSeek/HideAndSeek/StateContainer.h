//
//  StateContainer.h
//  HideAndSeek
//
//  Created by Carlos Garza on 7/16/11.
//  Copyright 2011 Carlos D. Garza. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <CoreLocation/CoreLocation.h>
#import "SphereVect.h"
#import "locationController.h"

@interface StateContainer : NSObject {
    SphereVect *loc;
    double locAcc;
    int locCount;
    NSArray *eightBall;
    LocationController *locController;
}

@property (nonatomic,retain) SphereVect *loc;
@property (nonatomic) double locAcc;
@property (nonatomic) int locCount;
@property (nonatomic,retain) LocationController *locController;

-(id)init;
-(void)dealloc;
-(NSString *)randomEightBallMessage;

@end
