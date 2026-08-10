# T†

![T-dagger gate tile from the Operations catalog](../images/gates/t-dagger.png){ .gate-tile }

**T†** ("T-dagger") is the inverse of the [T gate](t-gate.md): a \( -\pi/4 \) phase shift instead of \( +\pi/4 \).

| | |
|---|---|
| **Qubits** | 1 |
| **Parameters** | None |
| **Inverse** | [T](t-gate.md) |
| **Also called** | T-dagger, adjoint of T; equal to P(−π/4) |

## What it does

T† rotates the relative phase between \( |1\rangle \) and \( |0\rangle \) by \( -\pi/4 \), undoing a T gate.

## Matrix

\[
T^\dagger = \begin{pmatrix} 1 & 0 \\ 0 & e^{-i\pi/4} \end{pmatrix}
\]

## Action on basis states

- \( |0\rangle \rightarrow |0\rangle \)
- \( |1\rangle \rightarrow e^{-i\pi/4}\,|1\rangle \)

## Example

Two T† gates in a row are the same as one S† gate; four are the same as one Z gate.

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `tdg q[0];` |
| Qiskit | `circuit.tdg[q[0]]` |
| Cirq | `cirq.T(q[0])**-1` |
| Q# | `Adjoint T(q[0]);` |

## Related

- [T](t-gate.md)
- [S†](s-dagger.md)
