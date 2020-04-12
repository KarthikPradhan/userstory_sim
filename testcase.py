from fysom import *
from file_generator import create_file

def test_case_gen(states_events_lst, fsm):
    """ Generates all possible test cases for a given Finite State Machine (FSM) """
    lst_events = []
    i = 0
    while i < len(states_events_lst):
        lst_events.append(states_events_lst[i]['name'])
        i = i + 1

    j = 0
    lst_transitions = []
    while j < len(lst_events):
        eve = lst_events[j] + '()'
        prev_state = fsm.current

        # Below code generates all the test case except for the final one
        # lst_test_case = []
        # if fsm.current == fsm._final:
        #     lst_test_case = lst_transitions.copy()
        #     lst_test_case.append((prev_state, lst_events[j], fsm.current))
        #     print('Test cases: %s' % lst_test_case)

        try:
            eval('fsm.' + eve)
            lst_transitions.append((prev_state, lst_events[j], fsm.current))
            j = j + 1
        except FysomError:
            break

    return lst_transitions

def t_intersection_w_obj():
    states_events_lst = [
        {'name': 'obstacle_noticed', 'src': 'moving', 'dst': 'moving'},
        {'name': 'car_noticed', 'src': 'moving', 'dst': 'stopped'},
        {'name': 'car_passed', 'src': 'stopped', 'dst': 'moving'},
        {'name': 'car_noticed', 'src': 'moving', 'dst': 'stopped'},
        {'name': 'car_passed', 'src': 'stopped', 'dst': 'moving'}
    ]

    fsm = Fysom({
        'initial': 'moving',
        'final': 'moving',
        'events': states_events_lst
    })

    return test_case_gen(states_events_lst, fsm)

def t4wcds_intersection_wo_obj():
    states_events_lst = [
        {'name': 'car_noticed', 'src': 'moving', 'dst': 'stopped'},
        {'name': 'car_passed', 'src': 'stopped', 'dst': 'moving'},
        {'name': 'car_noticed', 'src': 'moving', 'dst': 'stopped'},
        {'name': 'car_passed', 'src': 'stopped', 'dst': 'moving'}
    ]

    fsm = Fysom({
        'initial': 'moving',
        'final': 'moving',
        'events': states_events_lst
    })

    return test_case_gen(states_events_lst, fsm)

def t_intersection_w_speed():
    states_events_lst = [
        {'name': 'car_noticed', 'src': 'moving_40', 'dst': 'stopped'},
        {'name': 'car_passed', 'src': 'stopped', 'dst': 'moving_40'},
        {'name': 'car_noticed', 'src': 'moving_40', 'dst': 'stopped'},
        {'name': 'car_passed', 'src': 'stopped', 'dst': 'moving_40'}
    ]

    fsm = Fysom({
        'initial': 'moving_40',
        'final': 'moving_40',
        'events': states_events_lst
    })

    return test_case_gen(states_events_lst, fsm)

def car_following():
    states_events_lst = [
        {'name': 'car_noticed', 'src': 'moving', 'dst': 'following'},
        {'name': 'car_stopped', 'src': 'following', 'dst': 'stopped'}
    ]

    fsm = Fysom({
        'initial': 'moving',
        'final': 'stopped',
        'events': states_events_lst
    })

    return test_case_gen(states_events_lst, fsm)

def fourway_intersection_w_obj():
    states_events_lst = [
        {'name': 'obstacle_noticed', 'src': 'moving', 'dst': 'lane_changed'},
    ]

    fsm = Fysom({
        'initial': 'moving',
        'final': 'lane_changed',
        'events': states_events_lst
    })

    return test_case_gen(states_events_lst, fsm)

def cul_de_sac_w_parked_car():
    states_events_lst = [
        {'name': 'car_noticed', 'src': 'moving', 'dst': 'lane_changed'},
    ]

    fsm = Fysom({
        'initial': 'moving',
        'final': 'lane_changed',
        'events': states_events_lst
    })

    return test_case_gen(states_events_lst, fsm)

def sudden_obstruction():
    states_events_lst = [
        {'name': 'car_noticed', 'src': 'moving', 'dst': 'stopped'},
    ]

    fsm = Fysom({
        'initial': 'moving',
        'final': 'stopped',
        'events': states_events_lst
    })

    return test_case_gen(states_events_lst, fsm)

# Uncomment the following code to print the test cases
# print('[Scenario 1] T-Intersection with a Static Object: %s' % t_intersection_w_obj())
# print('[Scenario 2] T-Intersection without a Static Object: %s' % t4wcds_intersection_wo_obj())
# print('[Scenario 3] T-Intersection without a Static Object: %s' % t_intersection_w_speed())
# print('[Scenario 4] Straight Road - Car Following: %s' % car_following())
# print('[Scenario 5] Lane Changing: %s' % fourway_intersection_w_obj())
# print('[Scenario 6] Fourway Intersection without a Static Object: %s' % t4wcds_intersection_wo_obj())
# print('[Scenario 7] Cul-de-sac with a moving car: %s' % t4wcds_intersection_wo_obj())
# print('[Scenario 8] Cul-de-sac with a parked car: %s' % cul_de_sac_w_parked_car())
# print('[Scenario 9] T-Intersection - Car Following: %s' % car_following())
# print('[Scenario 10] Straight Road - Sudden Obstruction: %s' % sudden_obstruction())

create_file('t_intersection_w_obj', t_intersection_w_obj())
create_file('t_intersection_wo_obj', t4wcds_intersection_wo_obj())
create_file('t_intersection_w_speed', t_intersection_w_speed())
create_file('straight_car_following', car_following())
create_file('fourway_intersection_w_obj', fourway_intersection_w_obj())
create_file('fw_intersection_wo_obj', t4wcds_intersection_wo_obj())
create_file('cds_wo_obj', t4wcds_intersection_wo_obj())
create_file('cul_de_sac_w_parked_car', cul_de_sac_w_parked_car())
create_file('t_intersection_car_following', car_following())
create_file('sudden_obstruction', sudden_obstruction())