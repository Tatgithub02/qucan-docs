# Pauli-Y

![Y gate tile from the Operations catalog](../images/gates/y-gate.png){ .gate-tile }

The **Pauli-Y gate** flips the qubit like X, but also rotates its phase - it's the "bit-and-phase-flip" member of the Pauli family.

| | |
|---|---|
| **Qubits** | 1 |
| **Parameters** | None |
| **Inverse** | Itself (Y² = I) |
| **Also called** | Y gate |

## What it does

Y swaps \( |0\rangle \) and \( |1\rangle \) like X does, but multiplies each resulting amplitude by \( \pm i \). It is equal, up to a global phase, to applying Z and then X (or X then Z, with opposite sign): \( Y = iXZ \).

## Matrix

\[
Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}
\]

## Action on basis states

- \( |0\rangle \rightarrow i\,|1\rangle \)
- \( |1\rangle \rightarrow -i\,|0\rangle \)

## Phase and Bloch-sphere effect

On the Bloch sphere, Y is a 180° rotation about the Y-axis - it swaps the poles like X, but rotates points on the equator in the opposite sense to X.

## Example

Placing `Y` on `q[0]` (initially \( |0\rangle \)) prepares \( i\,|1\rangle \). In the [Statevector](../tour/visualizations/statevector.md) panel, the `1` amplitude has the same magnitude as an X gate would give, but a different phase color.

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `y q[0];` |
| Qiskit | `circuit.y[q[0]]` |
| Cirq | `cirq.Y(q[0])` |
| Q# | `Y(q[0]);` |

## Related

- [Pauli-X / NOT](pauli-x.md)
- [Pauli-Z](pauli-z.md)
