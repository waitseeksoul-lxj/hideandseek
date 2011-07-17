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

@implementation DebugViewController
@synthesize accLabel;
@synthesize locateButton;
@synthesize gpsSwitch;
@synthesize xLabel;
@synthesize yLabel;
@synthesize zLabel;
@synthesize locCountLabel;
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
    double r;
    StateContainer *sc = [GlobalState sc];
    if(gpsSwitch.on){
        r = sc.loc.r;
        r++;
        sc.loc.r = r;
        zLabel.text = [self double2strVar: @"r = " Val:r];
    }
}

-(IBAction) gpsToggled:(id) sender{
    if(gpsSwitch.on){
    }else{
        
    }
}

-(IBAction) eightBallDown:(id) sender{
    NSString *msg = [[GlobalState sc] randomEightBallMessage];
    eightBallText.text = msg;
}

@end
