# S

![S gate tile from the Operations catalog](../images/gates/s-gate.png){ .gate-tile }

The **S gate** leaves \( |0\rangle \) alone and multiplies \( |1\rangle \) by \( i \) - a quarter-turn phase shift. It's also called the **√Z gate**, since applying it twice is the same as one Z gate.

| | |
|---|---|
| **Qubits** | 1 |
| **Parameters** | None |
| **Inverse** | [S†](s-dagger.md) (not self-inverse) |
| **Also called** | √Z, phase gate; equal to P(π/2) |

## What it does

S adds a relative phase of \( \pi/2 \) (90°) between the \( |1\rangle \) and \( |0\rangle \) components of a state, without changing measurement probabilities in the computational basis. \( S^2 = Z \), which is why it's read as "square root of Z."

## Matrix

\[
S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}
\]

## Action on basis states

- \( |0\rangle \rightarrow |0\rangle \)
- \( |1\rangle \rightarrow i\,|1\rangle \)

## Phase and Bloch-sphere effect

S rotates the Bloch vector by \( \pi/2 \) about the Z-axis. On a state that's already a superposition, this is exactly the kind of phase change visualized by [phase disks](../tour/visualizations/phase-disks.md), the [Q-Sphere](../tour/visualizations/q-sphere.md), and the [Statevector](../tour/visualizations/statevector.md) chart - see the worked H → S → T example on the phase disks page.

## Example

`H` then `S` on `q[0]` produces \( \dfrac{1}{\sqrt{2}}(|0\rangle + i|1\rangle) \): the same 50/50 measurement split as plain `H`, but the \( |1\rangle \) bar in the Statevector chart is now colored a quarter-turn around the Phase wheel from the \( |0\rangle \) bar.

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `s q[0];` |
| Qiskit | `circuit.s[q[0]]` |
| Cirq | `cirq.S(q[0])` |
| Q# | `S(q[0]);` |

## Related

- [S†](s-dagger.md) - the inverse of S
- [T](t-gate.md) - a smaller, π/4 phase step
- [P](p-gate.md) - the general phase gate; S = P(π/2)
- [Phase disks](../tour/visualizations/phase-disks.md)
