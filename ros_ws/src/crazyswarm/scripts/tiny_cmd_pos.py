from pycrazyswarm import *
import numpy as np

swarm = Crazyswarm()
timeHelper = swarm.timeHelper
allcfs = swarm.allcfs
cf = swarm.allcfs.crazyflies[0]
cf.initialPosition = cf.position()
Z = 0
# takeoff
while Z < 0.6:
    pos = np.array(cf.initialPosition) + np.array([0, 0, Z])
    cf.cmdPosition(pos)
    timeHelper.sleep(0.2)
    Z += 0.05

timeHelper.sleep(0.5)

print("Switching controller")
cf.setParam("stabilizer/controller", 5)  # MPC
timeHelper.sleep(0.1)

for k in range(5):
    pos = np.array(cf.initialPosition) + np.array([0.5, 0, Z])
    cf.cmdPosition(pos)
    timeHelper.sleep(0.5)

for k in range(5):
    pos = np.array(cf.initialPosition) + np.array([0, 0, Z])
    cf.cmdPosition(pos)
    timeHelper.sleep(0.5)

# land
while Z > 0.05:
    pos = np.array(cf.initialPosition) + np.array([0, 0, Z])
    cf.cmdPosition(pos)
    timeHelper.sleep(0.2)
    Z -= 0.05

# turn-off motors
cf.cmdStop()
