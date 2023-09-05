#!/usr/bin/env python

from __future__ import print_function

from pycrazyswarm import *

from pycrazyswarm import keyboard


def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    rat = allcfs.crazyflies[1]  # avoid the cat

    timeHelper.sleep(0.5)

    rat.setParam("stabilizer/controller", 1)
    print(f"crazyflie id: {rat.id}")
    rat.takeoff(1.0, 2.0)
    timeHelper.sleep(2.0)
    rat.goTo([0, 0, 1], 0, 3.0)
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

    rat.setParam("stabilizer/controller", 5) # 1: PID, 4: Brescianini, 5: TinyMPC
    rat.goTo([0, 0, 0], 0, 0.001) # Move obstacle out of the way

    print("press any button to land")

    with keyboard.KeyPoller() as keyPoller:
        # Wait until a key is pressed. Send obstacle pose as a setpoint in the meantime.
        while keyPoller.poll() is None:
            # 1. get new obstacle transform from mocap
            # 2. convert obstacle transform to xyz coords
            # 3. send transform as a setpoint with cf.goTo
            rat.goTo([0, 0.1, 0.9], 0, 0.001)
            rat_pos = rat.position()
        # Wait until the key is released.
        while keyPoller.poll() is not None:
            timeHelper.sleep(0.01)

    print("Switching to controller 1")
    rat.setParam("stabilizer/controller", 1)
    rat.land(0.02, 2.5)
    timeHelper.sleep(2.5)

    # cf.cmdStop()

if __name__ == "__main__":
    main()
