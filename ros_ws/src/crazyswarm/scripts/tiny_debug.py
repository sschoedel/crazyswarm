from pycrazyswarm import *
import numpy as np

swarm = Crazyswarm()
timeHelper = swarm.timeHelper
allcfs = swarm.allcfs
cf = swarm.allcfs.crazyflies[0]
cf.initialPosition = cf.position()
Z = 0.5

print("Switching controller")
cf.setParam("stabilizer/controller", 1)  # MPC
timeHelper.sleep(0.1)

for k in range(20):
    pos = np.array(cf.initialPosition) + np.array([0, 0, Z])
    cf.cmdPosition(pos)
    timeHelper.sleep(0.1)

for k in range(70):
    pos = np.array(cf.initialPosition) + np.array([0, 0, Z])
    cf.cmdPosition(pos)
    timeHelper.sleep(0.1)

# turn-off motors
cf.cmdStop()
