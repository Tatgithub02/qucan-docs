# Gate reference

This section is a complete reference for every operation in the Qompile [Operations](../tour/drag-drop/operations.md) catalog - one page per gate, aimed at anyone (including students) who wants more than "drag it onto the circuit." Each page covers what the gate does, its matrix, how it acts on basis states, a minimal example, and links to related gates.

!!! note "How this is organized"
    The categories below (Foundational, Phase, Rotation, and so on) are a learning-oriented grouping for this reference, not necessarily the exact category names shown in the Operations catalog itself. In the app, gates are grouped and color-coded by family (e.g. **Hadamard**, **Classical**) - see [Catalog view](../tour/drag-drop/operations.md#catalog-view) and [List view](../tour/drag-drop/operations.md#list-view).

## Foundational gates

The basic single-qubit building blocks: doing nothing, flipping a bit, and creating superposition.

- [Identity (I)](identity.md)
- [Pauli-X / NOT](pauli-x.md)
- [Pauli-Y](pauli-y.md)
- [Pauli-Z](pauli-z.md)
- [Hadamard (H)](hadamard.md)

## Phase gates

Gates that leave measurement probabilities alone but shift the *relative phase* between \( |0\rangle \) and \( |1\rangle \) - the foundation for interference effects. See [Phase disks](../tour/visualizations/phase-disks.md) for a visual walkthrough using these gates.

- [S](s-gate.md) and [S†](s-dagger.md)
- [T](t-gate.md) and [T†](t-dagger.md)
- [P](p-gate.md) - the general phase gate
- [RZ](rz-gate.md)

## Rotation gates

Continuously tunable single-qubit gates, parameterized by an angle (or three, for U).

- [RX](rx-gate.md)
- [RY](ry-gate.md)
- [√X](sqrt-x.md) and [√X†](sqrt-x-dagger.md)
- [U](u-gate.md) - the fully general single-qubit gate

## Multi-qubit and controlled gates

Gates that act on two or more qubits together, including the standard way to create entanglement.

- [CNOT](cnot.md)
- [Toffoli](toffoli.md)
- [SWAP](swap.md)
- [RXX](rxx-gate.md) and [RZZ](rzz-gate.md)
- [RCCX](rccx.md) and [RC3X](rc3x.md)

## Measurement and control flow

Operations that read out or route classical information, plus tools for building custom controlled gates.

- [Controls and conditionals](controls-and-conditionals.md) - start here for how quantum controls and classical conditionals differ
- [Measurement](measurement.md)
- [Reset](reset.md)
- [Barrier](barrier.md)
- [Control](control.md)
- [Conditional (if)](conditional.md)
- [Phase disk marker](phase-disk-marker.md)
