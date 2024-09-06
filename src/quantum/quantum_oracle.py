
from qiskit import QuantumCircuit

class QuantumOracle:
    def __init__(self, num_qubits, oracle_function):
        self.num_qubits = num_qubits
        self.oracle_function = oracle_function
        self.circuit = QuantumCircuit(num_qubits)

    def build_oracle(self):
        for index, flip in enumerate(self.oracle_function):
            if flip == 1:
                self.circuit.x(index)
        self.circuit.barrier()

        # Apply the multi-controlled Z gate as the oracle operator
        self.circuit.h(self.num_qubits - 1)
        self.circuit.mcx(list(range(self.num_qubits - 1)), self.num_qubits - 1)
        self.circuit.h(self.num_qubits - 1)
        self.circuit.barrier()

        for index, flip in enumerate(self.oracle_function):
            if flip == 1:
                self.circuit.x(index)

        return self.circuit

if __name__ == "__main__":
    # Define the oracle function (mark the state |101⟩)
    oracle_function = [1, 0, 1]
    num_qubits = 3

    oracle = QuantumOracle(num_qubits, oracle_function)
    oracle_circuit = oracle.build_oracle()
    print(oracle_circuit.draw())
