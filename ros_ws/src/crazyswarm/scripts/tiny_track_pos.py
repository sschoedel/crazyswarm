#!/usr/bin/env python

from __future__ import print_function

from pycrazyswarm import *

frequency = 500     # control frequency
trajLength = 1405   # for delay time 
trajIter = 1        # number of laps
trajHold = 2        # 1 is most agressive

def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf = allcfs.crazyflies[0]
    print(f"crazyflie id: {cf.id}")

    cf.setParam("stabilizer/controller", 1) 
    cf.takeoff(1.0, 2.0)  
    timeHelper.sleep(2.1)
    cf.goTo([0, 0, 1.0], 0, 2)
    timeHelper.sleep(2.0)

    # print("Select controller to switch to: 1: PID, 2: mellinger, 3: INDI, 4: Brescianini, 5: TinyMPC")
    
    print("START: Switching controller task")
    cf.setParam("usd/logging", 1)
    # cf.setParam("stabilizer/en_vel_ref", 1) 
    # cf.setParam("stabilizer/en_traj", 1)

    cf.setParam("stabilizer/controller", 5) # 1: PID, 4: Brescianini, 5: TinyMPC

    # cf.setParam("ctrlMPC/trajHold", trajHold)
    # cf.setParam("ctrlMPC/trajIter", trajIter)
    # cf.setParam("ctrlMPC/trajLength", trajLength)
    # cf.setParam("ctrlMPC/uHover", uHover)
    
    timeHelper.sleep(trajIter*trajLength*trajHold/frequency)
    cf.setParam("usd/logging", 0)
    timeHelper.sleep(1.0)    
    
    # cf.setParam("stabilizer/en_traj", 0)
    print("END: Switching to controller 1")
    cf.setParam("stabilizer/controller", 1)   

    timeHelper.sleep(2.0)
    cf.goTo([0, 0, 0.1], 0, 2)
    timeHelper.sleep(2.0)
    cf.land(0.02, 2.0)
    timeHelper.sleep(2.0)

if __name__ == "__main__":
    main()
