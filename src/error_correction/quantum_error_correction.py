
from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Pauli, Operator
from qiskit.providers.aer.noise import depolarizing_error, NoiseModel

class QuantumErrorCorrection:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.circuit = QuantumCircuit(num_qubits)

    def apply_error_correction(self):
        # Apply a simple three-qubit repetition code
        for qubit in range(self.num_qubits):
            self.circuit.cx(qubit, (qubit + 1) % self.num_qubits)
            self.circuit.cx(qubit, (qubit + 2) % self.num_qubits)

    def simulate_with_errors(self, error_probability=0.01, shots=1024):
        noise_model = NoiseModel()
        error = depolarizing_error(error_probability, 1)
        noise_model.add_all_qubit_quantum_error(error, ['cx', 'h', 'x'])
        
        self.circuit.measure_all()

        simulator = Aer.get_backend('qasm_simulator')
        result = execute(self.circuit, simulator, noise_model=noise_model, shots=shots).result()
        return result.get_counts(self.circuit)

    def draw(self):
        return self.circuit.draw()

if __name__ == "__main__":
    num_qubits = 3
    qec = QuantumErrorCorrection(num_qubits)

    qec.apply_error_correction()
    print(qec.draw())

    error_results = qec.simulate_with_errors()
    print(f"Results with errors: {error_results}")
