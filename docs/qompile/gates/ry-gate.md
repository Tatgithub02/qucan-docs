# RY

![RY gate tile from the Operations catalog](../images/gates/ry-gate.png){ .gate-tile }

**RY** rotates a qubit by an angle \( \theta \) about the Y-axis of the Bloch sphere. Unlike RX and RZ, its matrix entries are all real numbers, which makes it a common choice for building superpositions with adjustable probabilities.

| | |
|---|---|
| **Qubits** | 1 |
| **Parameters** | \( \theta \) - rotation angle, in radians |
| **Inverse** | RY(−θ) |
| **Also called** | Y-rotation |

## What it does

RY(θ) turns \( |0\rangle \) into a superposition weighted by \( \cos(\theta/2) \) and \( \sin(\theta/2) \), with no complex phase at all - useful whenever you want to dial in a specific measurement probability directly.

## Matrix

\[
RY(\theta) = \begin{pmatrix}
\cos(\theta/2) & -\sin(\theta/2) \\
\sin(\theta/2) & \cos(\theta/2)
\end{pmatrix}
\]

## Action on basis states

- \( |0\rangle \rightarrow \cos(\theta/2)\,|0\rangle + \sin(\theta/2)\,|1\rangle \)
- \( |1\rangle \rightarrow -\sin(\theta/2)\,|0\rangle + \cos(\theta/2)\,|1\rangle \)

## Example

`RY` with \( \theta = \pi/3 \) on `q[0]` (starting at \( |0\rangle \)) gives \( \cos(\pi/6)|0\rangle + \sin(\pi/6)|1\rangle \), which the [Probabilities](../tour/visualizations/probabilities.md) panel shows as a 75%/25% split.

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `ry(theta) q[0];` |
| Qiskit | `circuit.ry[theta, q[0]]` |
| Cirq | `cirq.ry(theta)(q[0])` |
| Q# | `Ry(theta, q[0]);` |

## Related

- [RX](rx-gate.md)
- [RZ](rz-gate.md)
- [U](u-gate.md) - RY(θ) = U(θ, 0, 0)
