from fysom import *
from nltk.corpus import wordnet
from nltk import word_tokenize
import nltk

events_dict = [
    {'name': 'turn_on', 'src': 'stopped', 'dst': 'moving'},
    {'name': 'apply_brake', 'src': 'moving', 'dst': 'deaccelerating'},
    {'name': 'turn_off', 'src': 'deaccelerating', 'dst': 'stopped'},
    {'name': 'turn_off', 'src': 'moving', 'dst': 'stopped'}
]

fsm = Fysom({
    'initial': 'stopped',
    'final': 'stopped',
    'events': events_dict
})

# lst_events = []
# i = 0
# while i < len(events_dict):
#     lst_events.append(events_dict[i]['name'])
#     i = i + 1
#
# print(lst_events)
# # fsm.turn_on()
# j = 0
# lst_transitions = []
# while j < len(lst_events):
#     eve = lst_events[j] + '()'
#     prev_state = fsm.current
#     eval('fsm.' + eve)
#     lst_transitions.append((prev_state, lst_events[j], fsm.current))
#     # getattr(fsm, eve),
#     j = j + 1
#
# print(lst_transitions)

lst_ex = [
    [('stopped', 'turn_on', 'moving'), ('moving', 'turn_off', 'stopped')],
    [('stopped', 'turn_on', 'moving'), ('moving', 'apply_brake', 'deaccelerate'), ('deaccelerate', 'turn_off', 'stopped')]
]


# for x in lst_ex:
#     print(x)

control = ['accelerate', 'steer', 'brake']
list_of_states = ['stop', 'move', 'accelerate']
list_of_events = ['come in front of', 'move away', 'apply brake']

# for dict in events_dict:
    # print(dict)
# ctrl_dict = dict()
#
# for ctrl in control:
#     high_sim = 0
#     high_sim_match = ""
#     for state in list_of_states:
#         # syns = wordnet.synsets(state, pos=wordnet.VERB)
#         # syns2 = wordnet.synsets(ctrl, pos=wordnet.VERB)
#         # print(syns, syns2)
#         # for syn in syns:
#         #     for syn2 in syns2:
#         #         print(syn, syn2)
#         #         print(syn.path_similarity(syn2))
#         ctrlsyn = wordnet.synset(ctrl + '.v.01')
#         statesyn = wordnet.synset(state + '.v.01')
#         path_sim = ctrlsyn.path_similarity(statesyn)
#         ctrl_dict[statesyn] = path_sim
#
#     for sim in ctrl_dict:
#         if high_sim < ctrl_dict[sim]:
#             high_sim = ctrl_dict[sim]
#             high_sim_match = sim
#
#     print(ctrl, high_sim_match)
#
#
#
#
#         # print(state, ctrl)
#         # print(syns)
#         # print('\n')
#
# print(ctrl_dict)
# compound_preps = list()
# for eve in list_of_events:
#     for word, tag in nltk.pos_tag(word_tokenize(eve)):
#         if tag in ('VBN', 'VB', 'RB'):
#             compound_preps.append(eve.replace(word + ' ', ''))
#
# print(compound_preps)

ctrlsyn = wordnet.synset('break.v.01')
statesyn = wordnet.synset('throttle.v.01')
# statesyn = wordnet.synset('throttle.v.01')
path_sim = ctrlsyn.wup_similarity(statesyn)
path_sim1 = ctrlsyn.wup_similarity(statesyn)
# path_sim2 = ctrlsyn.res_similarity(statesyn)
print('Path')
print(path_sim, path_sim1)
# print(wordnet.synsets('ahead'))
