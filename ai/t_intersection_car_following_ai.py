from beamngpy import BeamNGpy, Scenario, Vehicle, StaticObject
from beamngpy.sensors import Electrics, Damage
import numpy as np
from time import sleep, time

beamng = BeamNGpy('localhost', 64256, home=r'C:\BeamNG_unlimited\trunk')
scenario = Scenario('west_coast_usa', 't_intersection_car_following_ai')

vut = Vehicle('vut', model='coupe', licence='VUT', colour='Red')
electrics = Electrics()
damage = Damage()
vut.attach_sensor('electrics', electrics)
vut.attach_sensor('damage', damage)
scenario.add_vehicle(vut, pos=(-198.5, -164.189, 119.7), rot=(0, 0, -126.25))

car_1 = Vehicle('car_1', model='etk800', licence='CAR 1', colour='Blue')
scenario.add_vehicle(car_1, pos=(-140, -121.233, 119.586), rot=(0, 0, 55))

scenario.make(beamng)
bng = beamng.open(launch=True)
bng.load_scenario(scenario)
bng.start_scenario()

vut.ai_set_mode('span')
vut.ai_drive_in_lane(True)

car_1.ai_set_line([{'pos': (-198.5, -164.189, 119.7), 'speed': 2000}])

for _ in range(240):
    sleep(0.1)
    vut.update_vehicle()
    sensors = bng.poll_sensors(vut)
    dmg = sensors['damage']
    
    # Below code snippet is generated form 'detect_obstacle_car' function for car_1
    scenario.update()
    dist_car_1 = np.linalg.norm(np.array(vut.state['pos']) - np.array(car_1.state['pos']))
    
    if dist_car_1 < 8:
        print('Car Detected')
    
        # Below code snippet is generated form 'ai_following' function for car_1
        scenario.update()
        follow_car_1 = np.linalg.norm(np.array(vut.state['dir']) - np.array(np.array(car_1.state['dir'])))
        
        if follow_car_1 < 8 or dmg['damage'] == 0:
            print('[Successful] Car Following Successful')
        else:
            print('[Failed] Car Following Failed or the VUT is damaged')

    # Below code snippet is generated form 'car_stopped' function for car_1
    scenario.update()
    dist_car_1_prev = np.linalg.norm(np.array(vut.state['pos']) - np.array(np.array(car_1.state['pos'])))
    sleep(0.1)
    dist_car_1_next = np.linalg.norm(np.array(vut.state['pos']) - np.array(np.array(car_1.state['pos'])))

    if dist_car_1_next == dist_car_1_prev:
        print('Car Stopped')
        # Below code is written to make the self-driving car to come to a halt
        vut.ai_set_mode('stopping')
        # Below code snippet is generated form 'ai_stopped' function for car_1
        scenario.update()
        if sensors['electrics']['values']['wheelspeed'] == 0 or dmg['damage'] == 0:
            print('[Successful] VUT Stopped')
        else:
            print('[Failed] VUT Moved or Damaged')
    