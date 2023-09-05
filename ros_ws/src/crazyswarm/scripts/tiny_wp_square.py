"""Single CF: takeoff, follow absolute-coords waypoints, land."""

import numpy as np

from pycrazyswarm import Crazyswarm

# Start at South East
Z = 0.5
width = 1.5
TAKEOFF_DURATION = 1.5
GOTO_DURATION = 1.2
WAYPOINTS = np.array([
    (width, 0.0, Z),
    (width, width, Z),
    (0.0, width, Z),
    (0.0, 0.0, Z),
])


def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf = swarm.allcfs.crazyflies[0]

    cf.initialPosition = cf.position()

    cf.takeoff(targetHeight=Z, duration=TAKEOFF_DURATION)
    timeHelper.sleep(TAKEOFF_DURATION + 1.0)

    print("Switching controller")
    cf.setParam("stabilizer/controller", 5)  # MPC
    timeHelper.sleep(0.5)

    for p in WAYPOINTS:
        cf.goTo(cf.initialPosition + p, yaw=0.0, duration=GOTO_DURATION)
        timeHelper.sleep(GOTO_DURATION + 1.0)

    cf.setParam("stabilizer/controller", 1) 
    cf.land(targetHeight=0.05, duration=TAKEOFF_DURATION)
    timeHelper.sleep(TAKEOFF_DURATION + 1.0)


if __name__ == "__main__":
    main()
