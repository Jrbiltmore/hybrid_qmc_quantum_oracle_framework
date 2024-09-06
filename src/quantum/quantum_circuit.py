
from qiskit import QuantumCircuit, Aer, execute

class QuantumCircuitManager:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.circuit = QuantumCircuit(num_qubits)

    def apply_hadamard(self):
        for qubit in range(self.num_qubits):
            self.circuit.h(qubit)

    def apply_grover_diffusion(self):
        self.circuit.h(range(self.num_qubits))
        self.circuit.x(range(self.num_qubits))
        self.circuit.h(self.num_qubits - 1)
        self.circuit.mcx(list(range(self.num_qubits - 1)), self.num_qubits - 1)
        self.circuit.h(self.num_qubits - 1)
        self.circuit.x(range(self.num_qubits))
        self.circuit.h(range(self.num_qubits))

    def execute_circuit(self, shots=1024):
        simulator = Aer.get_backend('qasm_simulator')
        result = execute(self.circuit, simulator, shots=shots).result()
        counts = result.get_counts(self.circuit)
        return counts

    def measure(self):
        self.circuit.measure_all()

    def draw(self):
        return self.circuit.draw()

if __name__ == "__main__":
    num_qubits = 3
    qc_manager = QuantumCircuitManager(num_qubits)
    
    qc_manager.apply_hadamard()
    qc_manager.apply_grover_diffusion()
    qc_manager.measure()
    
    print(qc_manager.draw())
    result = qc_manager.execute_circuit()
    print(f"Result: {result}")
