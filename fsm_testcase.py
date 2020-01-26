from fysom import *

def testcase_gen(fsm_dict):
    events_dict = fsm_dict.get('events')
    fsm = Fysom(fsm_dict)
    lst_events = []
    i = 0
    while i < len(events_dict):
        lst_events.append(events_dict[i]['name'])
        i = i + 1

    # print('List of events: ', lst_events)
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
        # print('Independent FSMs: ', lst_transitions)

    return lst_transitions

