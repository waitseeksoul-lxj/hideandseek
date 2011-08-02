//
//  StateContainer.m
//  HideAndSeek
//
//  Created by Carlos Garza on 7/16/11.
//  Copyright 2011 Carlos D. Garza. All rights reserved.
//

#import "StateContainer.h"
#import "SphereVect.h"
#import "locationController.h"

@implementation StateContainer
@synthesize loc;
@synthesize locAcc;
@synthesize locCount;
@synthesize locController;
@synthesize sphVects;

- (id)init{
    self = [super init];
    if (self) {
        locAcc = 0.0;
        locCount = 0;
        loc = [[[SphereVect alloc] init]autorelease];
        eightBall = [NSArray arrayWithObjects:
                     @"That which doesn't kill you. only postpones the inevitable.",
                     @"As long as your better then half your peers your still above average.",
                     @"Success is merely the inverse of 'Mean Time Between Failure'",
                     nil];
        locController = [[[ LocationController alloc] init]autorelease];
        [[locController locationMgr ] startUpdatingLocation];
        sphVects = [[[ NSMutableArray alloc] init]autorelease];
        
    }    
    return self;
}

- (void)dealloc{
    [loc release];
    [eightBall release];
    [locController release];
    [sphVects release];
    [super dealloc];
}

-(NSString *)randomEightBallMessage{
    NSString *out;
    int n = [eightBall count];
    int i = random()% n;
    out = [eightBall objectAtIndex: i];
    return out;
}
@end
