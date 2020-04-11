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
import numpy as np

beamng = BeamNGpy('localhost', 64256, home=r'C:\\Deepak\\beamng-research_unlimited\\trunk' )
scenario = Scenario('west_coast_usa', '{scenario}')

vut = Vehicle('vut', model='coupe', licence='VUT', colour='Green')
scenario.add_vehicle(vut, pos=(-198.5, -164.189, 119.7), rot=(0, 0, -126.25))
"""
    # dict_env = environment_setup(test_case)
    # file_contents += dict_env.get('file_content')
    # no_of_cars = dict_env.get('no_of_cars')

    file_contents += """
scenario.make(beamng)
bng = beamng.open(launch=True)
bng.load_scenario(scenario)
bng.start_scenario()

vut.ai_set_mode('span')
vut.ai_drive_in_lane(True)
vut.ai_set_aggression(0.1)

"""

    # file_contents += define_cars_paths(no_of_cars)
    file_contents += fetch_test_case_content(test_case)
    file_contents += """
while True:
    bng.step(60)
    """
    # f.write(file_contents)
    # f.close()


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
car_{i} = Vehicle('caa', model='etk800', licence='CAR {i}')
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
    print('EVENT: ', car_obj, ', CAR SIMILARITY: ', car_sim, ', OBJ SIMILARITY: ', obj_sim)
    return 'car' if car_sim > obj_sim else 'obj'


def environment_setup(test_case):
    lst_events = [e[1] for e in test_case]
    no_of_cars, no_of_objs = 0, 0
    for ev in lst_events:
        if count_cars_objs(ev.split('_')[0]) == 'car':
            no_of_cars += 1
        else:
            no_of_objs += 1

    no_of_cars /= 2  # Quick hack to avoid unnecessary multiplication of cars by 2
    print('CAR COUNT: ', no_of_cars, 'OBJ COUNT: ', no_of_objs)

    return {'file_content': create_objs(no_of_objs) + create_cars(no_of_cars), 'no_of_cars': no_of_cars}

def detect_obstacle(obj):
    """ Checks whether the self-driving car is able to notice the given obstacle based on the distance.
A check is performed if the distance between the self-driving car and the obstacle is within 30 metres."""
    pass

def detect_car(car):
    """ Checks whether the self-driving car is able to notice the given car based on the distance.
A check is performed if the distance between the self-driving car and the given car is within 30 metres. """
    pass


def ai_stopped():
    """ Checks whether the self-driving car came to a halt. """
    pass


def car_passed(car):
    """ Checks whether the given car passed the self-driving car. """
    pass


def ai_moving(speed=False):
    """ Checks whether the self-driving car is moving at a given speed """
    pass


def ai_following(car):
    """ Checks whether the self-driving car is following the given car.
A check is performed if the distance between the self-driving car and the obstacle is within 30 metres."""
    pass

def get_similar_func(event):
    """ Returns the function whose description is most similar to the given event. """
    pos_tagged_e_tup = nltk.pos_tag(event)
    subject = 'Self-driving car'
    [tup[0] for tup in pos_tagged_e_tup if tup[1] == "NN"][0]
    [tup[0] for tup in pos_tagged_e_tup if tup[1] == "NN"][0]

    # pos_tagged_e = dict((pos, e) for e, pos in pos_tagged_e.items())
    # event = pos_tagged_e.get('VBD') + ' ' + pos_tagged_e.get('NN')

    dict_fn_sim = {}
    dict_fn_sim.update({'detect_obstacle': nltk.jaccard_distance(set(event), set(detect_obstacle.__doc__.strip()))})
    dict_fn_sim.update({'detect_car': nltk.jaccard_distance(set(event), set(detect_car.__doc__.strip()))})
    dict_fn_sim.update({'car_passed': nltk.jaccard_distance(set(event), set(car_passed.__doc__.strip()))})
    dict_fn_sim.update({'ai_stopped': nltk.jaccard_distance(set(event), set(ai_stopped.__doc__.strip()))})
    dict_fn_sim.update({'ai_moving': nltk.jaccard_distance(set(event), set(ai_moving.__doc__.strip()))})
    dict_fn_sim.update({'ai_following': nltk.jaccard_distance(set(event), set(ai_following.__doc__.strip()))})
    print(pos_tagged_e, dict_fn_sim)
    return min(dict_fn_sim, key=lambda k: dict_fn_sim[k])


def fetch_test_case_content(test_case):
    """ Generates the script to check if the simulation runs as per the test case. """
    lst_events = [e[1] for e in test_case]
    # lst_fn_docstrs = [detect_obstacle.__doc__.strip(), detect_car.__doc__.strip(), car_passed.__doc__.strip(),
    #                  ai_stopped.__doc__.strip(), ai_moving.__doc__.strip(), ai_following.__doc__.strip()]

    t_intersection_w_obj = [('moving', 'obstacle_noticed', 'moving'), ('moving', 'car_noticed', 'stopped'),
                            ('stopped', 'car_passed', 'moving'), ('moving', 'car_noticed', 'stopped'),
                            ('stopped', 'car_passed', 'moving')]

    i = 0
    while i < len(t_intersection_w_obj):
        # nltk.jaccard_distance(set(' '.join(t_intersection_w_obj[i][1].split('_'))), set(detect_static_object.__doc__.strip()))
        print('Which function? ', ' '.join(t_intersection_w_obj[i][1].split('_')), ': ', get_similar_func(t_intersection_w_obj[i][1].split('_')))
        i += 1

    # print(detect_static_object.__doc__.strip())
    # print(detect_car.__doc__.strip())
    # print(ai_stopped.__doc__.strip())
    # print(ai_moving.__doc__.strip())
    # print(ai_following.__doc__.strip())

    # print(' '.join(t_intersection_w_obj[0][1].split('_')))
    # print(nltk.jaccard_distance(set(' '.join(t_intersection_w_obj[0][1].split('_'))), set(detect_static_object.__doc__.strip())))
    return """"""


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