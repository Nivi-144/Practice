import traci
import sumolib
import os
import sys

# Path to SUMO
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare environment variable 'SUMO_HOME'")

# Start SUMO simulation
sumoBinary = "sumo-gui"  # Use "sumo" for command line mode

sumoCmd = [sumoBinary, "-c", "simulation.sumocfg"]

traci.start(sumoCmd)

step = 0

# Run simulation for 1000 steps
while step < 1000:
    traci.simulationStep()

    # Get number of vehicles
    vehicle_ids = traci.vehicle.getIDList()
    print("Step:", step, "Vehicles:", len(vehicle_ids))

    # Example: Change vehicle speed
    for vehicle in vehicle_ids:
        traci.vehicle.setSpeed(vehicle, 10)

    step += 1

traci.close()
