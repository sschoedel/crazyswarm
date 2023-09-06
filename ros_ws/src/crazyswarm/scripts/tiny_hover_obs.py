#!/usr/bin/env python

from __future__ import print_function

from pycrazyswarm import *

from pycrazyswarm import keyboard


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
    # rat.goTo([0, 0, 1], 0, 3.0)
    # timeHelper.sleep(1.5)

    # print("press any button to run MPC")

    # with keyboard.KeyPoller() as keyPoller:
    #     # Wait until a key is pressed.
    #     while keyPoller.poll() is None:
    #         timeHelper.sleep(0.01)
    #     # Wait until the key is released.
    #     while keyPoller.poll() is not None:
    #         timeHelper.sleep(0.01)

    print("Switching to TinyMPC")
    rat.setParam("stabilizer/controller", 5) # 1: PID, 4: Brescianini, 5: TinyMPC
    # rat.goTo([0, 0, 0], 0, 0.001) # Move obstacle out of the way

    # print("press any button to land")
    for i in range(30):
        rat_pos = rat.position() - [0, 0, 0.4]
        rat.cmdPosition(rat_pos, yaw=0)
        timeHelper.sleep(0.1)

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
    
    
    print("Switching to controller 1")
    timeHelper.sleep(0.1)
    rat.setParam("stabilizer/controller", 1 )
    timeHelper.sleep(2.0)
    rat.land(0.02, 2.5)
    timeHelper.sleep(2.5)

    # cf.cmdStop()

if __name__ == "__main__":
    main()
