import nltk
from nltk.corpus import wordnet
import spacy

lst_events = ['appears_static_object', 'vehicle_1_comes_near', 'vehicle_1_moves_far', 'vehicle_2_comes_near',
              'vehicle_2_moves_far', 'vehicle_3_comes_near', 'vehicle_3_moves_far']

for adv_pr in lst_events:
    adv_pr_str = nltk.word_tokenize(' '.join(adv_pr.split('_')))
    print(nltk.pos_tag(adv_pr_str))

pos_adv_0 = 'near'
pos_adv_1 = 'far'

# ctrlsyn = wordnet.synset('near.a.01')
# statesyn = wordnet.synset('far.a.01')
# path_sim = ctrlsyn.path_similarity(statesyn)
#
# print(path_sim)

sy1 = wordnet.synsets('long')
sy2 = wordnet.synsets('short')

# for s in sy1:
#     for t in sy2:
#         print("%s\t %s\t :%s" % (s.name,t.name,wordnet.path_similarity(s,t)))

nlp = spacy.load("en_core_web_md")  # make sure to use larger model!
tokens = nlp("close near")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

