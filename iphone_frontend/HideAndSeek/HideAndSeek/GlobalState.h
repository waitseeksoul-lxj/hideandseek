//
//  GlobalState.h
//  hideandseek
//
//  Created by Carlos Garza on 7/16/11.
//  Copyright 2011 Carlos D. Garza. All rights reserved.
//
#import <Foundation/Foundation.h>
#import <CoreLocation/CoreLocation.h>

@interface GlobalState : NSObject {
    
}
+(void)setMyAcc:(double) acc;
+(double)myAcc;
+(void)init;
+(NSString *)randomEightBallMessage;
+(void)dealloc;
@end

