//
//  GlobalState.m
//  hideandseek
//
//  Created by Carlos Garza on 7/16/11.
//  Copyright 2011 Carlos D. Garza. All rights reserved.
//

#import <CoreLocation/CoreLocation.h>
#import "GlobalState.h"


@implementation GlobalState
static double myAcc;
static NSArray *eightBall;
static CLLocationManager *locationManager;

+(void)setMyAcc:(double)acc{
    myAcc = acc;
}
+(double)myAcc{
    return myAcc;
}
+(void)init{
    srandom(time(NULL));
    myAcc=0.0;
    eightBall = [NSArray arrayWithObjects:
          @"That which doesn't kill you. only postpones the inevitable.",
          @"As long as your better then half your peers your still above average.",
          @"Success is merely the inverse of 'Mean Time Between Failure'",
        nil];
    locationManager = [[CLLocationManager alloc] init];
}

+(NSString *)randomEightBallMessage{
    NSString *out;
    int n = [eightBall count];
    int i = random()% n;
    out = [eightBall objectAtIndex: i];
    return out;
}

+(void)dealloc{
    [eightBall release];
    [locationManager release];
    [super dealloc];
}

@end
