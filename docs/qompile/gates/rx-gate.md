# RX

![RX gate tile from the Operations catalog](../images/gates/rx-gate.png){ .gate-tile }

**RX** rotates a qubit by an angle \( \theta \) about the X-axis of the Bloch sphere - the natural generalization of the [Pauli-X](pauli-x.md) gate to any rotation angle.

| | |
|---|---|
| **Qubits** | 1 |
| **Parameters** | \( \theta \) - rotation angle, in radians |
| **Inverse** | RX(−θ) |
| **Also called** | X-rotation |

## What it does

RX(θ) smoothly interpolates between doing nothing (θ = 0) and a full X gate (θ = π, up to a global phase). Small angles produce a small amount of superposition; π radians fully flips the qubit.

## Matrix

\[
RX(\theta) = \begin{pmatrix}
\cos(\theta/2) & -i\sin(\theta/2) \\
-i\sin(\theta/2) & \cos(\theta/2)
\end{pmatrix}
\]

## Action on basis states

- \( |0\rangle \rightarrow \cos(\theta/2)\,|0\rangle - i\sin(\theta/2)\,|1\rangle \)
- \( |1\rangle \rightarrow -i\sin(\theta/2)\,|0\rangle + \cos(\theta/2)\,|1\rangle \)

## Example

`RX` with \( \theta = \pi/2 \) on `q[0]` (starting at \( |0\rangle \)) gives an equal superposition, like [H](hadamard.md) does - but with a different relative phase (an \( -i \) on the \( |1\rangle \) term instead of a plain \( + \)).

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `rx(theta) q[0];` |
| Qiskit | `circuit.rx[theta, q[0]]` |
| Cirq | `cirq.rx(theta)(q[0])` |
| Q# | `Rx(theta, q[0]);` |

## Related

- [RY](ry-gate.md)
- [RZ](rz-gate.md)
- [U](u-gate.md) - RX(θ) = U(θ, −π/2, π/2)
