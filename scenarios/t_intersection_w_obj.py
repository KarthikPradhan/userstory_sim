from beamngpy import BeamNGpy, Scenario, Vehicle, StaticObject
from beamngpy.sensors import Electrics, Damage
import numpy as np
from time import sleep, time

beamng = BeamNGpy('localhost', 64256, home=r'C:\BeamNG_unlimited\trunk')
scenario = Scenario('west_coast_usa', 't_intersection_w_obj')

vut = Vehicle('vut', model='coupe', licence='VUT', colour='Red')
electrics = Electrics()
damage = Damage()
vut.attach_sensor('electrics', electrics)
vut.attach_sensor('damage', damage)
scenario.add_vehicle(vut, pos=(-198.5, -164.189, 119.7), rot=(0, 0, -126.25))

obj_1 = StaticObject('obj_1', pos=(-140, -121.233, 119.586), rot=(0, 0, 55), scale=(1, 1, 1), shape='/levels/west_coast_usa/art/shapes/objects/barrierfence_folk.dae')
scenario.add_object(obj_1)

car_1 = Vehicle('car_1', model='etk800', licence='CAR 1', colour='Blue')
scenario.add_vehicle(car_1, pos=(-140, -121.233, 119.586), rot=(0, 0, 55))

car_2 = Vehicle('car_2', model='etk800', licence='CAR 2', colour='Blue')
scenario.add_vehicle(car_2, pos=(-140, -121.233, 119.586), rot=(0, 0, 55))

scenario.make(beamng)
bng = beamng.open(launch=True)
bng.load_scenario(scenario)
bng.start_scenario()

vut.ai_set_mode('span')
vut.ai_drive_in_lane(True)

car_1.ai_set_line([{'pos': (-198.5, -164.189, 119.7), 'speed': 2000}])
car_2.ai_set_line([{'pos': (-198.5, -164.189, 119.7), 'speed': 2000}])

for _ in range(240):
    sleep(0.1)
    vut.update_vehicle()
    sensors = bng.poll_sensors(vut)
    dmg = sensors['damage']
    
    # Below code snippet is generated form 'detect_obstacle_car' function for obj_1
    scenario.update()
    dist_obj_1 = np.linalg.norm(np.array(vut.state['pos']) - np.array([2.91697, -12.596, 119.58]))
    
    if dist_obj_1 < 8:
        print('Obstacle Detected')
    
        # Below code snippet is generated form 'ai_moving' function for obj_1
        scenario.update()
        if sensors['electrics']['values']['wheelspeed'] > 0 or dmg['damage'] == 0:
            print('[Successful] VUT is moving')
        else:
            print('[Failed] VUT Stopped or Damaged')
    
    # Below code snippet is generated form 'detect_obstacle_car' function for car_2
    scenario.update()
    dist_car_2 = np.linalg.norm(np.array(vut.state['pos']) - np.array(car_2.state['pos']))
    
    if dist_car_2 < 8:
        print('Car Detected')
    
        # Below code snippet is generated form 'ai_stopped' function for car_2
        scenario.update()
        if sensors['electrics']['values']['wheelspeed'] == 0 or dmg['damage'] == 0:
            print('[Successful] VUT Stopped')
        else:
            print('[Failed] VUT Moved or Damaged')
    
    # Below code snippet is generated form 'car_passed' function for car_2
    scenario.update()
    dist_car_2_prev = np.linalg.norm(np.array(vut.state['pos']) - np.array(np.array(car_2.state['pos'])))
    sleep(0.1)
    dist_car_2_next = np.linalg.norm(np.array(vut.state['pos']) - np.array(np.array(car_2.state['pos'])))

    if dist_car_2_next > dist_car_2_prev:
        print('Car Passed')
    
        # Below code snippet is generated form 'ai_moving' function for car_2
        scenario.update()
        if sensors['electrics']['values']['wheelspeed'] > 0 or dmg['damage'] == 0:
            print('[Successful] VUT is moving')
        else:
            print('[Failed] VUT Stopped or Damaged')
    
    # Below code snippet is generated form 'detect_obstacle_car' function for car_1
    scenario.update()
    dist_car_1 = np.linalg.norm(np.array(vut.state['pos']) - np.array(car_1.state['pos']))
    
    if dist_car_1 < 8:
        print('Car Detected')
    
        # Below code snippet is generated form 'ai_stopped' function for car_1
        scenario.update()
        if sensors['electrics']['values']['wheelspeed'] == 0 or dmg['damage'] == 0:
            print('[Successful] VUT Stopped')
        else:
            print('[Failed] VUT Moved or Damaged')
    
    # Below code snippet is generated form 'car_passed' function for car_1
    scenario.update()
    dist_car_1_prev = np.linalg.norm(np.array(vut.state['pos']) - np.array(np.array(car_1.state['pos'])))
    sleep(0.1)
    dist_car_1_next = np.linalg.norm(np.array(vut.state['pos']) - np.array(np.array(car_1.state['pos'])))

    if dist_car_1_next > dist_car_1_prev:
        print('Car Passed')
    
        # Below code snippet is generated form 'ai_moving' function for car_1
        scenario.update()
        if sensors['electrics']['values']['wheelspeed'] > 0 or dmg['damage'] == 0:
            print('[Successful] VUT is moving')
        else:
            print('[Failed] VUT Stopped or Damaged')
    