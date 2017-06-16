#!/usr/bin/python

import numpy as np

class DiffDriveController():
    """
    Class used for controlling the robot linear and angular velocity
    """
    def __init__(self, max_speed, max_omega):
        # TODO for Student: Specify these parameters
        # kp > 0
        self.kp=2.
        # ka - kp > 0
        self.ka=4.
        # needs to be <0
        self.kb=-2.
        self.MAX_SPEED = max_speed
        self.MAX_OMEGA = max_omega
        
    def compute_vel(self, state, goal):
        """
        Function that computes the desired outputs given the state and goal
        Inputs:
        state - a numpy vector of size 3 by 1 with components (x,y,theta)
        goal - a numpy vector of size 2 by 1 specifying the location of the goal
        Outputs: a tuple with 3 elements
        v - a number specifying the forward speed (in m/s) of the robot (should 
            be no more than max_speed)
        omega - a number specifying the angular velocity (in rad/s) of the robot
            (should be no more than max_omega)
        done - a boolean value specifying if the robot has reached its goal (or
            is close enough
        """
        # YOUR CODE HERE
        # compute the states from video
        dx = goal[0] - state[0]
        dy = goal[1] - state[1]
        th = state[2]

        # compute states for controller
        rh = np.sqrt(dx*dx + dy*dy)
        al = -th + np.arctan2(dy,dx)
        be = -th - al

        # compute control outputs
        v  = self.kp*rh
        om = self.ka*al + self.kb*be
        # if within 5cm, we're done
        done = ( rh < .05)

        return (v,om,done)

