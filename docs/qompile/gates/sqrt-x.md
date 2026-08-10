# √X

![Square-root-of-X gate tile from the Operations catalog](../images/gates/sqrt-x.png){ .gate-tile }

**√X** ("square root of X") is a gate that, applied twice, is exactly equal to one [Pauli-X](pauli-x.md) gate. It's a common native gate on real quantum hardware.

| | |
|---|---|
| **Qubits** | 1 |
| **Parameters** | None |
| **Inverse** | [√X†](sqrt-x-dagger.md) (not self-inverse) |
| **Also called** | SX gate |

## What it does

√X creates an equal superposition from either basis state, similar to H, but with a different pattern of complex phases. Applying it twice in a row reproduces a full bit-flip: \( (\sqrt{X})^2 = X \).

## Matrix

\[
\sqrt{X} = \frac{1}{2}\begin{pmatrix} 1+i & 1-i \\ 1-i & 1+i \end{pmatrix}
\]

## Action on basis states

- \( |0\rangle \rightarrow \dfrac{1}{2}\big[(1+i)|0\rangle + (1-i)|1\rangle\big] \)
- \( |1\rangle \rightarrow \dfrac{1}{2}\big[(1-i)|0\rangle + (1+i)|1\rangle\big] \)

## Example

Two `√X` gates in a row on `q[0]` (starting at \( |0\rangle \)) land exactly on \( |1\rangle \) - the same result one `X` gate would give in a single step.

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `sx q[0];` |
| Qiskit | `circuit.sx[q[0]]` |
| Cirq | `cirq.X(q[0])**0.5` |
| Q# | - |

## Related

- [√X†](sqrt-x-dagger.md) - the inverse of √X
- [Pauli-X / NOT](pauli-x.md) - (√X)² = X
