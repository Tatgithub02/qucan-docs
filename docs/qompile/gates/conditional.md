# Conditional (if)

![If conditional tile from the Operations catalog](../images/gates/if-conditional.png){ .gate-tile }

The **if** tile applies an operation only when a classical condition is true - the bridge between a measurement result and later quantum operations, based on classical, not quantum, control.

| | |
|---|---|
| **Qubits** | Depends on the operation it wraps |
| **Parameters** | A classical register/bit and the value to compare against |
| **Category** | Classical control flow, not a quantum gate |
| **Also called** | Classically-controlled gate, `c_if` |

## What it does

A conditional operation checks the current value of a classical bit (usually set by an earlier [measurement](measurement.md)) and only applies its attached gate when that value matches the condition. Unlike [Control](control.md) - which conditions a gate on a *qubit's* quantum state without collapsing it - a conditional checks an already-measured, classical value, so there's no superposition involved in the decision itself.

## Example

Measure `q[0]` into `c[0]`, then apply `X` to `q[1]` conditioned on `c[0] == 1`: whatever definite value the measurement produced classically decides whether the `X` runs. This pattern shows up in protocols like quantum teleportation, where a receiver's correction gates depend on a sender's measurement outcomes.

## Other notations

Naming conventions across ecosystems; exact syntax can vary by library version, and this does not claim to be Qompile's generated output unless otherwise noted.

| Language | Typical form |
|---|---|
| OpenQASM 2.0 | `if (c[0] == 1) x q[1];` |
| Qiskit | `circuit.x[q[1]].c_if[c, 1]` |
| Cirq | `cirq.X(q[1]).with_classical_controls('c0')` |
| Q# | `if (M(q[0]) == One) { X(q[1]); }` |

## Related

- [Measurement](measurement.md)
- [Control](control.md) - the quantum-conditioned counterpart
- [Controls and conditionals](controls-and-conditionals.md)
