from pycrazyswarm import *
import numpy as np

swarm = Crazyswarm()
timeHelper = swarm.timeHelper
allcfs = swarm.allcfs
cf = swarm.allcfs.crazyflies[0]
cf.initialPosition = cf.position()
Z = 0.4

print("Switching controller")
cf.setParam("stabilizer/controller", 1)  # 1: PID, 5: MPC
cf.takeoff(Z, 2)
timeHelper.sleep(2.0)


for k in range(50):
    pos = np.array(cf.initialPosition) + np.array([0, 0, Z])
    cf.cmdPosition(pos)
    timeHelper.sleep(0.1)

cf.land(0.05, 2.0)
timeHelper.sleep(2.0)


# turn-off motors
cf.cmdStop()

