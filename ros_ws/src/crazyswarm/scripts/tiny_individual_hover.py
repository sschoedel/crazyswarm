#!/usr/bin/env python

from __future__ import print_function

from pycrazyswarm import *

CONTROLLER_NUM = 5

def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf = allcfs.crazyflies[0]

    cf.setParam("stabilizer/controller", CONTROLLER_NUM) # 1: PID, 2: mellinger, 5: MPC
    print(cf.id)
    cf.takeoff(0.5, 2.0)

    print("press button to continue")
    swarm.input.waitUntilButtonPressed()
    
    print("Switching to controller 5")
    cf.setParam("stabilizer/controller", CONTROLLER_NUM) # 1: PID, 2: mellinger, 5: MPC

    print("press button to continue")
    swarm.input.waitUntilButtonPressed()

    print("Switching to controller 1")
    cf.setParam("stabilizer/controller", 1) # 1: PID, 2: mellinger, 5: MPC
    # timeHelper.sleep(0.5)
    # cf.setParam("stabilizer/controller", CONTROLLER_NUM) # 1: PID, 2: mellinger, 5: MPC
    cf.land(0.05, 2.5)
    timeHelper.sleep(2.5)

    cf.cmdStop()

if __name__ == "__main__":
    main()
