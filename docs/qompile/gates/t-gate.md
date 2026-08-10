# T

![T gate tile from the Operations catalog](../images/gates/t-gate.png){ .gate-tile }

The **T gate** applies a smaller phase shift than S - \( \pi/4 \) (45°) instead of \( \pi/2 \). It's also called the **√S gate**, and is especially important because it's one of the few gates needed to reach *any* quantum computation when combined with H and CNOT.

| | |
|---|---|
| **Qubits** | 1 |
| **Parameters** | None |
| **Inverse** | [T†](t-dagger.md) (not self-inverse) |
| **Also called** | √S, π/8 gate; equal to P(π/4) |

## What it does

T adds a relative phase of \( \pi/4 \) between \( |1\rangle \) and \( |0\rangle \). \( T^2 = S \) and \( T^4 = Z \) - four T gates in a row bring you back to where two S gates (or one Z) would.

## Matrix

\[
T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}
\]

## Action on basis states

- \( |0\rangle \rightarrow |0\rangle \)
- \( |1\rangle \rightarrow e^{i\pi/4}\,|1\rangle \)

## Phase and Bloch-sphere effect

T rotates the Bloch vector by only \( \pi/4 \) about the Z-axis - an eighth of a full turn, and half of what S does. See the worked H → T → S example on the [Phase disks](../tour/visualizations/phase-disks.md) page for how this looks in the app.

## Example

`H` then `T` on `q[0]` gives \( \dfrac{1}{\sqrt{2}}(|0\rangle + e^{i\pi/4}|1\rangle) \): identical measurement odds to plain `H`, with the \( |1\rangle \) component's phase color rotated an eighth of the way around the Phase wheel - half as far as `S` would move it.

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `t q[0];` |
| Qiskit | `circuit.t[q[0]]` |
| Cirq | `cirq.T(q[0])` |
| Q# | `T(q[0]);` |

## Notes

T is not one of the Clifford gates (I, X, Y, Z, H, S, CNOT) - adding it is what makes a gate set "universal," able to approximate any quantum computation. This is why T shows up so often in algorithm resource-counting discussions.

## Related

- [S](s-gate.md) - T² = S
- [T†](t-dagger.md) - the inverse of T
- [Phase disks](../tour/visualizations/phase-disks.md)
