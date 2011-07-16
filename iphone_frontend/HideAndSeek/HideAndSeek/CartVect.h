//
//  CartVect.h
//  HideAndSeek
//
//  Created by Carlos Garza on 7/16/11.
//  Copyright 2011 Carlos D. Garza. All rights reserved.
//

#import <Foundation/Foundation.h>


@interface CartVect : NSObject {
    double x;
    double y;
    double z;
}

@property (nonatomic,assign) double x;
@property (nonatomic,assign) double y;
@property (nonatomic,assign) double z;


-(void) setX:(double)xIn setY:(double)yIn setZ:(double) zIn;
@end
