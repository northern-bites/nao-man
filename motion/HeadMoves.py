# Constants file to store all head moves, including pans and simple moves

import StiffnessModes as stiff

HEAD_MOVE_LENGTH = 4

ZERO_HEADS = (((0.0,0.0),1.0,0, stiff.LOW_HEAD_STIFFNESSES),)

NEUT_HEADS = (((0.,20.),2.0,0, stiff.LOW_HEAD_STIFFNESSES),)

LOOK_DOWN = ( ((0.0,30.0), 0.8, 1, stiff.LOW_HEAD_STIFFNESSES), )

LOOK_UP =  ( ((0.0,-30.0), 0.8, 1, stiff.LOW_HEAD_STIFFNESSES), )

LOOK_RIGHT = ( ((-70.0,25.0), 0.8, 1, stiff.LOW_HEAD_STIFFNESSES), )

LOOK_LEFT =  ( ((70.0,25.0), 0.8, 1, stiff.LOW_HEAD_STIFFNESSES), )

PENALIZED_HEADS = (((0.0,25.0),0.5,0,stiff.LOW_HEAD_STIFFNESSES),)

FIND_BALL_HEADS_LEFT = (((45.,-10.),0.8,0, stiff.LOW_HEAD_STIFFNESSES),
                        ((45.,20.),0.3,1, stiff.LOW_HEAD_STIFFNESSES))

FIND_BALL_HEADS_RIGHT =  (((-45.,-10.),0.8,0, stiff.LOW_HEAD_STIFFNESSES),
                          ((-45.,200.),0.3,1, stiff.LOW_HEAD_STIFFNESSES))


# Distance that can be seen at a certain head pitch
# | degree | close | far |
# |     20 |    15 |  53 |
# |     -5 |    33 | 104 |
# |    -30 |   104 | inf |
#HEAD SCANS


#####################BASIC PANS##########################
LOC_PANS = (
    (( 65.0, 10.0),1.5, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.,-20.),1.0,  1, stiff.LOW_HEAD_STIFFNESSES),
    ((-65.,-20.),2.5, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((-65.0, 10.0) ,1., 1, stiff.LOW_HEAD_STIFFNESSES),
    (( 0.0, 10.0),1.5,  1, stiff.LOW_HEAD_STIFFNESSES),)

QUICK_PANS = (
    ((  0.0,-40.0),.3,  1, stiff.LOW_HEAD_STIFFNESSES),
    (( 30.0,-25.0),.3,  1, stiff.LOW_HEAD_STIFFNESSES),
    (( 65.0,-20.0),.4,  1, stiff.LOW_HEAD_STIFFNESSES),
    (( 30.0,-25.0),.4,  1, stiff.LOW_HEAD_STIFFNESSES),
    ((  0.0,-40.0),.3,  1, stiff.LOW_HEAD_STIFFNESSES),
    ((-30.0,-25.0),.3,  1, stiff.LOW_HEAD_STIFFNESSES),
    ((-65.0,-20.0),.4,  1, stiff.LOW_HEAD_STIFFNESSES),
    ((-30.0,-25.0),.4,  1, stiff.LOW_HEAD_STIFFNESSES))

######################PHOTO PANS########################

#pans full field inf to about 2/3m
HIGH_SNAPSHOT_PAN = (
    ((-65.0, -25.0), 0.6, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((0.0, -35.0), 0.6, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.0, -25.0), 0.6, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((0.0, -35.0), 0.6, 1, stiff.LOW_HEAD_STIFFNESSES))

#pans full field inf to about .15m
HIGH_MID_SNAPSHOT_PAN = (
    ((-65.0, -25.0), 0.6, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((0.0, -35.0), 0.6, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.0, -25.0), 0.6, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.0, -10.0), 0.4, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((-65.0, -10.0), 1.2, 1, stiff.LOW_HEAD_STIFFNESSES))

#pans full field about 1m to about .15m
MID_SNAPSHOT_PAN = (
    ((-65.0, -10.0), 0.4, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.0, -10.0), 1.2, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.0, 0.0), 0.4, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((-65.0, 0.0), 1.2, 1, stiff.LOW_HEAD_STIFFNESSES))

#pans full field about 2/3m to 0m
MID_LOW_SNAPSHOT_PAN = (
    ((-65.0, 0.0), 0.5, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.0, 0.0), 1.2, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.0, 20.0), 0.5, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((-65.0, 20.0), 1.2, 1, stiff.LOW_HEAD_STIFFNESSES))

