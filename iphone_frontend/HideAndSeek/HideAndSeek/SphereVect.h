//
//  SphereVect.h
//  HideAndSeek
//
//  Created by Carlos Garza on 7/16/11.
//  Copyright 2011 Carlos D. Garza. All rights reserved.
//

#import <Foundation/Foundation.h>


@interface SphereVect : NSObject {
    double r;
    double th;
    double ph;
}

@property (nonatomic,assign) double r;
@property (nonatomic,assign) double th;
@property (nonatomic,assign) double ph;

-(id)init;

-(void)setR:(double)r Th:(double) th Ph:(double)ph;

-(void)dealloc;

@end
