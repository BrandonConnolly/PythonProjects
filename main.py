#Robot Project
#Author Brandon Connolly


def start():
     robot_ctrl.set_mode(rm_define.robot_mode_free)
    # Move the robot to within 1 meter of the marker.
     chassis_ctrl.move_with_distance(0,1.4)
     chassis_ctrl.rotate_with_degree(rm_define.aniticlockwise, 90)
     chassis_ctrl.move_with_distance(0,.6)
    # Scan for a marker.  This function is set up before the start().scan_for_marker()
marker_found = False
def scan_for_marker():
# Turn on detection and scan left and right until you hit a marker.
    global marker_found
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    marker_found = False
    gimbal_ctrl.yaw_ctrl(-90)
    while marker_found == False:
        gimbal_ctrl.yaw_ctrl(+180)
        gimbal_ctrl.yaw_ctrl(-180)
def vision_recognized_marker_letter_F(msg):
    global marker_found
    vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    gun_ctrl.fire_once()
    marker_found = True

gun_ctrl.fire_once()
vision_ctrl.enable_detection(rm_define.vision_detection_marker)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_[F, ..., Z])
#vision_ctrl.disable_detection(rm_define.vision_detection_marker)
Marker_info = vision_ctrl.get_marker_detection_info()
print(Marker_info)
    if Marker_info[F] == F:
        gun_ctrl.fire_once()
#Hallway Travel

if(room_one == 1):
def start():
    room_one = 1 #fire
    room_two = 2 #skip
    room_three = 3 #fire
    room_four = 4 #person



    robot_ctrl.set_mode(rm_define.robot_mode_free)
    chassis_ctrl.set_trans_speed(0.1)
    #moving to room one
    ########hallway part one
    chassis_ctrl.move_with_distance(0, 3.5814)
    chassis_ctrl.move_with_distance(0, 3.8)
    #rotate to face the door
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    #drvie through the door
    #this code is entering room one
    chassis_ctrl.move_with_distance(0, 4.8)

    #rotate to face the the F

    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    #scan_for_fire()

    #leaving room
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.move_with_distance(0, 4.8)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)

    #########moving down hall
    #hallway part 2
    chassis_ctrl.move_with_distance(0, 3.7973)
    chassis_ctrl.move_with_distance(0, 3.7973)

    #turning with the floor
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 45)
    chassis_ctrl.move_with_distance(0, 2.7178)

    #going to room 2
    chassis_ctrl.move_with_distance(0, 2.7686)
    chassis_ctrl.move_with_distance(0, 2.7686)
    gimbal_ctrl.yaw_ctrl(230)

    #scan for for 2 don't enter
    #add sound effect

    #move forward to next room
    ########## moving to room 3
    chassis_ctrl.move_with_distance(0, 4.1656)
    chassis_ctrl.move_with_distance(0, 4.1656)
#####Entering room 3
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90);
    chassis_ctrl.move_with_distance(0, 3.5052)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90);
    chassis_ctrl.move_with_distance(0, 1.4478)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0, 3.6068)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.move_with_distance(0, 1.2192)
    #scan for code
    #leaving room 3
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
    chassis_ctrl.move_with_distance(0, 1.2192)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0, 3.6068)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.move_with_distance(0, 1.4478)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0, 3.5052)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)

    robot_ctrl.set_mode(rm_define.robot_mode_free)
    # Set Rotate Speed: This set speed of the Gimble
    gimbal_ctrl.set_rotate_speed(60)
    # set_trans_speed sets the movement speed of the robot in meters per second
    chassis_ctrl.set_trans_speed(0.5)
##### Moving to room 4

    chassis_ctrl.move_with_distance(0, 3.4120)
    chassis_ctrl.move_with_distance(0, 3.4120)
    gimbal_ctrl.recenter()

     # Rotate with degree takes in a direction of rotation, and a number of degrees for
    # the bot to rotate.
#####Entering room 4
    chassis_ctrl.move_with_distance(0, 2)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.move_with_distance(0, 2)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    #scan for code
    #leaving room 4
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    chassis_ctrl.move_with_distance(0, 2)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    chassis_ctrl.move_with_distance(0, 2)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
#######moving back to the start
    gimbal_ctrl.recenter()
    chassis_ctrl.move_with_distance(0, 3.4120)
    chassis_ctrl.move_with_distance(0, 3.4120)
    chassis_ctrl.move_with_distance(0, 4.1656)
    chassis_ctrl.move_with_distance(0, 4.1656)
    chassis_ctrl.move_with_distance(0, 2.7686)
    chassis_ctrl.move_with_distance(0, 2.7686)
####### reset start point
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 45)
    chassis_ctrl.move_with_distance(0, 3)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 40)
    chassis_ctrl.move_with_distance(0, 3.7973)
    chassis_ctrl.move_with_distance(0, 3.7973)
    chassis_ctrl.move_with_distance(0, 3.5814)
    chassis_ctrl.move_with_distance(0, 3.8)
