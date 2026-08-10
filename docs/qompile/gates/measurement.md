# Measurement

![Measurement gate tile from the Operations catalog](../images/gates/measure.png){ .gate-tile }

**Measurement** reads out a qubit's state as a classical bit - the one operation in a quantum circuit that isn't reversible.

| | |
|---|---|
| **Qubits** | 1 quantum register + 1 classical register |
| **Parameters** | Which classical bit to store the result in |
| **Reversible?** | No |
| **Also called** | Measure |

## What it does

Measurement collapses a qubit's superposition into a definite outcome - \( 0 \) or \( 1 \) - with probability given by the squared magnitude of that basis state's amplitude, and writes the result into a classical bit. Any superposition or entanglement the qubit had is destroyed by this collapse.

## Example

Measuring a qubit prepared with [H](hadamard.md) gives `0` or `1` with 50/50 probability each time you run the circuit - matching the bars shown in [Probabilities](../tour/visualizations/probabilities.md). Every quantum wire also has a plain end-of-wire circle showing the default readout point, whether or not you've placed an explicit measurement - see [Quantum and classical registers](../tour/drag-drop/circuit.md#quantum-and-classical-registers).

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `measure q[0] -> c[0];` |
| Qiskit | `circuit.measure[q[0], c[0]]` |
| Cirq | `cirq.measure(q[0], key='c0')` |
| Q# | `let result = M(q[0]);` |

## Related

- [Reset](reset.md)
- [Conditional (if)](conditional.md) - act on a measurement result
- [Controls and conditionals](controls-and-conditionals.md)
