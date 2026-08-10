# Controls and conditionals

Qompile has two different ways to make an operation depend on something else in the circuit - and it's easy to mix them up, because both are described using the word "control." This page explains the difference, then shows a worked example of each.

## Quantum controls

A **quantum control** makes a gate depend on another *qubit*, while that qubit stays in superposition - nothing is measured, and no information becomes classical. The control qubit and the target stay entangled as part of one combined quantum state.

- [CNOT](cnot.md) and [Toffoli](toffoli.md) are the two built-in controlled gates (one and two controls, both controlling an X).
- The standalone [Control](control.md) tile lets you build a controlled version of *any* gate - not just X - by connecting a control point to another gate on a different wire.

Because the control qubit isn't measured, a quantum control can act on a *superposition* of "control on" and "control off" at the same time - which is exactly how gates like CNOT create entanglement in the first place.

## Classical conditionals

A **classical conditional** - the [if](conditional.md) tile - makes a gate depend on a *classical bit*, almost always one that was just set by a [measurement](measurement.md). Because measurement has already collapsed the superposition into a definite \( 0 \) or \( 1 \) before the conditional gate runs, there's no superposition left in the decision itself - the condition is checked exactly the way an `if` statement in ordinary code would be.

## Comparing the two

| | Quantum control | Classical conditional |
|---|---|---|
| Depends on | A qubit's quantum state | An already-measured classical bit |
| Involves measurement? | No | Yes (upstream of the conditional) |
| Can act on superposition? | Yes | No - the classical bit is always definite |
| Built-in examples | [CNOT](cnot.md), [Toffoli](toffoli.md) | [if](conditional.md) |
| Custom version | [Control](control.md) tile, connected to any gate | [if](conditional.md) tile, wrapping any gate |

## Example: quantum control (no measurement)

`H` on `q[0]`, then `CNOT` from `q[0]` to `q[1]`:

```qasm
OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[2];

h q[0];
cx q[0], q[1];
```

`q[0]` ends up in a superposition of \( |0\rangle \) and \( |1\rangle \), so the CNOT's effect - flip `q[1]` when the control is `1` - happens "for both branches at once," producing the entangled [Bell state](../algorithms/bell-states.md) \( \tfrac{1}{\sqrt{2}}(|00\rangle + |11\rangle) \). Neither qubit has a definite value yet; they're correlated, not decided.

## Example: classical conditional (after measurement)

Measure `q[0]` into `c[0]`, then apply `X` to `q[1]` only if the result was `1`:

```qasm
OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[2];

h q[0];
measure q[0] -> c[0];
if (c[0] == 1) x q[1];
```

This time, `q[0]` is measured *before* the conditional gate runs - so by the time the `if` is evaluated, `c[0]` already holds a definite `0` or `1`, and `q[1]` either gets flipped or doesn't, with no superposition involved in that decision. This pattern - measure, then classically decide what to do next - is exactly what protocols like quantum teleportation rely on for their final correction step.

## See also

- [CNOT](cnot.md), [Toffoli](toffoli.md), [Control](control.md) - the quantum-control gates
- [Conditional (if)](conditional.md) and [Measurement](measurement.md) - the classical side
- [Phase disks](../tour/visualizations/phase-disks.md) - another property (phase) that's easy to confuse across similar-looking gates
