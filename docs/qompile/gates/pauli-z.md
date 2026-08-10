# Pauli-Z

![Z gate tile from the Operations catalog](../images/gates/z-gate.png){ .gate-tile }

The **Pauli-Z gate** leaves \( |0\rangle \) alone and flips the sign of \( |1\rangle \). It's the simplest possible "phase flip."

| | |
|---|---|
| **Qubits** | 1 |
| **Parameters** | None |
| **Inverse** | Itself (Z² = I) |
| **Also called** | Z gate, phase-flip gate; equal to P(π) |

## What it does

Z does nothing visible to a qubit that's definitely \( |0\rangle \) or \( |1\rangle \) - measuring gives the same result either way. Its effect only becomes visible on a superposition, where it flips the *relative phase* between the \( |0\rangle \) and \( |1\rangle \) components by \( \pi \).

## Matrix

\[
Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
\]

## Action on basis states

- \( |0\rangle \rightarrow |0\rangle \)
- \( |1\rangle \rightarrow -|1\rangle \)

## Phase and Bloch-sphere effect

On the Bloch sphere, Z is a 180° rotation about the Z-axis, which passes straight through the poles - so the poles (\( |0\rangle \), \( |1\rangle \)) don't move, but any point on the equator (an equal superposition) rotates halfway around. See [Phase disks](../tour/visualizations/phase-disks.md) for how this shows up visually.

## Example

`H` then `Z` on `q[0]` turns \( |{+}\rangle = (|0\rangle+|1\rangle)/\sqrt{2} \) into \( |{-}\rangle = (|0\rangle-|1\rangle)/\sqrt{2} \) - same measurement probabilities as plain `H`, but a different relative phase.

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `z q[0];` |
| Qiskit | `circuit.z[q[0]]` |
| Cirq | `cirq.Z(q[0])` |
| Q# | `Z(q[0]);` |

## Related

- [S](s-gate.md) and [T](t-gate.md) - smaller phase flips (π/2 and π/4) than Z's π
- [P](p-gate.md) - the general phase gate; Z = P(π)
