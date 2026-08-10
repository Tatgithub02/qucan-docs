# S†

![S-dagger gate tile from the Operations catalog](../images/gates/s-dagger.png){ .gate-tile }

**S†** ("S-dagger") is the inverse of the [S gate](s-gate.md): it multiplies \( |1\rangle \) by \( -i \) instead of \( +i \), undoing whatever S did.

| | |
|---|---|
| **Qubits** | 1 |
| **Parameters** | None |
| **Inverse** | [S](s-gate.md) |
| **Also called** | S-dagger, adjoint of S; equal to P(−π/2) |

## What it does

S† rotates the relative phase between \( |1\rangle \) and \( |0\rangle \) by \( -\pi/2 \). Applying S followed by S† (in either order) returns a state to exactly where it started.

## Matrix

\[
S^\dagger = \begin{pmatrix} 1 & 0 \\ 0 & -i \end{pmatrix}
\]

## Action on basis states

- \( |0\rangle \rightarrow |0\rangle \)
- \( |1\rangle \rightarrow -i\,|1\rangle \)

## Example

`H`, then `S`, then `S†` on `q[0]` returns exactly to \( |{+}\rangle \), the same state plain `H` alone would give.

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `sdg q[0];` |
| Qiskit | `circuit.sdg[q[0]]` |
| Cirq | `cirq.S(q[0])**-1` |
| Q# | `Adjoint S(q[0]);` |

## Related

- [S](s-gate.md)
- [T†](t-dagger.md)
