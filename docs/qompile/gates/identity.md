# Identity (I)

![Identity gate tile from the Operations catalog](../images/gates/identity.png){ .gate-tile }

The **identity gate** does nothing to the qubit's state. It exists so a wire can have an explicit, visible gate - for example to pad a circuit's timing/layout - without changing what the qubit represents.

| | |
|---|---|
| **Qubits** | 1 |
| **Parameters** | None |
| **Inverse** | Itself (I is its own inverse) |
| **Also called** | Identity, No-op |

## What it does

Applying `I` leaves every amplitude exactly as it was. It's a genuine gate in the mathematical sense (a valid 1-qubit unitary), it's simply the unitary that changes nothing.

## Matrix

\[
I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
\]

## Action on basis states

- \( |0\rangle \rightarrow |0\rangle \)
- \( |1\rangle \rightarrow |1\rangle \)

## Example

Placing `I` on `q[0]` leaves its state unchanged - useful mainly for visually marking a time step on a wire, or as a starting point before editing a gate's parameters.

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `id q[0];` |
| Qiskit | `circuit.id[q[0]]` |
| Cirq | `cirq.I(q[0])` |
| Q# | `I(q[0]);` |

## Related

- [Pauli-X / NOT](pauli-x.md) - the gate that flips a qubit
- [Hadamard (H)](hadamard.md) - the gate that creates superposition
