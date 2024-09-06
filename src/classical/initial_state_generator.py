
import numpy as np

class InitialStateGenerator:
    def __init__(self, system_size, distribution='uniform', params=None):
        self.system_size = system_size
        self.distribution = distribution
        self.params = params if params else {}

    def generate(self):
        if self.distribution == 'uniform':
            return np.random.uniform(low=self.params.get('low', -1), high=self.params.get('high', 1), size=self.system_size)
        elif self.distribution == 'normal':
            return np.random.normal(loc=self.params.get('mean', 0), scale=self.params.get('stddev', 1), size=self.system_size)
        elif self.distribution == 'binary':
            return np.random.choice([0, 1], size=self.system_size)
        else:
            raise ValueError(f"Unsupported distribution type: {self.distribution}")

if __name__ == "__main__":
    generator_uniform = InitialStateGenerator(system_size=10, distribution='uniform')
    initial_state_uniform = generator_uniform.generate()
    print(f"Uniform Distribution Initial State: {initial_state_uniform}")

    generator_normal = InitialStateGenerator(system_size=10, distribution='normal', params={'mean': 0, 'stddev': 0.1})
    initial_state_normal = generator_normal.generate()
    print(f"Normal Distribution Initial State: {initial_state_normal}")

    generator_binary = InitialStateGenerator(system_size=10, distribution='binary')
    initial_state_binary = generator_binary.generate()
    print(f"Binary Distribution Initial State: {initial_state_binary}")
