# P (phase)

![P gate tile from the Operations catalog](../images/gates/p-gate.png){ .gate-tile }

The **P gate** is the general-purpose phase gate: pick any angle \( \theta \), and P applies exactly that much relative phase to \( |1\rangle \). Z, S, and T are all just P with a specific angle plugged in.

| | |
|---|---|
| **Qubits** | 1 |
| **Parameters** | \( \theta \) - phase angle, in radians |
| **Inverse** | P(−θ) |
| **Also called** | Phase gate; sometimes written R1 or U1 |

## What it does

P(θ) leaves \( |0\rangle \) completely untouched and multiplies \( |1\rangle \) by \( e^{i\theta} \). Setting \( \theta = \pi/4, \pi/2, \pi \) reproduces T, S, and Z exactly.

## Matrix

\[
P(\theta) = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\theta} \end{pmatrix}
\]

## Action on basis states

- \( |0\rangle \rightarrow |0\rangle \)
- \( |1\rangle \rightarrow e^{i\theta}\,|1\rangle \)

## Phase and Bloch-sphere effect

P(θ) rotates the Bloch vector by θ about the Z-axis - like [RZ](rz-gate.md), but without RZ's extra overall phase factor (see the note on that page for the exact relationship between the two).

## Example

`H` then `P` with \( \theta = \pi/3 \) on `q[0]` gives \( \dfrac{1}{\sqrt{2}}(|0\rangle + e^{i\pi/3}|1\rangle) \) - any angle you like, not just the fixed steps S and T provide.

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `u1(theta) q[0];` |
| Qiskit | `circuit.p[theta, q[0]]` |
| Cirq | `cirq.ZPowGate(exponent=theta / math.pi)(q[0])` |
| Q# | `R1(theta, q[0]);` |

## Related

- [RZ](rz-gate.md) - the same phase step, plus an overall phase factor
- [S](s-gate.md) = P(π/2), [T](t-gate.md) = P(π/4), [Pauli-Z](pauli-z.md) = P(π)
