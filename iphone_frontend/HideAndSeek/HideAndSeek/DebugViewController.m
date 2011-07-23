//
//  DebugViewController.m
//  HideAndSeek
//
//  Created by Carlos Garza on 7/16/11.
//  Copyright 2011 Carlos D. Garza. All rights reserved.
//  

#import "DebugViewController.h"
#import "GlobalState.h"
#import "StateContainer.h"
#import "locationController.h"

@implementation DebugViewController
@synthesize accLabel;
@synthesize locateButton;
@synthesize gpsSwitch;
@synthesize thLabel;
@synthesize phLabel;
@synthesize locCountLabel;
@synthesize eightBallText;
@synthesize eightBallButton;

-(NSString *)double2strVar:(NSString *) var Val: (double) x{
    return [NSString stringWithFormat:@"%@%f",var,x];
}

-(NSString *)int2strVar:(NSString *) var Val: (int) x{
    return [NSString stringWithFormat:@"%@%i",var,x];
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
    [thLabel release];
    [phLabel release];
    [locCountLabel release];
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
    double th = GlobalState.sc.loc.th;
    double ph = GlobalState.sc.loc.ph;
    int nCount = GlobalState.sc.locCount;
    
    self.thLabel.text = [self double2strVar: @"Th = " Val: th];
    self.phLabel.text = [self double2strVar: @"Ph = " Val: ph];
    self.locCountLabel.text = [self int2strVar: @"n = " Val: nCount];
}

-(IBAction) gpsToggled:(id) sender{
    CLLocationManager *cl = GlobalState.sc.locController.locationMgr;
    if(gpsSwitch.on){
        [cl startUpdatingLocation];
    }else{
        [cl stopUpdatingLocation];
    }
}

-(IBAction) eightBallDown:(id) sender{
    NSString *msg = [[GlobalState sc] randomEightBallMessage];
    eightBallText.text = msg;
}

@end
