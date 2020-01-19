from beamngpy import BeamNGpy, Scenario, Vehicle, log, StaticObject
import socket

# Instantiate BeamNGpy instance running the simulator from the given path,
# communicating over localhost:64256
bng = BeamNGpy('localhost', 64256, home='C://Projects//BeamNG Unlimited//trunk')
# Create a scenario in west_coast_usa called 'example'
scenario = Scenario('west_coast_usa', 'example')
# Create an ETK800 with the licence plate 'PYTHON'
vehicle = Vehicle('tester', model='coupe', licence='PYTHON')
ai_vehicle = Vehicle('ego_vehicle', model='etkc', licence='PYTHON')
wood_obj = Vehicle('wood_obj', model='woodplanks')
# Add it to our scenario at this position and rotation
scenario.add_vehicle(vehicle, pos=(-820, 24, 118), rot=(45, 0, 0))
scenario.add_vehicle(ai_vehicle, pos=(-880, -69, 114), rot=(0, 45, 0))
scenario.add_vehicle(wood_obj, pos=(-732, 92, 118), rot=(45, 0, 0))
# Place files defining our scenario for the simulator to read

# target_for_ai = StaticObject(name="target_for_ai", pos=(-732, 92, 118), rot=(45, 0, 0), scale=(0.5, 0.5, 0.5),
# shape="C://Projects//BeamNG Unlimited//trunk//levels//west_coast_usa//art//shapes//objects//construction_sign_big_a.DAE")
# scenario.add_object(target_for_ai)
scenario.make(bng)

# Launch BeamNG.research
bng.open()
# Load and start our scenario
bng.load_scenario(scenario)
bng.start_scenario()
# skt = bng.start_server()
# Make the vehicle's AI span the map
# vehicle.ai_set_mode('span')
# vehicle.connect(bng, skt.host, skt.port)
# ai_vehicle.connect(bng, skt.host, skt.port)


# ai_vehicle.ai_set_target(target=str(vehicle.vid))
ai_vehicle.ai_set_mode('manual')
ai_vehicle.ai_set_target(target=str(wood_obj.vid))

# print(ai_vehicle.options)

log.debug("State of the vehicle: " + str(ai_vehicle.state))


if int(vehicle.state['pos'][0]) in range(int(ai_vehicle.state['pos'][0]), int(ai_vehicle.state['pos'][0]) + 10):
    print('Good!sfgshjkssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss')
    # ai_vehicle.state[0] = -700
    ai_vehicle.ai_set_mode('stopping')
    log.debug('Super!')

# vehicle.update_vehicle()
# scenario.update()