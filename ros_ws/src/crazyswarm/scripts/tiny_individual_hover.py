#!/usr/bin/env python

from __future__ import print_function

from pycrazyswarm import *


def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf = allcfs.crazyflies[0]

    cf.setParam("stabilizer/controller", 1)
    print(f"crazyflie id: {cf.id}")
    cf.takeoff(0.25, 2.0)
    timeHelper.sleep(2.0)

    # print("Select controller to switch to: 1: PID, 2: mellinger, 3: INDI, 4: Brescianini, 5: TinyMPC")
    # button = swarm.input.waitUntilAnyButtonPressed()
    print("press any button to continue")
    swarm.input.waitUntilButtonPressed()
    
    print("Switching controller")
    cf.setParam("stabilizer/controller", 5) # 1: PID, 4: Brescianini, 5: TinyMPC

    print("press any button to land")
    swarm.input.waitUntilButtonPressed()

    print("Switching to controller 1")
    cf.setParam("stabilizer/controller", 1)
    cf.land(0.02, 2.5)
    timeHelper.sleep(2.5)

    cf.cmdStop()

if __name__ == "__main__":
    main()
