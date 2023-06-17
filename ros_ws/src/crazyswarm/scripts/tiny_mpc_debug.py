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
    cf.takeoff(0.5, 2.0)
    timeHelper.sleep(3.0)

    
    print("Switching to MPC controller")
    cf.setParam("stabilizer/controller", 5) # 1: PID, 4: Brescianini, 5: TinyMPC
    timeHelper.sleep(5.0)

    print("Set no constraints")
    cf.setParam("ctrlMPC/stgs_cstr_inputs", 0) # 1: PID, 4: Brescianini, 5: TinyMPC    
    timeHelper.sleep(5.0)

    print("Switching to controller 1")
    cf.setParam("stabilizer/controller", 1)
    cf.land(0.02, 2.5)
    timeHelper.sleep(2.5)

    # cf.cmdStop()

if __name__ == "__main__":
    main()
