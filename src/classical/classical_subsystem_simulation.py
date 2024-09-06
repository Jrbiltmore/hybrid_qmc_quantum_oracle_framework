
import numpy as np

class ClassicalSubsystemSimulator:
    def __init__(self, system_size, interaction_matrix, external_field):
        self.system_size = system_size
        self.interaction_matrix = interaction_matrix
        self.external_field = external_field
        self.state = np.random.choice([-1, 1], size=system_size)

    def energy(self):
        interaction_energy = -0.5 * np.dot(self.state, np.dot(self.interaction_matrix, self.state))
        field_energy = -np.dot(self.external_field, self.state)
        return interaction_energy + field_energy

    def flip_spin(self, index):
        self.state[index] *= -1

    def metropolis_step(self, temperature):
        index = np.random.randint(0, self.system_size)
        current_energy = self.energy()
        self.flip_spin(index)
        new_energy = self.energy()
        delta_energy = new_energy - current_energy

        if delta_energy > 0 and np.random.rand() >= np.exp(-delta_energy / temperature):
            self.flip_spin(index)  # Reject flip

    def simulate(self, num_steps, temperature):
        for _ in range(num_steps):
            self.metropolis_step(temperature)

    def get_state(self):
        return self.state

def generate_interaction_matrix(system_size):
    return np.random.uniform(-1, 1, (system_size, system_size))

def generate_external_field(system_size):
    return np.random.uniform(-1, 1, system_size)

if __name__ == "__main__":
    system_size = 20
    interaction_matrix = generate_interaction_matrix(system_size)
    external_field = generate_external_field(system_size)

    simulator = ClassicalSubsystemSimulator(system_size, interaction_matrix, external_field)

    simulator.simulate(num_steps=10000, temperature=1.0)
    final_state = simulator.get_state()

    print(f"Final State: {final_state}")
    print(f"Final Energy: {simulator.energy()}")
