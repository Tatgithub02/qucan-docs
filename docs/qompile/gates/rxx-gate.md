# RXX

![RXX gate tile from the Operations catalog](../images/gates/rxx-gate.png){ .gate-tile }

**RXX** is a two-qubit "Ising coupling" gate - it entangles two qubits by an amount that depends continuously on an angle \( \theta \), based on the \( X \otimes X \) interaction.

| | |
|---|---|
| **Qubits** | 2 |
| **Parameters** | \( \theta \) - coupling angle, in radians |
| **Inverse** | RXX(−θ) |
| **Also called** | XX-rotation, Ising XX coupling gate |

## What it does

RXX(θ) is defined as \( e^{-i\theta X \otimes X / 2} \). It mixes pairs of basis states that differ in *both* qubits: \( |00\rangle \) with \( |11\rangle \), and \( |01\rangle \) with \( |10\rangle \).

## Matrix

\[
RXX(\theta) = \begin{pmatrix}
\cos(\theta/2) & 0 & 0 & -i\sin(\theta/2) \\
0 & \cos(\theta/2) & -i\sin(\theta/2) & 0 \\
0 & -i\sin(\theta/2) & \cos(\theta/2) & 0 \\
-i\sin(\theta/2) & 0 & 0 & \cos(\theta/2)
\end{pmatrix}
\]

## Action on basis states

- \( |00\rangle \rightarrow \cos(\theta/2)|00\rangle - i\sin(\theta/2)|11\rangle \)
- \( |01\rangle \rightarrow \cos(\theta/2)|01\rangle - i\sin(\theta/2)|10\rangle \)
- \( |10\rangle \rightarrow \cos(\theta/2)|10\rangle - i\sin(\theta/2)|01\rangle \)
- \( |11\rangle \rightarrow \cos(\theta/2)|11\rangle - i\sin(\theta/2)|00\rangle \)

## Example

`RXX` with \( \theta = \pi/2 \) applied to `q[0], q[1]` (both starting at \( |0\rangle \)) produces \( \dfrac{1}{\sqrt{2}}(|00\rangle - i|11\rangle) \) - an entangled state built in a single gate, without a separate [H](hadamard.md) + [CNOT](cnot.md) pair.

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `rxx(theta) q[0], q[1];` |
| Qiskit | `circuit.rxx[theta, q[0], q[1]]` |
| Cirq | `cirq.XXPowGate(exponent=theta / math.pi)(q[0], q[1])` |
| Q# | - |

## Related

- [RZZ](rzz-gate.md) - the equivalent coupling gate built from Z⊗Z
