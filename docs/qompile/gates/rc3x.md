# RC3X

![RC3X gate tile from the Operations catalog](../images/gates/rc3x.png){ .gate-tile }

**RC3X** extends [RCCX](rccx.md) to three controls: a cheaper, relative-phase version of a triply-controlled X gate (C3X) on four qubits.

| | |
|---|---|
| **Qubits** | 4 (three controls, one target) |
| **Parameters** | None |
| **Inverse** | Itself, on computational basis inputs |
| **Also called** | Simplified 3-controlled Toffoli |

## What it does

On computational basis states, RC3X flips the target exactly when all three controls are \( |1\rangle \), matching a true C3X (triply-controlled X) gate. Like RCCX, it achieves this more cheaply by allowing relative phases on non-basis-state inputs.

## Action on basis states

(three controls first, target last - identical to C3X on computational basis states)

- \( |1110\rangle \rightarrow |1111\rangle \)
- \( |1111\rangle \rightarrow |1110\rangle \)
- every other computational basis state is left unchanged

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `rc3x q[0], q[1], q[2], q[3];` |
| Qiskit | `circuit.rc3x[q[0], q[1], q[2], q[3]]` |
| Cirq | - |
| Q# | - |

## Notes

Because RC3X needs four qubits, it appears greyed out in the Operations catalog until your circuit has at least four quantum registers - see the note on the [Operations](../tour/drag-drop/operations.md#catalog-view) page.

## Related

- [RCCX](rccx.md)
- [Toffoli](toffoli.md)
