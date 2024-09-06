
from qiskit import QuantumCircuit, Aer, execute

class QuantumMeasurement:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.circuit = QuantumCircuit(num_qubits)

    def add_measurement(self, qubit, classical_bit):
        self.circuit.measure(qubit, classical_bit)

    def measure_all(self):
        self.circuit.measure_all()

    def execute(self, shots=1024):
        simulator = Aer.get_backend('qasm_simulator')
        result = execute(self.circuit, simulator, shots=shots).result()
        counts = result.get_counts(self.circuit)
        return counts

    def draw(self):
        return self.circuit.draw()

if __name__ == "__main__":
    num_qubits = 3
    measurer = QuantumMeasurement(num_qubits)

    measurer.circuit.h(0)  # Apply Hadamard to qubit 0
    measurer.add_measurement(0, 0)  # Measure qubit 0 into classical bit 0

    print(measurer.draw())
    result = measurer.execute()
    print(f"Measurement Result: {result}")
