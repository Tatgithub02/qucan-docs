# Phase disk marker

![Phase disk marker tool tile from the Operations catalog](../images/gates/phase-disk-icon.png){ .gate-tile }

The **phase disk** tile isn't a gate either - it's a visualization tool. Clicking it inserts a snapshot marker on the circuit that displays each qubit's phase at that exact point.

| | |
|---|---|
| **Qubits** | All qubits at the chosen point in the circuit |
| **Parameters** | None |
| **Changes the quantum state?** | No |
| **Also called** | Phase disk snapshot |

## What it does

Selecting this tool and clicking a point on the circuit inserts a dashed vertical divider with one small disk per qubit wire, colored to show that qubit's phase at that moment - using the same Phase color wheel as the [Q-Sphere](../tour/visualizations/q-sphere.md) and [Statevector](../tour/visualizations/statevector.md) panels. It's a way to "freeze" and inspect phase information at a specific step, without needing those panels open.

## Example

See [Phase disks](../tour/visualizations/phase-disks.md) for a full walkthrough, including how the disk's appearance changes as you add [S](s-gate.md) and [T](t-gate.md) gates before the snapshot point.

## Related

- [Phase disks](../tour/visualizations/phase-disks.md) - including a worked Bell-state example, both before and after adding measurement gates
- [Circuit](../tour/drag-drop/circuit.md#phase-disks-in-circuit) - where to find the phase disk tool while building a circuit
