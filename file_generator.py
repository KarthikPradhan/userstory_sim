# Below assignments are the results of the corresponding scenarios
t_intersection_w_obj = [('moving', 'obstacle_noticed', 'moving'), ('moving', 'car_noticed', 'stopped'),
                        ('stopped', 'car_passed', 'moving'), ('moving', 'car_noticed', 'stopped'),
                        ('stopped', 'car_passed', 'moving')]
t_intersection_wo_obj = [('moving', 'car_noticed', 'stopped'), ('stopped', 'car_passed', 'moving'),
                         ('moving', 'car_noticed', 'stopped'), ('stopped', 'car_passed', 'moving')]
t_intersection_w_speed = [('moving_40', 'car_noticed', 'stopped'), ('stopped', 'car_passed', 'moving_40'),
                          ('moving_40', 'car_noticed', 'stopped'), ('stopped', 'car_passed', 'moving_40')]
straight_car_following = [('moving', 'car_noticed', 'following'), ('following', 'car_stopped', 'stopped')]
fourway_intersection_w_obj = [('moving', 'obstacle_noticed', 'lane_changed')]
fw_intersection_wo_obj = [('moving', 'car_noticed', 'stopped'), ('stopped', 'car_passed', 'moving'),
                          ('moving', 'car_noticed', 'stopped'), ('stopped', 'car_passed', 'moving')]
cds_wo_obj = [('moving', 'car_noticed', 'stopped'), ('stopped', 'car_passed', 'moving'),
              ('moving', 'car_noticed', 'stopped'), ('stopped', 'car_passed', 'moving')]
cul_de_sac_w_parked_car = [('moving', 'car_noticed', 'lane_changed')]
t_intersection_car_following = [('moving', 'car_noticed', 'following'), ('following', 'car_stopped', 'stopped')]
sudden_obstruction = [('moving', 'car_noticed', 'stopped')]


def create_file(scenario, test_case):
    f = open("scenarios/" + scenario + ".py", "w")

    file_contents = """from beamngpy import BeamNGpy, Scenario, Vehicle, StaticObject
import numpy as np

beamng = BeamNGpy('localhost', 64256, home=r'C:\\Deepak\\beamng-research_unlimited\\trunk' )
vehicle = Vehicle('ego', model='etk800', licence='PYTHON', colour='Green')
car = Vehicle('caa', model='coupe', licence='PYTHON')
scenario = Scenario('west_coast_usa', 'ai_sine')
orig = (-140, -121.233, 119.586)
scenario.add_vehicle(vehicle, pos=(-198.5, -164.189, 119.7), rot=(0, 0, -126.25))
scenario.add_vehicle(car, pos=(-140, -121.233, 119.586), rot=(0, 0, 55))
# so = StaticObject('stato', pos=(-140, -121.233, 119.586), rot=(0, 0, 55), scale=(1, 1, 1), shape='/levels/west_coast_usa/art/shapes/objects/barrierfence_folk.dae')
# scenario.add_object(so)
scenario.make(beamng)

script = list()

bng = beamng.open(launch=True)
bng.load_scenario(scenario)

bng.start_scenario()
vehicle.ai_set_mode('span')
vehicle.ai_drive_in_lane(True)
vehicle.ai_set_aggression(0.1)
car.ai_set_line([{'pos': (-198.5, -164.189, 119.7), 'speed': 2000}])

while True:
    bng.step(60)
    """

    f.write(file_contents)
    f.close()


create_file('t_intersection_w_obj', t_intersection_w_obj)
# create_file('t_intersection_w_obj', t_intersection_w_obj)
# create_file('t_intersection_w_obj', t_intersection_w_obj)
# create_file('t_intersection_w_obj', t_intersection_w_obj)
# create_file('t_intersection_w_obj', t_intersection_w_obj)
# create_file('t_intersection_w_obj', t_intersection_w_obj)
# create_file('t_intersection_w_obj', t_intersection_w_obj)

# def detect_static_object():
#     """" Detects the given static object based on the distance """
#     pass
#
# def detect_car():
#     """" Detects the given car based on the distance """
#     pass
#
# def ai_stopped():
#     """" Checks if the AI is at a standstill """
#     pass
#
# def ai_moving(speed=False):
#     """" Checks if the AI is moving """
#     pass
#
# def ai_following():
#     """" Checks if the AI is following a given car """
#     pass
