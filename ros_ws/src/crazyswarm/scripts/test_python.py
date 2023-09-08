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
    obs_pos_all = np.array([        
        [0.5, 0.5, 1],
        [0, 0, 1],
        [-0.5, 0.5, 1],
        [0.5, -0.5, 1],
        [-0.5, -0.5, 1],
    ])
    rat_pos = np.array([-0.5, 6, 1])
    obs_pos = check_closest_obs(rat_pos, obs_pos_all)
    print(obs_pos)

if __name__ == "__main__":
    main()
