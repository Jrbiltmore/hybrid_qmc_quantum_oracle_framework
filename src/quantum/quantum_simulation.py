
from qiskit import QuantumCircuit, Aer, execute

class QuantumSimulator:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.circuit = QuantumCircuit(num_qubits)

    def add_gate(self, gate, qubit):
        if gate == 'X':
            self.circuit.x(qubit)
        elif gate == 'H':
            self.circuit.h(qubit)
        elif gate == 'CX':
            if isinstance(qubit, tuple) and len(qubit) == 2:
                self.circuit.cx(qubit[0], qubit[1])
        else:
            raise ValueError("Unsupported gate type.")

    def simulate(self, shots=1024):
        simulator = Aer.get_backend('qasm_simulator')
        self.circuit.measure_all()
        result = execute(self.circuit, simulator, shots=shots).result()
        counts = result.get_counts(self.circuit)
        return counts

    def draw(self):
        return self.circuit.draw()

if __name__ == "__main__":
    num_qubits = 3
    simulator = QuantumSimulator(num_qubits)

    simulator.add_gate('H', 0)
    simulator.add_gate('CX', (0, 1))
    simulator.add_gate('X', 2)

    print(simulator.draw())
    result = simulator.simulate()
    print(f"Simulation result: {result}")
