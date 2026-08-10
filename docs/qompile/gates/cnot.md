# CNOT

![CNOT gate tile from the Operations catalog](../images/gates/cnot.png){ .gate-tile }

**CNOT** ("controlled-NOT") is the most common two-qubit gate: it flips a target qubit, but only when a control qubit is \( |1\rangle \). It's the standard way to create entanglement between two qubits.

| | |
|---|---|
| **Qubits** | 2 (one control, one target) |
| **Parameters** | None |
| **Inverse** | Itself (CNOT² = I) |
| **Also called** | CX, controlled-X |

## What it does

If the control qubit is \( |0\rangle \), CNOT does nothing. If the control is \( |1\rangle \), CNOT applies an [X gate](pauli-x.md) to the target. Applied to a control in superposition, this correlates the two qubits - the essence of entanglement.

## Matrix

\[
\text{CNOT} = \begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&0&1\\
0&0&1&0
\end{pmatrix}
\]

## Action on basis states

(control first, target second)

- \( |00\rangle \rightarrow |00\rangle \)
- \( |01\rangle \rightarrow |01\rangle \)
- \( |10\rangle \rightarrow |11\rangle \)
- \( |11\rangle \rightarrow |10\rangle \)

## Example

On the circuit canvas, CNOT is drawn as a solid dot on the control wire connected by a vertical line to a circled **+** on the target wire - see [Multi-qubit gate symbols](../tour/drag-drop/circuit.md#multi-qubit-gate-symbols). `H` on `q[0]` followed by `CNOT` from `q[0]` to `q[1]` is the standard [Bell state](../algorithms/bell-states.md) circuit:

![Bell state circuit: H on q0, CNOT from q0 to q1](../images/circuit/left-align-cnot.png)

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `cx q[0], q[1];` |
| Qiskit | `circuit.cx[q[0], q[1]]` |
| Cirq | `cirq.CNOT(q[0], q[1])` |
| Q# | `CNOT(q[0], q[1]);` |

## Related

- [Toffoli](toffoli.md) - the three-qubit generalization (two controls)
- [Control](control.md) - add a standalone control point to build custom controlled gates
- [Bell states](../algorithms/bell-states.md)
