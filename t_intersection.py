import fsm_testcase, scenario_creator
from beamngpy import BeamNGpy, Scenario, Vehicle, log, StaticObject, Road

"""
As an AI, the car wants to change the lane when it detects the static object (so that it avoids an accident).
"""

events_dict = [
    {'name': 'approach_static_object', 'src': 'moving', 'dst': 'changing_lane_and_moving'},
    {'name': 'approach_car_1', 'src': 'changing_lane_and_moving', 'dst': 'stopping'},
    {'name': 'approach_car_2', 'src': 'stopping', 'dst': 'stopping'},
    {'name': 'approach_car_3', 'src': 'stopping', 'dst': 'moving'},
    {'name': 'reach_goal', 'src': 'moving', 'dst': 'stopping'},
]

fsm_dict = {
    'initial': 'moving',
    'final': 'stopping',
    'events': events_dict
}

test_case = fsm_testcase.testcase_gen(fsm_dict)
roads +
print('List of events: ', test_case)

scenario_creator = scenario_creator.create_scenario_file(test_case, 't_intersection',)
# no_of_vehicles = 0
# no_of_static_objects = 0
# # no. of events
# for eve in lst_events:
#     # print(eve)
#     if 'vehicle' in eve:
#         no_of_vehicles += 1
#     elif 'object' in eve:
#         no_of_static_objects += 1
#
# lst_vehicle_objs = []
# for veh in range(no_of_vehicles):
#     vehicle = Vehicle('vehicle_' + str(veh), model='etkc', licence='THESIS')
#     lst_vehicle_objs.append(vehicle)
#     scenario.add_vehicle(vehicle, pos=(-820, 24, 118), rot=(45, 0, 0))
#
# lst_static_objs = []
# for stat in range(no_of_static_objects):
#     stat_obj = StaticObject(name="statc_object_ai", pos=(0, 0, 0), rot=(45, 0, 0), scale=(0.5, 0.5, 0.5),
#                  shape="C://Projects//BeamNG Unlimited//trunk//levels//west_coast_usa//art//shapes//objects//construction_sign_big_a.DAE")
#     lst_static_objs.append(stat_obj)
#     scenario.add_vehicle(stat_obj)
#
#
# print(lst_vehicle_objs[0].vid, lst_static_objs)
#
# scenario.add_vehicle(Vehicle('ai_vehicle', model='coupe', licence='THESIS'))
# # scenario.make(bng)
# #
# # # Launch BeamNG.research
# # bng.open()
# # # Load and start our scenario
# # bng.load_scenario(scenario)
# # bng.start_scenario()
#
# # conduct tests
# print(dir(lst_vehicle_objs[0]))
#
# if lst_static_objs:
#     if lst_vehicle_objs[0].vid == 'ai_vehicle':
#         print('Hello')
#
