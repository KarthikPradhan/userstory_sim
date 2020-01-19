adverb = 'behind'

is_position = True

code = """
from beamngpy import BeamNGpy, Scenario, Vehicle

bng = BeamNGpy('localhost', 64256, home='E://Uni Projects//BeamNG')
scenario = Scenario('west_coast_usa', 'example')
vehicle = Vehicle('ego_vehicle', model='etk800', licence='PYTHON')
scenario.add_vehicle(vehicle, pos=(-717, 101, 118), rot=(0, 0, 45))

scenario.make(bng)

bng.open()
bng.load_scenario(scenario)
bng.start_scenario()
"""


if is_position:
    code = """vehicle.state[pos] """