//
//  DebugViewController.m
//  HideAndSeek
//
//  Created by Carlos Garza on 7/16/11.
//  Copyright 2011 Carlos D. Garza. All rights reserved.
//  
#import "DebugViewController.h"
#import "GlobalState.h"

@implementation DebugViewController
@synthesize accLabel;
@synthesize locateButton;
@synthesize gpsSwitch;
@synthesize xLabel;
@synthesize yLabel;
@synthesize zLabel;
@synthesize eightBallText;
@synthesize eightBallButton;

-(NSString *)double2strVar:(NSString *) var Val: (double) x{
    return [NSString stringWithFormat:@"%@%f",var,x];
}

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
    }
    return self;
}

- (void)dealloc
{
    [locateButton release];
    [gpsSwitch release];
    [accLabel release];
    [xLabel release];
    [yLabel release];
    [zLabel release];
    [eightBallButton release];
    [eightBallText release];
    [super dealloc];
}

- (void)didReceiveMemoryWarning
{
    // Releases the view if it doesn't have a superview.
    [super didReceiveMemoryWarning];
    
    // Release any cached data, images, etc that aren't in use.
}

#pragma mark - View lifecycle

- (void)viewDidLoad
{
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
    eightBallText.editable = NO;
}

- (void)viewDidUnload
{
    [super viewDidUnload];
    // Release any retained subviews of the main view.
    // e.g. self.myOutlet = nil;
}

- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation
{
    // Return YES for supported orientations
    return (interfaceOrientation == UIInterfaceOrientationPortrait);
}

-(IBAction) locateButtonDown:(id) sender{
    if(gpsSwitch.on){
        GlobalState.myAcc = GlobalState.myAcc + 1;
    }
    accLabel.text = [self double2strVar: @"acc=" Val: GlobalState.myAcc];
}

-(IBAction) gpsToggled:(id) sender{
    if(gpsSwitch.on){
        GlobalState.myAcc = 0.0;
        accLabel.text = [self double2strVar: @"acc=" Val: GlobalState.myAcc];
    }else{
        
    }
}

-(IBAction) eightBallDown:(id) sender{
    NSString *msg = [GlobalState randomEightBallMessage];
    eightBallText.text = msg;
}

@end
