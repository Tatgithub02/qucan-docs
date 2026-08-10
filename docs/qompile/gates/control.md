# Control

![Control point tile from the Operations catalog](../images/gates/control.png){ .gate-tile }

The **Control** tile is a standalone control point you can drag onto a wire and connect to another gate - the general-purpose way to build a custom controlled version of any gate, not just the built-in [CNOT](cnot.md) and [Toffoli](toffoli.md).

| | |
|---|---|
| **Qubits** | 1 (per control point placed) |
| **Parameters** | None - it takes on whatever gate it's connected to |
| **Changes the quantum state?** | Only via the gate it controls |
| **Also called** | Control point |

## What it does

Where CNOT and Toffoli are pre-built controlled-X gates, the standalone Control tile lets you add a control condition to *any* gate - for example, a controlled-Z, a controlled-H, or a controlled rotation - by placing the control dot on one wire and connecting it to the gate you want controlled on another wire. The connected gate only applies when the control qubit is \( |1\rangle \), exactly like the control half of a CNOT.

## Example

Dragging a Control point onto `q[0]` and connecting it to a [Z gate](pauli-z.md) on `q[1]` builds a controlled-Z - a gate not otherwise in the default catalog.

## Related

- [CNOT](cnot.md) - a built-in controlled-X
- [Toffoli](toffoli.md) - a built-in, two-control controlled-X
- [Controls and conditionals](controls-and-conditionals.md)
