
class IterationControl:
    def __init__(self, max_iterations, tolerance):
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.current_iteration = 0
        self.prev_value = None

    def has_converged(self, current_value):
        if self.prev_value is None:
            self.prev_value = current_value
            return False

        if abs(current_value - self.prev_value) < self.tolerance:
            return True
        else:
            self.prev_value = current_value
            return False

    def should_continue(self):
        return self.current_iteration < self.max_iterations

    def increment_iteration(self):
        self.current_iteration += 1

if __name__ == "__main__":
    control = IterationControl(max_iterations=100, tolerance=1e-6)
    values = [0.5, 0.49, 0.485, 0.484, 0.4839]  # Simulated result values

    for value in values:
        if control.has_converged(value):
            print(f"Converged after {control.current_iteration} iterations with value: {value}")
            break
        control.increment_iteration()
        if not control.should_continue():
            print("Reached max iterations.")
            break
