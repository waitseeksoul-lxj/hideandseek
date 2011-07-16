//
//  DebugViewController.h
//  HideAndSeek
//
//  Created by Carlos Garza on 7/16/11.
//  Copyright 2011 Carlos D. Garza. All rights reserved.
//
#import <UIKit/UIKit.h>


@interface DebugViewController : UIViewController {
    IBOutlet UIButton *locateButton;
    IBOutlet UISwitch *gpsSwitch;
    IBOutlet UILabel  *accLabel;
    IBOutlet UILabel  *xLabel;
    IBOutlet UILabel  *yLabel;
    IBOutlet UILabel  *zLabel;
    IBOutlet UITextView *eightBallText;
    IBOutlet UIButton *eightBallButton;
}

@property (nonatomic,retain) IBOutlet UIButton *locateButton;
@property (nonatomic,retain) IBOutlet UISwitch *gpsSwitch;
@property (nonatomic,retain) IBOutlet UILabel *accLabel;
@property (nonatomic,retain) IBOutlet UILabel *xLabel;
@property (nonatomic,retain) IBOutlet UILabel *yLabel;
@property (nonatomic,retain) IBOutlet UILabel *zLabel;
@property (nonatomic,retain) IBOutlet UIButton *eightBallButton;
@property (nonatomic,retain) IBOutlet UITextView *eightBallText;

-(IBAction) locateButtonDown:(id) sender;
-(IBAction) gpsToggled:(id) sender;
-(IBAction) eightBallDown:(id) sender;
@end

