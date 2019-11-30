from Simulation.simulation_config import SimulationConfig


class SimulationStarter:
    def __init__(self, simulation_config: SimulationConfig):
        self.simulation_config = simulation_config

    def run_simulation(self):
        """Run simulation"""