#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialize the EV3 Brick.
ev3 = EV3Brick()
flag_side=True
flag_side_start=True
flag_side_end=True
stop=False
flag_stop=False

# Initialize the motors.
left_motor = Motor(Port.D)
right_motor = Motor(Port.A)
font_motor = Motor(Port.B)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Initialize the Ultrasonic Sensor. It is used to detect
# obstacles as the robot drives around.
print(UltrasonicSensor(Port.S1))
obstacle_sensor_right = UltrasonicSensor(Port.S1)
obstacle_sensor_font = UltrasonicSensor(Port.S3)
obstacle_sensor_back = UltrasonicSensor(Port.S2)

# Play a sound to tell us when we are ready to start moving
ev3.speaker.beep()
dis_state_start=0
dis_state_end=0

### Check the side obstacles
robot.drive(50, 0)

while flag_stop==False:

    if obstacle_sensor_right.distance()<150  and obstacle_sensor_font.distance()>100:
        flag_side=False
    print("obstacle_sensor_right.distance()::",obstacle_sensor_right.distance())

    # If there are obstacles
    while flag_side==False and obstacle_sensor_right.distance()<150:
        flag_side_start=False
        state_freelist = robot.state()  # Distance, drive speed, angle, turn rate
        dis_state_start=state_freelist[0]
        print("obstacle_sensor_right.distance()::",obstacle_sensor_right.distance())

        while flag_side_start==False and obstacle_sensor_right.distance()>100:
            state_freelist2=robot.state()
            dis_state_end=state_freelist2[0]
            flag_side_end=False
            print("dis_state_end::",dis_state_end)
            print("dis_state_end-dis_state_start::",dis_state_end-dis_state_start)
            # print("dis_state_end-dis_state_start::",dis_state_end-dis_state_start)
            while dis_state_end-dis_state_start>300:
                # robot.turn(45)
                # robot.straight(100,0)
                # robot.turn(45)
                # robot.straight(100,0)
                font_motor.turn(45)
                robot.drive(-100,0)
                print("state:",robot.state())
                state=robot.state()

                while obstacle_sensor_back.distance()>100 and state[2]==90:
                    font_motor.turn(-45)
                    robot.drive(-100,0)
                    print("robot dis::",robot.state())
                    flag_stop=True
# else:
#     robot.drive(100,0)


