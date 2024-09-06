
import numpy as np

class ErrorEstimator:
    def __init__(self, samples):
        self.samples = samples

    def mean(self):
        return np.mean(self.samples)

    def variance(self):
        return np.var(self.samples)

    def standard_error(self):
        return np.std(self.samples) / np.sqrt(len(self.samples))

    def confidence_interval(self, confidence_level=0.95):
        sample_mean = self.mean()
        std_err = self.standard_error()
        z_value = self._z_value(confidence_level)
        margin_of_error = z_value * std_err
        return (sample_mean - margin_of_error, sample_mean + margin_of_error)

    def _z_value(self, confidence_level):
        return {
            0.90: 1.645,
            0.95: 1.96,
            0.99: 2.576
        }.get(confidence_level, 1.96)

if __name__ == "__main__":
    # Example usage
    sample_data = np.random.normal(loc=0, scale=1, size=1000)  # Generate normal distribution samples
    estimator = ErrorEstimator(sample_data)
    
    print(f"Mean: {estimator.mean()}")
    print(f"Variance: {estimator.variance()}")
    print(f"Standard Error: {estimator.standard_error()}")
    print(f"95% Confidence Interval: {estimator.confidence_interval()}")
