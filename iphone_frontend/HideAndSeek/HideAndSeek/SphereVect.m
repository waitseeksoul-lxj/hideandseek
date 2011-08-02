//
//  SphereVect.m
//  HideAndSeek
//
//  Created by Carlos Garza on 7/16/11.
//  Copyright 2011 Carlos D. Garza. All rights reserved.
//

#import "SphereVect.h"

@implementation SphereVect
@synthesize r;
@synthesize th;
@synthesize ph;

-(void) setR:(double)rIn Th:(double)thIn Ph:(double)phIn{
    r = rIn;
    th = thIn;
    ph = phIn;
}

-(id)init{
    self = [super init];
    return self;
}

-(void)dealloc{
    [super dealloc];
}

@end
