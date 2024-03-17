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

    # blue m3, green m4, green m1, blue m2, blue m3, red m4, red m1, blue m2
    bitSeq = [0b10000001, 0b10000010, 0b10001000, 0b10100000,
          0b10000001, 0b10000100, 0b10010000, 0b10100000] 
    green = 0b10001010
    blue  = 0b10100001
    red   = 0b10010100
    off   = 0b10000000

    cf.setParam('led/bitmask', off)

    timeHelper.sleep(2.0)

    # # Create a spinning effect using the onboard LEDs
    # for i in range(10):         
    #     for j in range(8):
    #         # Set black color effect
    #         cf.setParam('led/bitmask', bitSeq[j])
    #         timeHelper.sleep(0.15)

if __name__ == "__main__":
    main()
