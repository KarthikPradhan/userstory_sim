from beamngpy import BeamNGpy, Scenario, Vehicle, StaticObject
from beamngpy.sensors import Electrics
import numpy as np
from time import sleep, time

beamng = BeamNGpy('localhost', 64256, home=r'C:\BeamNG_unlimited\trunk')
scenario = Scenario('west_coast_usa', 'fourway_intersection_w_obj')

vut = Vehicle('vut', model='coupe', licence='VUT', colour='Red')
electrics = Electrics()
vut.attach_sensor('electrics', electrics)
scenario.add_vehicle(vut, pos=(-198.5, -164.189, 119.7), rot=(0, 0, -126.25))

obj_1 = StaticObject('obj_1', pos=(-140, -121.233, 119.586), rot=(0, 0, 55), scale=(1, 1, 1), shape='/levels/west_coast_usa/art/shapes/objects/barrierfence_folk.dae')
scenario.add_object(obj_1)

scenario.make(beamng)
bng = beamng.open(launch=True)
bng.load_scenario(scenario)
bng.start_scenario()

vut.ai_set_mode('span')
vut.ai_drive_in_lane(True)


for _ in range(240):
    sleep(0.1)
    vut.update_vehicle()
    sensors = bng.poll_sensors(vut)
    
    # Below code snippet is generated form 'detect_obstacle_car' function for obj_1
    scenario.update()
    dist_obj_1 = np.linalg.norm(np.array(vut.state['pos']) - np.array([2.91697, -12.596, 119.58]))
    
    if dist_obj_1 < 8:
        print('Obstacle Detected')
    
        # Below code snippet is generated form 'ai_lane_changed' function
        scenario.update()
        ct__lane = np.array(vut.state['pos'])
        sleep(0.6)
        moved = np.linalg.norm(np.array(vut.state['pos']) - ct__lane)
    
        if moved >= 3.7:
            print('[Successful] Lane Changing Successful')
        else:
            print('[Failed] Lane Changing Failed')
    