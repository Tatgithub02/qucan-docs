# What is Qompile?

**Qompile** is a browser-based quantum circuit composer, part of the [Qucan](../index.md) platform. It's a visual workspace for building, editing, and exploring quantum circuits.

At its core, Qompile gives you two equivalent ways to build the same circuit:

- **Drag-and-drop** — assemble a circuit by dragging gates from a catalog onto a canvas of quantum and classical registers.
- **Code** — write the circuit directly in OpenQASM, Qiskit, Cirq, or Q#.

These two views are fully synced: change the circuit visually and the code updates instantly, or edit the code and watch the circuit diagram redraw itself. Neither view is the "source of truth" — they're two windows onto the same underlying circuit.

Alongside the editor, Qompile includes a set of **live visualization panels** — Probabilities, Q-Sphere, and Statevector — that update in real time as you build, so you can see the effect of every gate on the quantum state immediately rather than only after running the circuit.

Qompile also ships with a library of **ready-made algorithms** (Bell states, Grover's, Shor's, and others) that you can load directly, making it a practical way to study canonical algorithms as well as build your own circuits from scratch.

## Get started

- **Take the grand tour** — [Tour of Qompile](tour/overview.md) walks through every part of the interface.
- **See what it can do** — [Capabilities overview](what-it-can-do.md) for a quick summary.
- **Browse algorithms** — [Ready algorithms](algorithms/overview.md) covers all 12 built-in algorithms.

## You might also like

- [Learn with QCAP](../qcap/index.md) — structured quantum computing curriculum with modules and live sessions.
- [Explore Qanvas](../qanvas/index.md) — freeform whiteboard for quantum building blocks.
- [Gate reference](gates/index.md) — all 29 quantum gates with matrices, symbols, and worked examples.
- [Read & publish on Sqope](../sqope/index.md) — quantum computing news, research, and conversations.
