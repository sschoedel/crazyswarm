from pycrazyswarm import *
import numpy as np

swarm = Crazyswarm()
timeHelper = swarm.timeHelper
allcfs = swarm.allcfs
cf = swarm.allcfs.crazyflies[0]
cf.initialPosition = cf.position()
Z = 0

print("Switching controller")
cf.setParam("stabilizer/controller", 5)  # MPC
timeHelper.sleep(0.1)

# takeoff
while Z < 0.6:
    pos = np.array(cf.initialPosition) + np.array([0, 0, Z])
    cf.cmdPosition(pos)
    timeHelper.sleep(0.1)
    Z += 0.02

timeHelper.sleep(0.5)

# print("Switching controller")
# cf.setParam("stabilizer/controller", 5)  # MPC
# timeHelper.sleep(0.1)

for k in range(25):
    pos = np.array(cf.initialPosition) + np.array([0.5, 0, Z])
    cf.cmdPosition(pos)
    timeHelper.sleep(0.1)

for k in range(25):
    pos = np.array(cf.initialPosition) + np.array([0, 0, Z])
    cf.cmdPosition(pos)
    timeHelper.sleep(0.1)

# land
while Z > 0.05:
    pos = np.array(cf.initialPosition) + np.array([0, 0, Z])
    cf.cmdPosition(pos)
    timeHelper.sleep(0.1)
    Z -= 0.02

# turn-off motors
cf.cmdStop()
