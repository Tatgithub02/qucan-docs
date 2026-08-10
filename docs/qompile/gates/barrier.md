# Barrier

![Barrier tile from the Operations catalog](../images/gates/barrier.png){ .gate-tile }

A **barrier** isn't a quantum operation at all - it's a visual/compiler divider that marks a point in the circuit that optimizers shouldn't rearrange gates across.

| | |
|---|---|
| **Qubits** | Any number (applies across the wires it spans) |
| **Parameters** | None |
| **Changes the quantum state?** | No |
| **Also called** | Barrier |

## What it does

Barriers have no effect on the mathematics of a circuit - the statevector, probabilities, and phases are exactly the same with or without one. They exist purely to (a) visually separate stages of a circuit for readability, and (b) tell a compiler or transpiler "don't reorder or merge gates across this line," which matters when gate order affects real hardware behavior even though it doesn't affect the ideal simulated math.

## Example

Placing a barrier after a state-preparation section and before an algorithm's main loop keeps the two visually and logically distinct, without changing any simulation results.

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `barrier q[0], q[1];` |
| Qiskit | `circuit.barrier[q[0], q[1]]` |
| Cirq | - |
| Q# | - |

## Notes

Cirq has no direct equivalent instruction - its `Moment` structure organizes timing differently.

## Related

- [Managing registers](../tour/drag-drop/circuit.md#managing-registers)
