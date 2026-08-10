# Toffoli

![Toffoli gate tile from the Operations catalog](../images/gates/toffoli.png){ .gate-tile }

The **Toffoli gate** is a doubly-controlled NOT: it flips the target qubit only when *both* control qubits are \( |1\rangle \). It's the quantum version of a classical AND gate (the target ends up holding the AND of the two controls, if it started at \( |0\rangle \)).

| | |
|---|---|
| **Qubits** | 3 (two controls, one target) |
| **Parameters** | None |
| **Inverse** | Itself (Toffoli² = I) |
| **Also called** | CCX, CCNOT, doubly-controlled NOT |

## What it does

Toffoli acts as the identity on every basis state except the one where both controls are \( |1\rangle \); there, it flips the target - swapping \( |110\rangle \) with \( |111\rangle \) (using the convention that the first two qubits are the controls and the third is the target). Every other basis state is unchanged.

## Action on basis states

(controls first and second, target third)

- \( |110\rangle \rightarrow |111\rangle \)
- \( |111\rangle \rightarrow |110\rangle \)
- every other 3-qubit basis state is left unchanged

## Example

With `q[0]` and `q[1]` both set to \( |1\rangle \) (e.g. with two [X](pauli-x.md) gates) and `q[2]` at \( |0\rangle \), a Toffoli from controls `q[0], q[1]` to target `q[2]` flips `q[2]` to \( |1\rangle \) - same as classical `AND(1, 1) = 1`.

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `ccx q[0], q[1], q[2];` |
| Qiskit | `circuit.ccx[q[0], q[1], q[2]]` |
| Cirq | `cirq.TOFFOLI(q[0], q[1], q[2])` |
| Q# | `CCNOT(q[0], q[1], q[2]);` |

## Notes

Toffoli's full matrix is 8×8 - identity everywhere except a single 2×2 X block in the corner covering \( |110\rangle \) and \( |111\rangle \), matching the basis-state mapping above.

## Related

- [CNOT](cnot.md) - the single-control version
- [RCCX](rccx.md) - a cheaper, relative-phase version of Toffoli
