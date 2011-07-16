//
//  main.m
//  HideAndSeek
//
//  Created by Carlos Garza on 7/16/11.
//  Copyright 2011 Carlos D. Garza. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "GlobalState.h"

int main(int argc, char *argv[])
{
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    [GlobalState init];
    int retVal = UIApplicationMain(argc, argv, nil, nil);
    [pool release];
    return retVal;
}
