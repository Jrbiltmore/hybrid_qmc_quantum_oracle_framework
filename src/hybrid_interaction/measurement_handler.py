
from qiskit import QuantumCircuit, Aer, execute

class MeasurementHandler:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.circuit = QuantumCircuit(num_qubits)

    def apply_measurement(self):
        self.circuit.measure_all()

    def execute_circuit(self, shots=1024):
        simulator = Aer.get_backend('qasm_simulator')
        result = execute(self.circuit, simulator, shots=shots).result()
        counts = result.get_counts(self.circuit)
        return counts

    def process_measurement(self, counts):
        total_shots = sum(counts.values())
        probabilities = {state: count / total_shots for state, count in counts.items()}
        return probabilities

if __name__ == "__main__":
    num_qubits = 3
    handler = MeasurementHandler(num_qubits)

    handler.circuit.h(0)  # Apply Hadamard to qubit 0
    handler.apply_measurement()

    counts = handler.execute_circuit()
    print(f"Raw counts: {counts}")

    probabilities = handler.process_measurement(counts)
    print(f"State probabilities: {probabilities}")
