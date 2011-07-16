//
//  HideAndSeekAppDelegate.h
//  HideAndSeek
//
//  Created by Carlos Garza on 7/16/11.
//  Copyright 2011 Carlos D. Garza. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface HideAndSeekAppDelegate : NSObject <UIApplicationDelegate, UITabBarControllerDelegate> {

}

@property (nonatomic, retain) IBOutlet UIWindow *window;

@property (nonatomic, retain) IBOutlet UITabBarController *tabBarController;

@end
