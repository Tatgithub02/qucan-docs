# What it can do

A quick overview of Qompile's capabilities - see [Tour of Qompile](tour/overview.md) for the full walkthrough of each.

## Build circuits visually

Drag gates from the [Operations](tour/drag-drop/operations.md) catalog onto the [Circuit](tour/drag-drop/circuit.md) canvas. Supports single- and multi-qubit gates (including CNOT and SWAP), parameterized gates like `RZ` and `U`, editing gates after placement, and multiple layout modes (Left, Layers, Freeform alignment).

## Build circuits with code

Write or read your circuit in **[OpenQASM, Qiskit, Cirq, or Q#](tour/code/openqasm.md)** - fully synced with the visual canvas in both directions.

## Manage registers

Add, rename, and resize **quantum and classical registers** at any time via [Manage registers](tour/drag-drop/circuit.md#managing-registers).

## Visualize the quantum state live

Three panels update automatically as you build:

- **[Probabilities](tour/visualizations/probabilities.md)** - measurement outcome probabilities as a bar chart
- **[Q-Sphere](tour/visualizations/q-sphere.md)** - 3D visualization of the full quantum state
- **[Statevector](tour/visualizations/statevector.md)** - amplitude chart plus the raw statevector array

All three support table views, and exporting as SVG/PNG/CSV depending on the panel.

## Load ready-made algorithms

Jump straight into canonical algorithms - [Bell states](algorithms/bell-states.md), superdense coding, quantum teleportation, Deutsch-Jozsa, Bernstein-Vazirani, Simon's, Grover's, QAOA, QPE, Shor's, and VQE - without building them from scratch.

## Customize your workspace

Rename circuits, control which panels are visible via the [View menu](tour/customizing.md#view), set a fixed [visualizations seed](tour/drag-drop/circuit.md#visualizations-seed) for reproducible results, and use standard File/Edit shortcuts (undo/redo, cut/copy/paste, import/export).

## Coming soon

**Run circuits and view results** - actually executing circuits (as opposed to live simulation of the state) is marked as a coming-soon feature.
