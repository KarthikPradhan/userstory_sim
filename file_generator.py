# f = open("generated_scenario.py", "w")
#
# file_contents = """from beamngpy import BeamNGpy, Scenario, Vehicle, log, StaticObject
# bng = BeamNGpy('localhost', 64256, home='C://Projects//BeamNG Unlimited//trunk')
# scenario = Scenario('west_coast_usa', 'example')
# vehicle = Vehicle('tester', model='coupe', licence='PYTHON')
# ai_vehicle = Vehicle('ego_vehicle', model='etkc', licence='PYTHON')
# """
#
# f.write(file_contents)
# f.close()

def detect_static_object():
    """" Detects the given static object based on the distance """
    pass

def detect_car():
    """" Detects the given car based on the distance """
    pass

def ai_stopped():
    """" Checks if the AI is at a standstill """
    pass

def ai_moving(speed=False):
    """" Checks if the AI is moving """
    pass

def ai_following():
    """" Checks if the AI is following a given car """
    pass
