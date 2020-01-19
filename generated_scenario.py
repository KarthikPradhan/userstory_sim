from beamngpy import BeamNGpy, Scenario, Vehicle, log, StaticObject
bng = BeamNGpy('localhost', 64256, home='C://Projects//BeamNG Unlimited//trunk')
scenario = Scenario('west_coast_usa', 'example')
vehicle = Vehicle('tester', model='coupe', licence='PYTHON')
ai_vehicle = Vehicle('ego_vehicle', model='etkc', licence='PYTHON')
