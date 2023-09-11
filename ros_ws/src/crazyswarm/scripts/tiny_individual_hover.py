#!/usr/bin/env python

from __future__ import print_function

from pycrazyswarm import *

from pycrazyswarm import keyboard


def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf = allcfs.crazyflies[0]

    timeHelper.sleep(0.5)

    cf.setParam("stabilizer/controller", 1)
    print(f"crazyflie id: {cf.id}")
    cf.takeoff(1.0, 2.0)
    timeHelper.sleep(2.0)
    # cf.goTo([0, 0, 1], 0, 3.0)
    timeHelper.sleep(1.5)

    print("press any button to run MPC")

    with keyboard.KeyPoller() as keyPoller:
        # Wait until a key is pressed.
        while keyPoller.poll() is None:
            timeHelper.sleep(0.01)
        # Wait until the key is released.
        while keyPoller.poll() is not None:
            timeHelper.sleep(0.01)

    print("Switching to TinyMPC")

    cf.setParam("stabilizer/controller", 5) # 1: PID, 4: Brescianini, 5: TinyMPC

    print("press any button to land")

    # with keyboard.KeyPoller() as keyPoller:
        # Wait until a key is pressed. Send obstacle pose as a setpoint in the meantime.
        # while keyPoller.poll() is None:
            # 1. get new obstacle transform from mocap
            # 2. convert obstacle transform to xyz coords
            # 3. send transform as a setpoint with cf.goTo
            # cf.goTo([1.5, .5, 1.5], 0, 0.001)
        # Wait until the key is released.
        # while keyPoller.poll() is not None:
            # timeHelper.sleep(0.01)
    
    # cf.goTo([0, 0, 1], 0, 3.0)
    # timeHelper.sleep(2.0)

    print("Switching to controller 1")
    cf.setParam("stabilizer/controller", 1)
    timeHelper.sleep(0.1)
    cf.cmdPosition([0, 0, 0.5], yaw=0)
    cf.land(0.02, 2.5)
    timeHelper.sleep(2.5)

    # cf.cmdStop()

if __name__ == "__main__":
    main()
