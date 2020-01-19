from fysom import *

# events_dict = [
#     {'name': 'come_in_front_of_the_AI', 'src': 'moving', 'dst': 'stopping'},
#     {'name': 'moves_far', 'src': 'stopping', 'dst': 'moving'}
# ]

events_dict = [
    {'name': 'come_in_front_of_the_AI', 'src': 'moving', 'dst': 'stopping'},
    {'name': 'moves_far', 'src': 'stopping', 'dst': 'moving'}
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

# print(lst_events)
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

print(lst_transitions)