# Pauli-X / NOT

![NOT gate tile from the Operations catalog](../images/gates/not.png){ .gate-tile }

The **Pauli-X gate**, shown in Qompile's catalog as **NOT**, is the quantum equivalent of a classical NOT gate - it flips \( |0\rangle \) to \( |1\rangle \) and vice versa.

| | |
|---|---|
| **Qubits** | 1 |
| **Parameters** | None |
| **Inverse** | Itself (X² = I) |
| **Also called** | X gate, bit-flip gate, quantum NOT |

## What it does

X swaps the amplitudes of \( |0\rangle \) and \( |1\rangle \). Applied to a definite state it behaves exactly like a classical bit flip; applied to a superposition it swaps the two amplitudes while leaving their values (and any phase) otherwise intact.

## Matrix

\[
X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
\]

## Action on basis states

- \( |0\rangle \rightarrow |1\rangle \)
- \( |1\rangle \rightarrow |0\rangle \)

## Phase and Bloch-sphere effect

On the Bloch sphere, X is a 180° rotation about the X-axis. It swaps the north and south poles (\( |0\rangle \) and \( |1\rangle \)) and leaves points on the X-axis unmoved.

## Example

Placing `X` on `q[0]` (initially \( |0\rangle \)) prepares \( |1\rangle \) - the [Probabilities](../tour/visualizations/probabilities.md) panel then shows 100% on outcome `1`.

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `x q[0];` |
| Qiskit | `circuit.x[q[0]]` |
| Cirq | `cirq.X(q[0])` |
| Q# | `X(q[0]);` |

## Related

- [Pauli-Y](pauli-y.md)
- [Pauli-Z](pauli-z.md)
- [CNOT](cnot.md) - applies X to a target qubit only when a control qubit is \(|1\rangle\)
