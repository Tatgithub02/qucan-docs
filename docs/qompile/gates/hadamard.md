# Hadamard (H)

![Hadamard gate tile from the Operations catalog](../images/gates/hadamard.png){ .gate-tile }

The **Hadamard gate** is the standard way to create superposition. Applied to \( |0\rangle \), it produces an equal mix of \( |0\rangle \) and \( |1\rangle \) - the starting point of most quantum algorithms.

| | |
|---|---|
| **Qubits** | 1 |
| **Parameters** | None |
| **Inverse** | Itself (H² = I) |
| **Also called** | H gate |

## What it does

H maps each basis state to an equal-weight superposition of both basis states, with a relative sign that depends on which one it started from. Qompile's own gate info panel (opened via the **Info** action described in [Editing, viewing info, and other gate actions](../tour/drag-drop/circuit.md#editing-viewing-info-and-other-gate-actions)) puts it this way:

> The Hadamard gate creates superposition by mapping \( |0\rangle \mapsto |{+}\rangle = \dfrac{1}{\sqrt{2}}(|0\rangle+|1\rangle) \) and \( |1\rangle \mapsto |{-}\rangle = \dfrac{1}{\sqrt{2}}(|0\rangle-|1\rangle) \).

## Matrix

\[
H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}
\]

## Action on basis states

- \( |0\rangle \rightarrow \dfrac{1}{\sqrt{2}}\big(|0\rangle + |1\rangle\big) = |{+}\rangle \)
- \( |1\rangle \rightarrow \dfrac{1}{\sqrt{2}}\big(|0\rangle - |1\rangle\big) = |{-}\rangle \)

## Phase and Bloch-sphere effect

On the Bloch sphere, H swaps the Z-axis and X-axis (with a sign flip) - it's a 180° rotation about the diagonal axis halfway between X and Z. That's why applying H twice returns you to where you started.

## Example

`H` on `q[0]` (starting at \( |0\rangle \)) is the first step of a [Bell state](../algorithms/bell-states.md): once followed by a [CNOT](cnot.md), it produces the entangled state \( (|00\rangle+|11\rangle)/\sqrt{2} \).

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `h q[0];` |
| Qiskit | `circuit.h[q[0]]` |
| Cirq | `cirq.H(q[0])` |
| Q# | `H(q[0]);` |

## Related

- [Bell states](../algorithms/bell-states.md) - H + CNOT, the canonical example
- [CNOT](cnot.md)
- [Phase disks](../tour/visualizations/phase-disks.md) - see phase change after H, S, T
