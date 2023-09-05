#!/usr/bin/env python

"""
Figure-8 trajectory (x, y, z, yaw in 7th-order polynomial parameters) is uploaded
and executed internally. Works with TinyMPC.
"""

import numpy as np

from pycrazyswarm import *
import uav_trajectory

if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf = allcfs.crazyflies[0]
    cf.initialPosition = cf.position()

    traj1 = uav_trajectory.Trajectory()
    traj1.loadcsv("figure8.csv")

    Z = 0.6
    TRIALS = 1
    TIMESCALE = 1.0
    for i in range(TRIALS):
        for cf in allcfs.crazyflies:
            cf.uploadTrajectory(0, 0, traj1)

        allcfs.takeoff(targetHeight=Z, duration=2.0)
        timeHelper.sleep(2.0)
        for cf in allcfs.crazyflies:
            pos = np.array(cf.initialPosition) + np.array([0, 0, Z])
            cf.goTo(pos, 0, 2.0)
        timeHelper.sleep(2.0)

        # cf.setParam("usd/logging", 1) 
        print("Switching controller")
        cf.setParam("stabilizer/controller", 5) 
        timeHelper.sleep(0.5)

        allcfs.startTrajectory(0, timescale=TIMESCALE)
        timeHelper.sleep(traj1.duration * TIMESCALE + 1.0)
        # allcfs.startTrajectory(0, timescale=TIMESCALE, reverse=True)
        # timeHelper.sleep(traj1.duration * TIMESCALE + 1.0)
        
        # cf.setParam("usd/logging", 0) 
        cf.setParam("stabilizer/controller", 1) 
        allcfs.land(targetHeight=0.06, duration=2.0)
        timeHelper.sleep(3.0)
