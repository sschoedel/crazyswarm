#!/usr/bin/env python

import numpy as np
from pycrazyswarm import *


Z = 0.5
sleepRate = 30

# North first

def goCircle(timeHelper, cf, totalTime, radius, kPosition):
        startTime = timeHelper.time()
        pos = cf.position()
        startPos = pos + np.array([0, 0, Z])
        center_circle = startPos - np.array([radius, 0, 0])
        while True:
            time = timeHelper.time() - startTime
            omega = 2 * np.pi / totalTime
            vx = -radius * omega * np.sin(omega * time)  
            vy = radius * omega * np.cos(omega * time)
            desiredPos = center_circle + radius * np.array(
                [np.cos(omega * time), np.sin(omega * time), 0])
            errorX = desiredPos - cf.position() 
            cf.cmdVelocityWorld(np.array([vx, vy, 0] + kPosition * errorX), yawRate=0)
            timeHelper.sleepForRate(sleepRate)
            if (time > totalTime*2):
                break

if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf = swarm.allcfs.crazyflies[0]

    cf.takeoff(targetHeight=Z, duration=1.0+Z)
    timeHelper.sleep(2 + Z)

    print("Switching controller")
    cf.setParam("stabilizer/controller", 5) 
    timeHelper.sleep(0.5)

    goCircle(timeHelper, cf, totalTime=3, radius=1, kPosition=1)
    cf.land(targetHeight=0.06, duration=2.5)
    timeHelper.sleep(3.0)

    cf.setParam("stabilizer/controller", 1)  # return the original
    timeHelper.sleep(0.5)
    
    cf.land(targetHeight=0.05, duration=2.0)
    timeHelper.sleep(2.0)