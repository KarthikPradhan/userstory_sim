from nltk.corpus import wordnet
# adverb = 'behind'

is_position = True


def create_scenario_file(testcase, name, road_nodes):
    car_synonyms = []
    for syn in wordnet.synsets("car"):
        for l in syn.lemmas():
            car_synonyms.append(l.name())

    sobj_synonyms = []
    for syn in wordnet.synsets("obstacle"):
        for l in syn.lemmas():
            sobj_synonyms.append(l.name())

    f = open(name + ".py", "w")

    file_contents = """
    from beamngpy import BeamNGpy, Scenario, Vehicle
    
    bng = BeamNGpy('localhost', 64256, home='E://Uni Projects//BeamNG')
    scenario = Scenario('GridMap', 'road_test')
    ai = Vehicle('ai_vehicle', model='etk800', licence='PYTHON')
    scenario.add_vehicle(vehicle, pos=(-717, 101, 118), rot=(0, 0, 45))
    """

    car_count = 0
    for el in [tp[1] for tp in testcase]:
        for car in car_synonyms:
            if car in el:
                car_count += 1
                file_contents += "vehicle_" + str(car_count) + " = Vehicle('vehicle_" + car_count + " ', model='etk800', licence='PYTHON')"


    """
    # Detect static object, change lane, and come back to original lane
    
    if ai.state[pos].range() == 
    
    
    # Detect car and stop
    
    
    # Car moves far and the AI moves
    
    
    # Detect car on the same lane as the AI and slows down the AI
    """

    if is_position:
        file_contents = """vehicle.state[pos] """


    """
    scenario.make(bng)
    
    bng.open()
    bng.load_scenario(scenario)
    bng.start_scenario()
    """

    f.write(file_contents)
    f.close()