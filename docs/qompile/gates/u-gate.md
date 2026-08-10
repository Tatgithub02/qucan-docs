# U (general single-qubit gate)

![U gate tile from the Operations catalog](../images/gates/u-gate.png){ .gate-tile }

**U** is the most general possible single-qubit gate - with the right three angles, it can reproduce *any* single-qubit unitary, including every other gate on this page.

| | |
|---|---|
| **Qubits** | 1 |
| **Parameters** | \( \theta, \varphi, \lambda \) - three angles, in radians |
| **Inverse** | U(−θ, −λ, −φ) |
| **Also called** | U3 gate |

## What it does

U(θ, φ, λ) covers every possible way to rotate and phase-shift a single qubit. Every gate on this reference page is a special case of U with particular angles plugged in.

## Matrix

\[
U(\theta, \varphi, \lambda) = \begin{pmatrix}
\cos(\theta/2) & -e^{i\lambda}\sin(\theta/2) \\
e^{i\varphi}\sin(\theta/2) & e^{i(\varphi+\lambda)}\cos(\theta/2)
\end{pmatrix}
\]

## Example

`U` with \( (\theta,\varphi,\lambda) = (\pi/2, 0, \pi) \) on `q[0]` produces exactly the same state as an `H` gate - a good way to see how U generalizes the gates you already know.

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `u(theta, phi, lambda) q[0];` |
| Qiskit | `circuit.u[theta, phi, lam, q[0]]` |
| Cirq | - |
| Q# | - |

## Notes

Some useful special cases (all exact, no leftover global phase):

- \( U(0, 0, \lambda) = P(\lambda) \) - see [P](p-gate.md)
- \( U(\theta, -\pi/2, \pi/2) = RX(\theta) \) - see [RX](rx-gate.md)
- \( U(\theta, 0, 0) = RY(\theta) \) - see [RY](ry-gate.md)
- \( U(\pi, 0, \pi) = X \) - see [Pauli-X](pauli-x.md)
- \( U(\pi/2, 0, \pi) = H \) - see [Hadamard](hadamard.md)

## Related

- [P](p-gate.md)
- [RX](rx-gate.md)
- [RY](ry-gate.md)
- [Hadamard](hadamard.md)
