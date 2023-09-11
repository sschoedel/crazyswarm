#!/usr/bin/env python

from __future__ import print_function

from pycrazyswarm import *

frequency = 500     # control frequency

def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf = allcfs.crazyflies[0]
    print(f"crazyflie id: {cf.id}")

    # cf.setParam("stabilizer/controller", 1)
    cf.setParam("stabilizer/controller", 5) # 1: PID, 4: Brescianini, 5: TinyMPC
    cf.setParam("usd/logging", 1)
    # timeHelper.sleep(1.0)

    # cf.cmdPosition([0, 0, 1])
    cf.goTo([1.65, 1.2, 1.6], 0, 3)
    # cf.goTo([0, 0, 1.0], 0, 3)
    timeHelper.sleep(3.0)

    # print("Select controller to switch to: 1: PID, 2: mellinger, 3: INDI, 4: Brescianini, 5: TinyMPC")
    
    # print("Switching controller")  # Controller 5 doesn't care about cmd
    # cf.setParam("stabilizer/controller", 5) # 1: PID, 4: Brescianini, 5: TinyMPC
    timeHelper.sleep(3)
    cf.setParam("usd/logging", 0)
    timeHelper.sleep(1)

    # print("press any button to land")
    # swarm.input.waitUntilButtonPressed()

    print("Switching to controller 1")
    cf.setParam("stabilizer/controller", 1)
    # cf.goTo([0, 0, 0.2], 0, 3)
    cf.land(0.02, 2)
    timeHelper.sleep(2)

if __name__ == "__main__":
    main()
