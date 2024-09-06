
import numpy as np

class QMCSampler:
    def __init__(self, num_samples, system_size, potential_function, temperature):
        self.num_samples = num_samples
        self.system_size = system_size
        self.potential_function = potential_function
        self.temperature = temperature
        self.samples = []

    def metropolis_hastings(self, initial_state, step_size=0.1):
        current_state = initial_state
        current_energy = self.potential_function(current_state)
        accepted_samples = []
        
        for _ in range(self.num_samples):
            proposed_state = current_state + np.random.uniform(-step_size, step_size, self.system_size)
            proposed_energy = self.potential_function(proposed_state)
            delta_energy = proposed_energy - current_energy

            if delta_energy < 0 or np.random.rand() < np.exp(-delta_energy / self.temperature):
                current_state = proposed_state
                current_energy = proposed_energy
                accepted_samples.append(current_state)

        self.samples = np.array(accepted_samples)
        return self.samples

    def get_autocorrelation(self, lag=1):
        if len(self.samples) == 0:
            raise ValueError("No samples to calculate autocorrelation.")
        return np.corrcoef(self.samples[:-lag], self.samples[lag:])[0, 1]

    def get_average_energy(self):
        energies = [self.potential_function(sample) for sample in self.samples]
        return np.mean(energies)

    def get_variance(self):
        energies = [self.potential_function(sample) for sample in self.samples]
        return np.var(energies)

def harmonic_potential(state):
    return 0.5 * np.sum(state**2)

if __name__ == "__main__":
    num_samples = 10000
    system_size = 10
    temperature = 1.0
    initial_state = np.random.rand(system_size)
    sampler = QMCSampler(num_samples, system_size, harmonic_potential, temperature)

    samples = sampler.metropolis_hastings(initial_state)
    avg_energy = sampler.get_average_energy()
    variance = sampler.get_variance()
    autocorr = sampler.get_autocorrelation()

    print(f"Average Energy: {avg_energy}")
    print(f"Variance: {variance}")
    print(f"Autocorrelation: {autocorr}")
