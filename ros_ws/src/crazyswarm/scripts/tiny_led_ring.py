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

    off = 0b10000000
    cf.setParam('led/bitmask', off)
    cf.setParam('ring/effect', 4)
    cf.setParam('ring/headlightEnable', 0)
    cf.setParam('ring/solidRed', 0)
    cf.setParam('ring/solidGreen', 0)
    cf.setParam('ring/solidBlue', 20)    

    timeHelper.sleep(5.0)

    cf.setParam('ring/effect', 0)    

    # # Create a spinning effect using the onboard LEDs
    # for i in range(10):         
    #     for j in range(8):
    #         # Set black color effect
    #         cf.setParam('led/bitmask', bitSeq[j])
    #         timeHelper.sleep(0.15)

if __name__ == "__main__":
    main()
