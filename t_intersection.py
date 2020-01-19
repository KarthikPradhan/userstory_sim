from fysom import *
from beamngpy import BeamNGpy, Scenario, Vehicle, log, StaticObject, Road

"""

"""

events_dict = [
    {'name': 'approach_static_object', 'src': 'moving', 'dst': 'moving'},
    {'name': 'vehicle_1_comes_near', 'src': 'moving', 'dst': 'stopping'},
    {'name': 'vehicle_1_moves_far', 'src': 'stopping', 'dst': 'moving'},
    {'name': 'vehicle_2_comes_near', 'src': 'moving', 'dst': 'stopping'},
    {'name': 'vehicle_2_moves_far', 'src': 'stopping', 'dst': 'moving'},
    {'name': 'vehicle_3_comes_near', 'src': 'moving', 'dst': 'stopping'},
    {'name': 'vehicle_3_moves_far', 'src': 'stopping', 'dst': 'moving'}
]

fsm = Fysom({
    'initial': 'moving',
    'final': 'stopping',
    'events': events_dict
})

lst_events = []
i = 0
while i < len(events_dict):
    lst_events.append(events_dict[i]['name'])
    i = i + 1

print(lst_events)
# fsm.turn_on()
j = 0
lst_transitions = []
while j < len(lst_events):
    eve = lst_events[j] + '()'
    prev_state = fsm.current
    eval('fsm.' + eve)
    lst_transitions.append((prev_state, lst_events[j], fsm.current))
    # getattr(fsm, eve),
    j = j + 1

# print(lst_transitions)

no_of_vehicles = 0
no_of_static_objects = 0
# no. of events
for eve in lst_events:
    # print(eve)
    if 'vehicle' in eve:
        no_of_vehicles += 1
    elif 'object' in eve:
        no_of_static_objects += 1

lst_vehicle_objs = []
for veh in range(no_of_vehicles):
    vehicle = Vehicle('vehicle_' + str(veh), model='etkc', licence='THESIS')
    lst_vehicle_objs.append(vehicle)
    scenario.add_vehicle(vehicle, pos=(-820, 24, 118), rot=(45, 0, 0))

lst_static_objs = []
for stat in range(no_of_static_objects):
    stat_obj = StaticObject(name="statc_object_ai", pos=(0, 0, 0), rot=(45, 0, 0), scale=(0.5, 0.5, 0.5),
                 shape="C://Projects//BeamNG Unlimited//trunk//levels//west_coast_usa//art//shapes//objects//construction_sign_big_a.DAE")
    lst_static_objs.append(stat_obj)
    scenario.add_vehicle(stat_obj)


print(lst_vehicle_objs[0].vid, lst_static_objs)

scenario.add_vehicle(Vehicle('ai_vehicle', model='coupe', licence='THESIS'))
# scenario.make(bng)
#
# # Launch BeamNG.research
# bng.open()
# # Load and start our scenario
# bng.load_scenario(scenario)
# bng.start_scenario()

# conduct tests
print(dir(lst_vehicle_objs[0]))

if lst_static_objs:
    if lst_vehicle_objs[0].vid == 'ai_vehicle':
        print('Hello')

