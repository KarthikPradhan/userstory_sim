"""
.. module:: file_generator
    :synopsis: Generates files from test cases which can be executed to run scenarios and test the same
.. moduleauthor:: Karthik Pradhan
"""

from nltk.corpus import wordnet as wn
import nltk

# Below assignments are the results of the corresponding scenarios
# Uncomment the below assignments to generate the file content
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
    file_contents = f"""from beamngpy import BeamNGpy, Scenario, Vehicle, StaticObject
from beamngpy.sensors import Electrics, Damage
import numpy as np
from time import sleep, time

beamng = BeamNGpy('localhost', 64256, home=r'C:\\BeamNG_unlimited\\trunk')
scenario = Scenario('west_coast_usa', '{scenario}')

vut = Vehicle('vut', model='coupe', licence='VUT', colour='Red')
electrics = Electrics()
damage = Damage()
vut.attach_sensor('electrics', electrics)
vut.attach_sensor('damage', damage)
scenario.add_vehicle(vut, pos=(-198.5, -164.189, 119.7), rot=(0, 0, -126.25))
"""
    dict_env = environment_setup(test_case)
    file_contents += dict_env.get('file_content')
    no_of_cars = dict_env.get('no_of_cars')

    file_contents += """
scenario.make(beamng)
bng = beamng.open(launch=True)
bng.load_scenario(scenario)
bng.start_scenario()

vut.ai_set_mode('span')
vut.ai_drive_in_lane(True)

"""

    file_contents += define_cars_paths(no_of_cars)
    file_contents += """
for _ in range(240):
    sleep(0.1)
    vut.update_vehicle()
    sensors = bng.poll_sensors(vut)
    dmg = sensors['damage']
    """

    file_contents += fetch_test_case_content(test_case)

    f.write(file_contents)
    f.close()


def create_objs(n):
    i = 1
    objs = """"""
    while i <= n:
        objs += f"""
obj_{i} = StaticObject('obj_{i}', pos=(-140, -121.233, 119.586), rot=(0, 0, 55), scale=(1, 1, 1), shape='/levels/west_coast_usa/art/shapes/objects/barrierfence_folk.dae')
scenario.add_object(obj_{i})
"""
        i += 1
    return objs


def create_cars(n):
    i = 1
    cars = """"""
    while i <= n:
        cars += f"""
car_{i} = Vehicle('car_{i}', model='etk800', licence='CAR {i}', colour='Blue')
scenario.add_vehicle(car_{i}, pos=(-140, -121.233, 119.586), rot=(0, 0, 55))
"""
        i += 1
    return cars


def define_cars_paths(no_of_cars):
    i = 1
    cars_env = """"""
    attrs = "{'pos': (-198.5, -164.189, 119.7), 'speed': 2000}"
    while i <= no_of_cars:
        cars_env += f"""car_{i}.ai_set_line([{attrs}])
"""
        i += 1
    return cars_env


def count_cars_objs(car_obj):
    car, obj = wn.synset('car.n.01'), wn.synset('object.n.01')
    car_obj_syn = wn.synset(car_obj + '.n.01')
    car_sim, obj_sim = car.path_similarity(car_obj_syn), obj.path_similarity(car_obj_syn)
    # print('EVENT: ', car_obj, ', CAR SIMILARITY: ', car_sim, ', OBJ SIMILARITY: ', obj_sim)
    return 'car' if car_sim > obj_sim else 'obj'


def environment_setup(test_case):
    lst_events = [e[1] for e in test_case]
    no_of_cars, no_of_objs = 0, 0
    for ev in lst_events:
        if count_cars_objs(ev.split('_')[0]) == 'car':
            no_of_cars += 1
        else:
            no_of_objs += 1

    if no_of_cars > 1:
        no_of_cars /= 2 # A quick hack to avoid unnecessary multiplication of cars by 2
    # print('CAR COUNT: ', no_of_cars, 'OBJ COUNT: ', no_of_objs)

    return {'file_content': create_objs(no_of_objs) + create_cars(no_of_cars), 'no_of_cars': no_of_cars}

def get_state_func_content(dest_state):
    dict_fn_sim = {}
    try:
        dict_fn_sim.update({'ai_stopped': nltk.jaccard_distance(set(dest_state), set(ai_stopped.__doc__.strip()))})
        dict_fn_sim.update({'ai_moving': nltk.jaccard_distance(set(dest_state), set(ai_moving.__doc__.strip()))})
        dict_fn_sim.update({'ai_following': nltk.jaccard_distance(set(dest_state), set(ai_following.__doc__.strip()))})
        dict_fn_sim.update({'ai_lane_changed': nltk.jaccard_distance(set(dest_state), set(ai_lane_changed.__doc__.strip()))})
        # print(dict_fn_sim)
        while list(dict_fn_sim.values()).count(min(dict_fn_sim.values())) > 1:
            del dict_fn_sim[min(dict_fn_sim, key=lambda k: dict_fn_sim[k])] # A quick hack to avoid wrong selection of functions
    except AttributeError:
        print('Please add docstrings to one of the event-matching functions.')
        return ''

    return min(dict_fn_sim, key=lambda k: dict_fn_sim[k])

