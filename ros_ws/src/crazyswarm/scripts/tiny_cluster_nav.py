#!/usr/bin/env python

from __future__ import print_function

from pycrazyswarm import *

from pycrazyswarm import keyboard

import numpy as np

def check_closest_obs(rat_pos, obs_pos_all):
    dist = np.linalg.norm(obs_pos_all - rat_pos, axis=1)
    dist_min_idx = np.argmin(dist)       
    return obs_pos_all[dist_min_idx]

def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    rat = allcfs.crazyflies[0]  # avoid the obstacle

    timeHelper.sleep(0.5)

    rat.setParam("stabilizer/controller", 1)
    print(f"crazyflie id: {rat.id}")
    rat.takeoff(1.0, 2.0)
    timeHelper.sleep(2.0)
    rat.goTo([0, -1, 1.0], 0, 1.0)
    timeHelper.sleep(1.0)

    print("press any button to run MPC")

    with keyboard.KeyPoller() as keyPoller:
        # Wait until a key is pressed.
        while keyPoller.poll() is None:
            timeHelper.sleep(0.01)
        # Wait until the key is released.
        while keyPoller.poll() is not None:
            timeHelper.sleep(0.01)

    # swarm.input.waitUntilButtonPressed()
    print("Switching to TinyMPC")
    # rat.setParam("usd/logging", 1)
    rat.setParam("stabilizer/controller", 5)  # 1: PID, 4: Brescianini, 5: TinyMPC

    width = 0.7
    obs_rad = 0.3

    obs_pos_all = [
        [0, 0, 1],
        [0, -0.5, 1],
        # [0, with, 1],
        [-width, 0, 1],
        [width, 0, 1],
        [width, -width, 1],
        [-width, -width, 1],
        [width, width, 1],
        [-width, width, 1],

        [0, 0, width],
        [0, -0.5, width],
        # [0, width, width],
        [-width, 0, width],
        [width, 0, width],
        [width, -width, width],
        [-width, -width, width],
        [width, width, width],
        [-width, width, width],
    ]

    # obs_pos_all = [
    #     [0, 0.4, 0.8],
    #     [0, 0.4, 1.2],
    #     [0, -0.4, 1.2],
    #     [0, -0.4, 0.8],
    # ]

    rat.goTo([0, 0, 0], 0, 0.001)

    # print("press any button to land")
    for i in range(1000):
        rat_pos = rat.position()
        obs_pos = check_closest_obs(rat_pos, obs_pos_all)
        print("rat at:", rat_pos)
        rat.cmdPosition(obs_pos, yaw=obs_rad)
        # rat.goTo(obs_pos, obs_rad, 0.001)
        timeHelper.sleep(0.01)

    # # obs_pos = [0.3, 0, 0.4]
    # with keyboard.KeyPoller() as keyPoller:
    #     # Wait until a key is pressed. Send obstacle pose as a setpoint in the meantime.
    #     while keyPoller.poll() is None:
    #         # 1. get new obstacle transform from mocap
    #         # 2. convert obstacle transform to xyz coords
    #         # 3. send transform as a setpoint with cf.goTo
    #         rat_pos = rat.position() - [0, 0, 0.4]
    #         # rat.goTo(obs_pos, 0, 0.5)
    #         rat.cmdPosition(rat_pos, yaw=0)
    #         timeHelper.sleep(0.1)
    #     # Wait until the key is released.
    #     while keyPoller.poll() is not None:
    #         # rat_pos = rat.position() - [0.5, 0, 0.4]
    #         rat.cmdPosition(rat_pos, yaw=0)
    #         timeHelper.sleep(1.0)

    # swarm.input.waitUntilButtonPressed()
    # rat.setParam("usd/logging", 0)
    print("Switching to controller 1")
    rat.setParam("stabilizer/controller", 1)
    timeHelper.sleep(0.1)
    rat.cmdPosition([0, 1, 0.5], yaw=0)
    timeHelper.sleep(0.5)
    rat.land(0.02, 2)
    timeHelper.sleep(2)

    # cf.cmdStop()


if __name__ == "__main__":
    main()
