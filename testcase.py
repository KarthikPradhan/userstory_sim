from fysom import *
from nltk.corpus import wordnet
from nltk import word_tokenize
import nltk

def testcase_gen(states_events_lst, fsm):
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

def t_interesction_w_obj():
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

    return testcase_gen(states_events_lst, fsm)

def t4w_interesction_wo_obj():
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

    return testcase_gen(states_events_lst, fsm)

def t_interesction_w_speed():
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

    return testcase_gen(states_events_lst, fsm)

def car_following():
    states_events_lst = [
        {'name': 'car_noticed', 'src': 'moving', 'dst': 'decelerating'},
        {'name': 'car_stopped', 'src': 'decelerating', 'dst': 'stopped'}
    ]

    fsm = Fysom({
        'initial': 'moving',
        'final': 'stopped',
        'events': states_events_lst
    })

    return testcase_gen(states_events_lst, fsm)

def fourway_interesction_w_obj():
    states_events_lst = [
        {'name': 'obstacle_noticed', 'src': 'moving', 'dst': 'lane_changed'},
    ]

    fsm = Fysom({
        'initial': 'moving',
        'final': 'lane_changed',
        'events': states_events_lst
    })

    return testcase_gen(states_events_lst, fsm)

print('[Scenario 1] T-Intersection with a Static Object: %s' % t_interesction_w_obj())
print('[Scenario 2] T-Intersection without a Static Object: %s' % t4w_interesction_wo_obj())
print('[Scenario 3] T-Intersection without a Static Object: %s' % t_interesction_w_speed())
print('[Scenario 4] Car Following: %s' % car_following())
print('[Scenario 5] Lane Changing: %s' % fourway_interesction_w_obj())
print('[Scenario 6] Fourway Intersection without a Static Object: %s' % t4w_interesction_wo_obj())