def detect_obstacle_car(*args):
    """ Checks whether the self-driving car is able to notice the given obstacle or car. """
    # print(args)
    car_or_obj = "[2.91697, -12.596, 119.58]" if args[0] == 'obj' else "{}_{}.state['pos']".format(args[0], args[1])
    car_or_obj_str = 'Obstacle' if args[0] == 'obj' else 'Car'
    # Expects obstacle and iteration count as parameters
    return f"""
    # Below code snippet is generated form 'detect_obstacle_car' function for {args[0]}_{args[1]}
    scenario.update()
    dist_{args[0]}_{args[1]} = np.linalg.norm(np.array(vut.state['pos']) - np.array({car_or_obj}))
    
    if dist_{args[0]}_{args[1]} < 8:
        print('{car_or_obj_str} Detected')
    """


def car_passed(*args):
    """ Checks whether the given car passed the self-driving car. """
    # print(args)
    # Expects car as a parameter
    return f"""
    # Below code snippet is generated form 'car_passed' function for {args[0]}_{args[1]}
    scenario.update()
    dist_{args[0]}_{args[1]}_prev = np.linalg.norm(np.array(vut.state['pos']) - np.array(np.array({args[0]}_{args[1]}.state['pos'])))
    sleep(0.1)
    dist_{args[0]}_{args[1]}_next = np.linalg.norm(np.array(vut.state['pos']) - np.array(np.array({args[0]}_{args[1]}.state['pos'])))

    if dist_{args[0]}_{args[1]}_next > dist_{args[0]}_{args[1]}_prev:
        print('Car Passed')
    """

def car_stopped(*args):
    """ Checks whether the given car stopped. """
    # print(args)
    # Expects car as a parameter
    return f"""
    # Below code snippet is generated form 'car_stopped' function for {args[0]}_{args[1]}
    scenario.update()
    dist_{args[0]}_{args[1]}_prev = np.linalg.norm(np.array(vut.state['pos']) - np.array(np.array({args[0]}_{args[1]}.state['pos'])))
    sleep(0.1)
    dist_{args[0]}_{args[1]}_next = np.linalg.norm(np.array(vut.state['pos']) - np.array(np.array({args[0]}_{args[1]}.state['pos'])))

    if dist_{args[0]}_{args[1]}_next == dist_{args[0]}_{args[1]}_prev:
        print('Car Stopped')
    """


def ai_stopped(*args):
    """ Checks whether the self-driving car is stopped. """
    # print(args)
    return f"""
        # Below code snippet is generated form 'ai_stopped' function for {args[0]}_{args[1]}
        scenario.update()
        if sensors['electrics']['values']['wheelspeed'] == 0 and dmg['damage'] == 0:
            print('[Successful] VUT Stopped')
        else:
            print('[Failed] VUT Moved or Damaged')
    """


def ai_moving(*args):
    """ Checks whether the self-driving car is moving """
    # print(args)
    file_content = f"""
        # Below code snippet is generated form 'ai_moving' function for {args[0]}_{args[1]}
        scenario.update()
        if sensors['electrics']['values']['wheelspeed'] > 0 and dmg['damage'] == 0:
            print('[Successful] VUT is moving')
        else:
            print('[Failed] VUT Stopped or Damaged')
    """
    if args[2] != '0':
        file_content += f""" 
        if sensors['electrics']['values']['wheelspeed'] == {args[2]} and dmg['damage'] == 0:
            print('[Successful] VUT is moving at {args[2]} kmph')
        else:
            print('[Failed] VUT did not move at {args[2]} kmph or it is damaged')
    """
    # Expects speed as the parameter, by default it is set to 0
    return file_content


def ai_following(*args):
    """ Checks whether the self-driving car is following the given car. """
    # print(args)
    # Expects car as a parameter
    return f"""
        # Below code snippet is generated form 'ai_following' function for {args[0]}_{args[1]}
        scenario.update()
        follow_{args[0]}_{args[1]} = np.linalg.norm(np.array(vut.state['dir']) - np.array(np.array({args[0]}_{args[1]}.state['dir'])))
        
        if follow_{args[0]}_{args[1]} < 8 and dmg['damage'] == 0:
            print('[Successful] Car Following Successful')
        else:
            print('[Failed] Car Following Failed or the VUT is damaged')
    """


