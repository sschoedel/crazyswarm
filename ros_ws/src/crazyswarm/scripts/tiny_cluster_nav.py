#!/usr/bin/env python

from __future__ import print_function

from pycrazyswarm import *

from pycrazyswarm import keyboard

import numpy as np

def check_closest_obs(rat_pos, obs_pos_all):
    dist = np.linalg.norm(obs_pos_all - rat_pos, axis=1)
    # dist_min_idx = np.argmin(dist)    
    dist_min_idxs = np.argsort(dist)
    # heuristics for better reaction
    if rat_pos[1] > obs_pos_all[dist_min_idxs[0]][1] - 0.1*0:
        return obs_pos_all[dist_min_idxs[1]]
    # return [obs_pos_all[dist_min_idxs[0]], obs_pos_all[dist_min_idxs[1]]]
    return obs_pos_all[dist_min_idxs[0]]

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
    rat.goTo([0, -1.5, 1.0], 0, 1.0)
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
    timeHelper.sleep(.5)
    rat.setParam("usd/logging", 1) # Begin logging data
    timeHelper.sleep(.5)
    rat.goTo([0, 0, -.5], 0, 0.001) # Move obstacle out of the way

    width = 0.7
    obs_rad = 0.3

    obs_pos_all = [
        [-0.1, 0.3, 1],
        [0.1, -0.5, 1],
        # [0, with, 1],
        [-width, 0, 1],
        [width, 0, 1],
        [width, -width, 1],
        [-width, -width, 1],
        [width, width, 1],
        [-width, width, 1],
    ]

    # obs_pos_all = [
    #     [0, 0.4, 0.8],
    #     [0, 0.4, 1.2],
    #     [0, -0.4, 1.2],
    #     [0, -0.4, 0.8],
    # ]

    max_rat_x = 0
    min_rat_x = 0
    with keyboard.KeyPoller() as keyPoller:
        # Wait until a key is pressed.
        while keyPoller.poll() is None:
            rat_pos = rat.position()
            if rat_pos[0] > max_rat_x:
                max_rat_x = rat_pos[0]
            if rat_pos[0] < min_rat_x:
                min_rat_x = rat_pos[0]
            obs_position = check_closest_obs(rat_pos, obs_pos_all)
            print("rat pos:", rat_pos)
            # rat.cmdFullState(obs_positions[0], obs_positions[1], [obs_rad, 0, 0], 0, [0, 0, 0])
            rat.cmdFullState(obs_position, [0, 0, 0], [.3, 0, 0], 0, [0, 0, 0])
            timeHelper.sleep(0.01)
        # Wait until the key is released.
        while keyPoller.poll() is not None:
            timeHelper.sleep(0.01)

    print(f"max x displacement: {max_rat_x}")
    print(f"min x displacement: {min_rat_x}")


    timeHelper.sleep(0.5)
    rat.setParam("usd/logging", 0)
    timeHelper.sleep(.5)

    print("Switching to controller 1")
    rat.setParam("stabilizer/controller", 1)
    timeHelper.sleep(0.1)
    rat.cmdPosition([0, 1.5, 1], yaw=0)
    timeHelper.sleep(0.5)
    rat.land(0.02, 2)
    timeHelper.sleep(2)



    # cf.cmdStop()


if __name__ == "__main__":
    main()
