# RCCX

![RCCX gate tile from the Operations catalog](../images/gates/rccx.png){ .gate-tile }

**RCCX** ("relative-phase CCX", also called the Margolus gate) gives the same computational-basis result as a [Toffoli](toffoli.md) gate, but can be built from fewer elementary gates - at the cost of introducing extra phases on some inputs.

| | |
|---|---|
| **Qubits** | 3 (two controls, one target) |
| **Parameters** | None |
| **Inverse** | Itself, on computational basis inputs |
| **Also called** | Margolus gate, simplified Toffoli |

## What it does

On every computational basis state, RCCX flips the target exactly when both controls are \( |1\rangle \) - identical to Toffoli's action. The difference is *not* visible in the basis-state mapping: RCCX implements this using a cheaper sequence of gates by allowing a relative phase to appear on some intermediate/superposition inputs, which Toffoli does not introduce.

## Action on basis states

(controls first and second, target third - identical to Toffoli on computational basis states)

- \( |110\rangle \rightarrow |111\rangle \)
- \( |111\rangle \rightarrow |110\rangle \)
- every other computational basis state is left unchanged

## Example

RCCX is most useful as a cheaper building block inside larger circuits - e.g. constructing [RC3X](rc3x.md) or other multi-controlled gates - where its relative-phase caveat doesn't matter because it's immediately uncomputed or only ever touches basis states.

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `rccx q[0], q[1], q[2];` |
| Qiskit | `circuit.rccx[q[0], q[1], q[2]]` |
| Cirq | - |
| Q# | - |

## Notes

Because RCCX only *matches* Toffoli on computational basis states - not as an exactly identical unitary - it's safe to use as a drop-in replacement when its inputs and outputs are always basis states (e.g. classical logic built from quantum gates), but it should not be substituted for a true Toffoli inside a larger circuit where the extra relative phase would affect interference between amplitudes.

## Related

- [Toffoli](toffoli.md) - the exact (more expensive) version
- [RC3X](rc3x.md) - the four-qubit counterpart