#pans full field about .5m to 0m
LOW_SNAPSHOT_PAN = (
    ((-65.0, 5.0), 0.4, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.0, 5.0), 1.2, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.0, 20.0), 0.4, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((-65.0, 20.0), 1.2, 1, stiff.LOW_HEAD_STIFFNESSES))

#pans full field inf to 0m
COMB_SNAPSHOT_PAN = (
    ((-65.0, -25.0), 0.6, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((0.0, -35.0), 0.6, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.0, -25.0), 0.6, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.0, -10.0), 0.4, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((-65.0, -10.0), 1.2, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((-65.0, 0.0), 0.4, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.0, 0.0), 1.2, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.0, 20.0), 0.4, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((-65.0, 20.0), 1.2, 1, stiff.LOW_HEAD_STIFFNESSES))

#pans in front of robot inf to about 2/3m
FORWARD_HIGH_PAN = (
    ((-30.0, -30.0), 0.4, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((0.0, -35.0), 0.4, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((30.0, -30.0), 0.4, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((0.0, -35.0), 0.4, 1, stiff.LOW_HEAD_STIFFNESSES))

#pans in front of robot inf to about .15m
FORWARD_HIGH_MID_PAN = (
    ((-30.0, -30.0), 0.3, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((0.0, -35.0), 0.4, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((30.0, -30.0), 0.4, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((30.0, -10.0), 0.3, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((-30.0, -10.0), .8, 1, stiff.LOW_HEAD_STIFFNESSES))

#pans in front of robot about 1m to about .15m
FORWARD_MID_PAN = (
    ((-30.0, -10.0), 0.3, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((30.0, -10.0), .8, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((30.0, 0.0), 0.3, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((-30.0, 0.0), 0.8, 1, stiff.LOW_HEAD_STIFFNESSES))

#pans in front of robot about 2/3m to 0m
FORWARD_MID_LOW_PAN = (
    ((-30.0, 0.0), 0.3, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((30.0, 0.0), .8, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((30.0, 20.0), 0.3, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((-30.0, 20.0), 0.8, 1, stiff.LOW_HEAD_STIFFNESSES))

#pans in front of robot about .5m to 0m
FORWARD_LOW_PAN = (
    ((-30.0, 5.0), 0.3, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((30.0, 5.0), 0.8, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((30.0, 20.0), 0.3, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((-30.0, 20.0), 0.8, 1, stiff.LOW_HEAD_STIFFNESSES))

#pans in front of robot inf to 0m
FORWARD_COMB_PAN = (
    ((-30.0, -30.0), 0.6, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((0.0, -35.0), 0.4, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((30.0, -30.0), 0.4, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((30.0, -10.0), 0.3, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((-30.0, -10.0), 0.8, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((-30.0, 0.0), 0.3, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((30.0, 0.0), 0.8, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((30.0, 20.0), 0.3, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((-30.0, 20.0), 0.8, 1, stiff.LOW_HEAD_STIFFNESSES))

########################SCANS###########################

HIGH_SCAN_CLOSE_BOUND = 104
HIGH_SCAN_BALL = (
    (( -65.0, -25.0),0.6,  1, stiff.LOW_HEAD_STIFFNESSES),
    (( 0.0, -35.0),0.5, 1, stiff.LOW_HEAD_STIFFNESSES),
    (( 65.0, -25.0),0.5, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.,-5.),0.2,  1, stiff.LOW_HEAD_STIFFNESSES),
    ((-65.,-5.),1.0, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((-65.,20.),0.2,1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.,20.),1.0, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.0, -5.0) ,0.2, 1, stiff.LOW_HEAD_STIFFNESSES),
    (( -65.0, -5.0),1.0,  1, stiff.LOW_HEAD_STIFFNESSES),)

MID_SCAN_CLOSE_BOUND = 40
MID_SCAN_FAR_BOUND = 104
MID_DOWN_SCAN_BALL = (
    ((65.,-5.),0.6,  1, stiff.LOW_HEAD_STIFFNESSES),
    ((-65.,-5.),1.0, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((-65.,20.),0.2,1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.,20.),1.0, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.0, -5.0) ,0.2, 1, stiff.LOW_HEAD_STIFFNESSES),
    (( -65.0, -5.0),1.0,  1, stiff.LOW_HEAD_STIFFNESSES),
    (( -65.0, -25.0),0.2,  1, stiff.LOW_HEAD_STIFFNESSES),
    (( 0.0, -35.0),0.5,  1, stiff.LOW_HEAD_STIFFNESSES),
    (( 65.0, -25.0),0.5, 1, stiff.LOW_HEAD_STIFFNESSES),)

MID_UP_SCAN_BALL = (
    ((65.0, -5.0) ,0.6, 1, stiff.LOW_HEAD_STIFFNESSES),
    (( -65.0, -5.0),1.0,  1, stiff.LOW_HEAD_STIFFNESSES),
    (( -65.0, -25.0),0.2,  1, stiff.LOW_HEAD_STIFFNESSES),
    (( 0.0, -35.0),0.5,  1, stiff.LOW_HEAD_STIFFNESSES),
    (( 65.0, -25.0),0.5, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.,-5.),0.2,  1, stiff.LOW_HEAD_STIFFNESSES),
    ((-65.,-5.),1.0, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((-65.,20.),0.2,1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.,20.),1.0, 1, stiff.LOW_HEAD_STIFFNESSES),)

LOW_SCAN_CLOSE_BOUND = 0
LOW_SCAN_FAR_BOUND = 40
LOW_SCAN_BALL = (
    ((-65.,20.),0.6,1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.,20.),1.0, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.0, -5.0) ,0.2, 1, stiff.LOW_HEAD_STIFFNESSES),
    (( -65.0, -5.0),1.0,  1, stiff.LOW_HEAD_STIFFNESSES),
    (( -65.0, -25.0),0.4,  1, stiff.LOW_HEAD_STIFFNESSES),
    (( 0.0, -35.0),0.5,  1, stiff.LOW_HEAD_STIFFNESSES),
    (( 65.0, -25.0),0.5, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.,-5.),0.2,  1, stiff.LOW_HEAD_STIFFNESSES),
    ((-65.,-5.),1.0, 1, stiff.LOW_HEAD_STIFFNESSES),)

SQUAT_LOW_SCAN_BALL = (
    ((-65.,20.),0.6,1, stiff.LOW_HEAD_STIFFNESSES),
    ((0.,42.),0.5, 1,  stiff.LOW_HEAD_STIFFNESSES),
    ((65.,20.),0.5, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.0, -5.0) ,0.2, 1, stiff.LOW_HEAD_STIFFNESSES),
    (( -65.0, -5.0),1.0,  1, stiff.LOW_HEAD_STIFFNESSES),
    (( -65.0, -25.0),0.4,  1, stiff.LOW_HEAD_STIFFNESSES),
    (( 0.0, -35.0),0.5,  1, stiff.LOW_HEAD_STIFFNESSES),
    (( 65.0, -25.0),0.5, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((65.,-5.),0.2,  1, stiff.LOW_HEAD_STIFFNESSES),
    ((-65.,-5.),1.0, 1, stiff.LOW_HEAD_STIFFNESSES),)


POST_SCAN = (
    ((65.,-25.),2.0,  1, stiff.LOW_HEAD_STIFFNESSES),
    ((-65.,-25.),2.0, 1, stiff.LOW_HEAD_STIFFNESSES))


KICK_SCAN = (
    ((0.0,-45),0.5, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((90.,-20.),0.5,  1, stiff.LOW_HEAD_STIFFNESSES),
    ((0.0,-45),0.5, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((-90.,-20.),0.5, 1, stiff.LOW_HEAD_STIFFNESSES),
    ((0.0,40.),0.5,1,stiff.LOW_HEAD_STIFFNESSES))


PAN_LEFT_HEADS = ( 65.0, -20.0)

PAN_RIGHT_HEADS = ( -65.0, -20.0)

PAN_UP_HEADS = ( 0.0, -30.0)

PAN_DOWN_HEADS = (0.0, 35.0)

PAN_LEFT_DOWN_HEADS = (60.0, 25.0)

PAN_RIGHT_DOWN_HEADS = (-60.0, 25.0)

LOOK_HEADS = {'left' : PAN_LEFT_HEADS,
              'right' : PAN_RIGHT_HEADS,
              'up' : PAN_UP_HEADS,
              'down' : PAN_DOWN_HEADS,
              'leftDown' : PAN_LEFT_DOWN_HEADS,
              'rightDown' : PAN_RIGHT_DOWN_HEADS}

################### DATA COLLECTION PAN###############
DATA_PAN = (
    ((0.0,-45), 2.0, 0, stiff.LOW_HEAD_STIFFNESSES),
    ((0.0, 15), 2.0, 0, stiff.LOW_HEAD_STIFFNESSES))
