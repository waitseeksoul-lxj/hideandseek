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
    IBOutlet UILabel  *rLabel;
    IBOutlet UILabel  *thLabel;
    IBOutlet UILabel  *phLabel;
    IBOutlet UILabel  *locCountLabel;
    IBOutlet UITextView *eightBallText;
    IBOutlet UIButton *eightBallButton;
}

@property (nonatomic,retain) IBOutlet UIButton *locateButton;
@property (nonatomic,retain) IBOutlet UISwitch *gpsSwitch;
@property (nonatomic,retain) IBOutlet UILabel *accLabel;
@property (nonatomic,retain) IBOutlet UILabel *rLabel;
@property (nonatomic,retain) IBOutlet UILabel *thLabel;
@property (nonatomic,retain) IBOutlet UILabel *phLabel;
@property (nonatomic,retain) IBOutlet UILabel *locCountLabel;
@property (nonatomic,retain) IBOutlet UIButton *eightBallButton;
@property (nonatomic,retain) IBOutlet UITextView *eightBallText;

-(IBAction) locateButtonDown:(id) sender;
-(IBAction) gpsToggled:(id) sender;
-(IBAction) eightBallDown:(id) sender;
@end

