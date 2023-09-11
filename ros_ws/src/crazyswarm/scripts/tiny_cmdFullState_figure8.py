#!/usr/bin/env python

"""
Figure-8 trajectory (x, y, z, yaw in 7th-order polynomial parameters) is computed and
sent to the drone. Works with TinyMPC.
"""

import numpy as np

from pycrazyswarm import *
import uav_trajectory


def executeTrajectory(timeHelper, cf, trajpath, rate=100, offset=np.zeros(3)):
    traj = uav_trajectory.Trajectory()
    traj.loadcsv(trajpath)

    start_time = timeHelper.time()
    while not timeHelper.isShutdown():
        t = timeHelper.time() - start_time
        if t > traj.duration:
            break

        e = traj.eval(t)
        cf.cmdFullState(
            e.pos + np.array(cf.initialPosition) + offset,
            e.vel,
            e.acc,
            e.yaw,
            e.omega)

        timeHelper.sleepForRate(rate)


if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf = swarm.allcfs.crazyflies[0]
    cf.initialPosition = cf.position()
    rate = 1.0
    Z = 1.0

    print("Switching controller")
    cf.setParam("stabilizer/controller", 1) 
    # cf.setParam("stabilizer/controller", 5) 
    timeHelper.sleep(1.0)

    cf.takeoff(targetHeight=Z, duration=Z+1.0)
    timeHelper.sleep(Z+2.5)

    # cf.setParam("usd/logging", 1) 
    print("Switching controller")
    # cf.setParam("stabilizer/controller", 5) 
    timeHelper.sleep(1.5)

    executeTrajectory(timeHelper, cf, "figure8.csv", rate, offset=np.array([0, 0, Z]))

    cf.notifySetpointsStop()

    cf.setParam("stabilizer/controller", 1) 
    # cf.setParam("usd/logging", 0) 

    cf.land(targetHeight=0.03, duration=Z+1.0)
    timeHelper.sleep(Z+2.0)
    # cf.setParam("stabilizer/controller", 1) 
