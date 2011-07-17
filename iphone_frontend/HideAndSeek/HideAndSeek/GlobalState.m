//
//  GlobalState.m
//  hideandseek
//
//  Created by Carlos Garza on 7/16/11.
//  Copyright 2011 Carlos D. Garza. All rights reserved.
//

#import <CoreLocation/CoreLocation.h>
#import "GlobalState.h"
#import "StateContainer.h"

@implementation GlobalState

static StateContainer *sc;

+(void)init{
    sc = [[StateContainer alloc] init];
}

+(void)dealloc{
    [sc release];
    [super dealloc];
}

+(StateContainer *)sc{
    return sc;
}

@end