def ai_lane_changed(*args):
    """ Checks whether the self-driving car changed the current lane. """
    # print(args)
    # Expects car as a parameter
    return f"""
        # Below code snippet is generated form 'ai_lane_changed' function
        scenario.update()
        ct__lane = np.array(vut.state['pos'])
        sleep(0.6)
        moved = np.linalg.norm(np.array(vut.state['pos']) - ct__lane)
    
        if moved >= 3.7 and dmg['damage'] == 0:
            print('[Successful] Lane Changing Successful')
        else:
            print('[Failed] Lane Changing Failed or the VUT is damaged')
    """


def get_event_func_content(event):
    """ Returns the function whose description is most similar to the given event. """
    pos_tagged_e_tup = nltk.pos_tag(event)
    subj = 'Self-driving car'
    dir_obj = [tup[0] for tup in pos_tagged_e_tup if tup[1] == "NN"][0]
    verb = [tup[0] for tup in pos_tagged_e_tup if tup[1] == "VBD"][0]
    indir_obj_lst = [tup[0] for tup in pos_tagged_e_tup if tup[1] == "CD"]
    indir_obj = ' at ' + indir_obj_lst[0]  + 'kmph' if indir_obj_lst else ''
    # 'at' is added because the direct object is always speed in all our scenarios
    # However, this can be improved in the future work to work for other measures, for example, distance, wind speed, etc if the simulator supports
    event = subj + ' ' + verb + ' ' + dir_obj + indir_obj
    dict_fn_sim = {}
    try:
        dict_fn_sim.update({'detect_obstacle_car': nltk.jaccard_distance(set(event), set(detect_obstacle_car.__doc__.strip()))})
        dict_fn_sim.update({'car_passed': nltk.jaccard_distance(set(event), set(car_passed.__doc__.strip()))})
        dict_fn_sim.update({'car_stopped': nltk.jaccard_distance(set(event), set(car_stopped.__doc__.strip()))})
    except AttributeError:
        print('Please add docstrings to one of the event-matching functions.')
        return ''

    return min(dict_fn_sim, key=lambda k: dict_fn_sim[k])


def enumerate_events(events):
    lst_enum_events = []
    for ev in events:
        lst_enum_events.append((ev, events.count(ev)))

    return list(set(lst_enum_events))


def fetch_test_case_content(test_case):
    """ Generates the script to check if the simulation runs as per the test case. """
    testing_content = """"""
    i = 0
    lst_events_set = enumerate_events([tup[1] for tup in test_case])
    # print(lst_events_set)
    while i < len(test_case):
        current_event, current_destination_state = test_case[i][1], test_case[i][2]
        matched_event_func = get_event_func_content(current_event.split('_'))
        matched_state_func = get_state_func_content(current_destination_state)
        # print('Which event function? ', ' '.join(current_event.split('_')), ': ', matched_event_func)
        print('Which state function? ', ' '.join(current_destination_state.split('_')), ': ', matched_state_func)
        speed = current_destination_state.split('_')[1] if any(map(str.isdigit, current_destination_state)) else 0
        param = current_event.split('_')[0]
        car_or_obj = 'obj' if param == 'obstacle' else param # Just to make it fit to the convention used
        # ent_no =  lst_events_set.count(current_event) - 1 if lst_events_set.count(current_event) >= 2  else 1
        ent_no = 0
        for ev_enum in lst_events_set:
            if current_event == ev_enum[0]:
                ent_no = ev_enum[1]
                if ev_enum[1] > 1:
                    lst_events_set.remove(ev_enum)
                    lst_events_set.append((current_event, ev_enum[1] - 1))
                    break

        # print(current_event, current_destination_state, lst_events_set)
        # Parameters for the functions called below: (entity (object or car), entity index, speed, destination state)
        params = "('" + car_or_obj + "', '" + str(ent_no) + "', '" + str(speed) + "')"
        print('Params', params)
        testing_content += eval(matched_event_func + params)
        testing_content += eval(matched_state_func + params)
        i += 1

    return testing_content


# Uncomment the below function calls to generate the file content
create_file('t_intersection_w_obj', t_intersection_w_obj)
# create_file('t_intersection_wo_obj', t_intersection_wo_obj)
# create_file('t_intersection_w_speed', t_intersection_w_speed)
# create_file('straight_car_following', straight_car_following)
# create_file('fourway_intersection_w_obj', fourway_intersection_w_obj)
# create_file('fw_intersection_wo_obj', fw_intersection_wo_obj)
# create_file('cds_wo_obj', cds_wo_obj)
# create_file('cul_de_sac_w_parked_car', cul_de_sac_w_parked_car)
# create_file('t_intersection_car_following', t_intersection_car_following)
# create_file('sudden_obstruction', sudden_obstruction)