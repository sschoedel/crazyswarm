#!/usr/bin/env python

from __future__ import print_function

from pycrazyswarm import *

from pycrazyswarm import keyboard

import time


def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf = allcfs.crazyflies[0]
    cf_obstacle = allcfs.crazyflies[1]

    timeHelper.sleep(0.5)

    cf.setParam("stabilizer/controller", 1)
    print(f"crazyflie id: {cf.id}")
    cf.takeoff(1.0, 2.0)
    timeHelper.sleep(2.0)
    cf.goTo([0, 0, 1], 0, 3.0)
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
    cf.setParam("usd/logging", 1) # Begin logging data
    cf.goTo([0, 0, 0], 0, 0.001) # Move obstacle out of the way

    print("press any button to land")

    velocity = [0, 0, 0]
    prev_position = [0, 0, 0]
    pos_time = time.time()

    with keyboard.KeyPoller() as keyPoller:
        # Wait until a key is pressed. Send obstacle pose as a setpoint in the meantime.
        while keyPoller.poll() is None:
            # 1. get new obstacle transform from mocap
            # 2. convert obstacle transform to xyz coords
            # 3. send transform as a setpoint with cf.goTo
            position = cf_obstacle.position()
            diff = time.time() - pos_time
            if max(position - prev_position) > 1e-6 or diff > 0.05:
                # print(["{0: 0.4f}".format(v_) for v_ in velocity])
                velocity = (position - prev_position)/diff
                prev_position = position
                pos_time = time.time()

            cf.cmdFullState(position, velocity, [0.8, 0, 0], 0, [0, 0, 0])
            timeHelper.sleep(0.001)
        # Wait until the key is released.
        while keyPoller.poll() is not None:
            timeHelper.sleep(0.01)
    
    cf.setParam("usd/logging", 0) # Stop logging data
    timeHelper.sleep(1)

    print("Switching to controller 1")
    cf.setParam("stabilizer/controller", 1)
    cf.goTo([0, 0, 1], 0, 3.0)
    timeHelper.sleep(2.0)
    cf.land(0.02, 2.5)
    timeHelper.sleep(2.5)

    # cf.cmdStop()

if __name__ == "__main__":
    main()
