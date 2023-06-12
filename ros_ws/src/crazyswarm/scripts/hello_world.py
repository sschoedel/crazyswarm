"""Takeoff-hover-land for one CF. Useful to validate hardware config."""

from pycrazyswarm import Crazyswarm


TAKEOFF_DURATION = 2.5
HOVER_DURATION = 5.0
TRAVEL_TIME = 4.0

offsetx = -4.5
offsety = -1

def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf = swarm.allcfs.crazyflies[0]

    cf.takeoff(targetHeight=0.5, duration=TAKEOFF_DURATION)
    timeHelper.sleep(TAKEOFF_DURATION)

    # cf.goTo([0+offsetx, 0+offsety, 1.0], 0, 3)
    # timeHelper.sleep(3)

    print("Switching to controller 5")
    cf.setParam("stabilizer/controller", 5) # 1: PID, 2: mellinger, 5: MPC

    
    # cf.goTo([0+offsetx, 1+offsety, 1], 0, TRAVEL_TIME)
    timeHelper.sleep(TRAVEL_TIME)
    # cf.goTo([1+offset, 1+offset, 1.0], 0, TRAVEL_TIME)
    # timeHelper.sleep(TRAVEL_TIME)
    # cf.goTo([1+offset, 0+offset, 1.0], 0, TRAVEL_TIME)
    # timeHelper.sleep(TRAVEL_TIME)
    # cf.goTo([0+offset, 0+offset, 1.0], 0, TRAVEL_TIME)
    # timeHelper.sleep(TRAVEL_TIME)

    timeHelper.sleep(1)

    print("Switching to controller 1")
    cf.setParam("stabilizer/controller", 1) # 1: PID, 2: mellinger
    cf.land(targetHeight=0.05, duration=2.5)
    timeHelper.sleep(TAKEOFF_DURATION)


if __name__ == "__main__":
    main()
