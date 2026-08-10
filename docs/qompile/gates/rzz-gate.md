# RZZ

![RZZ gate tile from the Operations catalog](../images/gates/rzz-gate.png){ .gate-tile }

**RZZ** is the Z-based counterpart of [RXX](rxx-gate.md): a continuously tunable two-qubit coupling built from the \( Z \otimes Z \) interaction.

| | |
|---|---|
| **Qubits** | 2 |
| **Parameters** | \( \theta \) - coupling angle, in radians |
| **Inverse** | RZZ(−θ) |
| **Also called** | ZZ-rotation, Ising ZZ coupling gate |

## What it does

RZZ(θ) is defined as \( e^{-i\theta Z \otimes Z / 2} \). Unlike RXX, it never mixes basis states into each other - it only ever applies a phase, based on whether the two qubits agree (\( |00\rangle, |11\rangle \)) or disagree (\( |01\rangle, |10\rangle \)).

## Matrix

\[
RZZ(\theta) = \mathrm{diag}\left(e^{-i\theta/2},\ e^{i\theta/2},\ e^{i\theta/2},\ e^{-i\theta/2}\right)
\]

## Action on basis states

- \( |00\rangle \rightarrow e^{-i\theta/2}\,|00\rangle \)
- \( |01\rangle \rightarrow e^{i\theta/2}\,|01\rangle \)
- \( |10\rangle \rightarrow e^{i\theta/2}\,|10\rangle \)
- \( |11\rangle \rightarrow e^{-i\theta/2}\,|11\rangle \)

## Example

Applying `RZZ` to two qubits already in superposition adds a phase that depends on whether the two qubits' bits match - a building block for algorithms like [QAOA](../algorithms/qaoa.md) that encode a cost function into phases.

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `rzz(theta) q[0], q[1];` |
| Qiskit | `circuit.rzz[theta, q[0], q[1]]` |
| Cirq | `cirq.ZZPowGate(exponent=theta / math.pi)(q[0], q[1])` |
| Q# | - |

## Related

- [RXX](rxx-gate.md)
- [QAOA](../algorithms/qaoa.md)
