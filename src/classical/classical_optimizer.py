
import numpy as np
from scipy.optimize import minimize

class ClassicalOptimizer:
    def __init__(self, objective_function, initial_params, method="BFGS", tol=1e-6):
        self.objective_function = objective_function
        self.initial_params = initial_params
        self.method = method
        self.tol = tol
        self.result = None

    def optimize(self):
        self.result = minimize(self.objective_function, self.initial_params, method=self.method, tol=self.tol)
        return self.result

    def get_optimized_params(self):
        if self.result is None:
            raise ValueError("Optimization has not been performed yet.")
        return self.result.x

    def get_optimized_value(self):
        if self.result is None:
            raise ValueError("Optimization has not been performed yet.")
        return self.result.fun

    def has_converged(self):
        if self.result is None:
            raise ValueError("Optimization has not been performed yet.")
        return self.result.success

def example_objective_function(params):
    return np.sum(params**2) + 3 * np.prod(params)

if __name__ == "__main__":
    initial_params = np.random.rand(5)
    optimizer = ClassicalOptimizer(example_objective_function, initial_params)

    result = optimizer.optimize()
    print(f"Optimized Parameters: {optimizer.get_optimized_params()}")
    print(f"Optimized Value: {optimizer.get_optimized_value()}")
    print(f"Has Converged: {optimizer.has_converged()}")
