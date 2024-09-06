
import numpy as np

class ClassicalErrorMitigation:
    def __init__(self, data):
        self.data = data

    def moving_average(self, window_size=3):
        return np.convolve(self.data, np.ones(window_size)/window_size, mode='valid')

    def polynomial_fitting(self, degree=2):
        x = np.arange(len(self.data))
        poly_coefficients = np.polyfit(x, self.data, degree)
        poly_fit = np.polyval(poly_coefficients, x)
        return poly_fit

    def outlier_removal(self, threshold=1.5):
        q1 = np.percentile(self.data, 25)
        q3 = np.percentile(self.data, 75)
        iqr = q3 - q1
        lower_bound = q1 - threshold * iqr
        upper_bound = q3 + threshold * iqr
        return [x for x in self.data if lower_bound <= x <= upper_bound]

if __name__ == "__main__":
    # Simulated noisy data
    noisy_data = np.array([1, 2, 2, 4, 100, 3, 2, 5, 1, 6])

    mitigator = ClassicalErrorMitigation(noisy_data)

    print("Original Data:", noisy_data)
    print("Moving Average:", mitigator.moving_average(window_size=3))
    print("Polynomial Fit:", mitigator.polynomial_fitting(degree=2))
    print("Outlier Removal:", mitigator.outlier_removal())
