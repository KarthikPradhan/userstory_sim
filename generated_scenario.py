from beamngpy import BeamNGpy, Scenario, Vehicle, StaticObject
import numpy as np
from time import sleep, time

beamng = BeamNGpy('localhost', 64256, home = r'C:\BeamNG_unlimited\trunk' )
vehicle = Vehicle('ego', model='etk800', licence='PYTHON', colour='Green')
scenario = Scenario('west_coast_usa', 'ai_sine')
# scenario.add_vehicle(vehicle, pos=(-198.5, -164.189, 119.7), rot=(0, 0, -126.25))
scenario.add_vehicle(vehicle, pos=(-24.8179, -37.308, 119.86), rot=(0, 0, -126.25))
# so = StaticObject('stato', pos=(-140, -121.233, 119.586), rot=(0, 0, 55), scale=(1, 1, 1), shape='/levels/west_coast_usa/art/shapes/objects/barrierfence_folk.dae')
so = StaticObject('stato', pos=(2.91697, -12.596, 119.58), rot=(0, 0, 55), scale=(1, 1, 1), shape='/levels/west_coast_usa/art/shapes/objects/barrierfence_folk.dae')
scenario.add_object(so)
scenario.make(beamng)

bng = beamng.open()
bng.load_scenario(scenario)
bng.start_scenario()

vehicle.ai_set_mode('span')
vehicle.ai_drive_in_lane(True)

# scenario.update()
dist_buffer = 0
for _ in range(240):
    sleep(0.1)
    scenario.update()
    distance = np.linalg.norm(np.array(vehicle.state['pos']) - np.array([2.91697, -12.596, 119.58]))
    vehicle.update_vehicle()
    print(distance)
#     # scenario.update()
#     vehicle.update_vehicle()
#     distance = np.linalg.norm(np.array(vehicle.state['pos']) - [2.91697, -12.596, 119.58])
#     log.debug('DISTANCE %s', distance)
    # while distance <= 15:
    #     scenario.update()
    #     distance = np.linalg.norm(np.array(vehicle.state['pos']) - [2.91697, -12.596, 119.58])
    #     log.debug('dadaadad')

