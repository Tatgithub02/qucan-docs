# Reset

![Reset gate tile from the Operations catalog](../images/gates/reset.png){ .gate-tile }

**Reset** forces a qubit back to \( |0\rangle \), no matter what state it was in - shown in the catalog with the \( |0\rangle \) ket notation.

| | |
|---|---|
| **Qubits** | 1 |
| **Parameters** | None |
| **Reversible?** | No |
| **Also called** | Reset to |0⟩ |

## What it does

Reset discards whatever state a qubit is in - including superposition or entanglement - and reinitializes it to \( |0\rangle \). It's a shortcut for "measure, then flip back to 0 if the result was 1," which is exactly how it's implemented on real hardware.

## Example

Reset is useful for reusing a qubit partway through a circuit - for example, after its role in an intermediate step is finished and you want to use it again from a clean \( |0\rangle \) state.

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `reset q[0];` |
| Qiskit | `circuit.reset[q[0]]` |
| Cirq | `cirq.reset(q[0])` |
| Q# | `Reset(q[0]);` |

## Related

- [Measurement](measurement.md)
