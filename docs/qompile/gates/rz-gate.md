# RZ

![RZ gate tile from the Operations catalog](../images/gates/rz-gate.png){ .gate-tile }

**RZ** rotates a qubit by an angle \( \theta \) about the Z-axis of the Bloch sphere. It produces the same *relative* phase shift as [P](p-gate.md), but - unlike P - also applies an overall phase, making it a true rotation.

| | |
|---|---|
| **Qubits** | 1 |
| **Parameters** | \( \theta \) - rotation angle, in radians |
| **Inverse** | RZ(−θ) |
| **Also called** | Z-rotation |

## What it does

RZ(θ) multiplies \( |0\rangle \) by \( e^{-i\theta/2} \) and \( |1\rangle \) by \( e^{i\theta/2} \). The *difference* between those two phases is θ - exactly what P(θ) produces - so RZ(θ) and P(θ) affect measurement probabilities identically: \( RZ(\theta) = e^{-i\theta/2}\,P(\theta) \).

## Matrix

\[
RZ(\theta) = \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix}
\]

## Action on basis states

- \( |0\rangle \rightarrow e^{-i\theta/2}\,|0\rangle \)
- \( |1\rangle \rightarrow e^{i\theta/2}\,|1\rangle \)

## Phase and Bloch-sphere effect

Because global phase (a factor applied equally to every amplitude in a state) has no observable effect, RZ(θ) and P(θ) move a qubit's point on the Bloch sphere identically - both are rotations by θ about the Z-axis. The difference only shows up when the qubit is *entangled* with, or has its phase compared against, another qubit that wasn't rotated - since global-phase equivalence only holds per-qubit, not for a shared multi-qubit state.

## Example

`H` then `RZ` with \( \theta = \pi/2 \) on `q[0]` gives the same measurement probabilities as `H` then [S](s-gate.md) - the Probabilities panel is identical either way.

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `rz(theta) q[0];` |
| Qiskit | `circuit.rz[theta, q[0]]` |
| Cirq | `cirq.rz(theta)(q[0])` |
| Q# | `Rz(theta, q[0]);` |

## Related

- [P](p-gate.md) - the relative-phase-only version of this rotation
- [RX](rx-gate.md) and [RY](ry-gate.md) - the other two axis rotations
