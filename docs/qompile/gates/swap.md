# SWAP

![SWAP gate tile from the Operations catalog](../images/gates/swap.png){ .gate-tile }

The **SWAP gate** exchanges the states of two qubits - whatever `q[0]` held, `q[1]` now holds, and vice versa.

| | |
|---|---|
| **Qubits** | 2 |
| **Parameters** | None |
| **Inverse** | Itself (SWAP² = I) |
| **Also called** | SWAP |

## What it does

SWAP leaves \( |00\rangle \) and \( |11\rangle \) unchanged (swapping identical values does nothing) and exchanges \( |01\rangle \) and \( |10\rangle \). It works the same way on superpositions and entangled states, not just definite basis states.

## Matrix

\[
\text{SWAP} = \begin{pmatrix}
1&0&0&0\\
0&0&1&0\\
0&1&0&0\\
0&0&0&1
\end{pmatrix}
\]

## Action on basis states

- \( |00\rangle \rightarrow |00\rangle \)
- \( |01\rangle \rightarrow |10\rangle \)
- \( |10\rangle \rightarrow |01\rangle \)
- \( |11\rangle \rightarrow |11\rangle \)

## Example

On the circuit canvas, SWAP is drawn as an **✕** mark on each of the two wires it connects - see [Multi-qubit gate symbols](../tour/drag-drop/circuit.md#multi-qubit-gate-symbols).

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `swap q[0], q[1];` |
| Qiskit | `circuit.swap[q[0], q[1]]` |
| Cirq | `cirq.SWAP(q[0], q[1])` |
| Q# | `SWAP(q[0], q[1]);` |

## Related

- [CNOT](cnot.md)
