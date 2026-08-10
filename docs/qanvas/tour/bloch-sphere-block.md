# Bloch sphere

The **Bloch sphere** block (found under [Quantum](tools.md#quantum) in the Tools panel) shows a single qubit's reduced state as a point on a sphere. It uses the same circuit-selector dropdown described on the [Coding](coding-block.md#choosing-which-circuit-to-show) page, pick a circuit by name (**Alpha**, **Beta**, ...) to show its qubits here.

## Picking a qubit

A circuit usually has more than one qubit, so tabs across the top let you switch which qubit's reduced state the sphere is showing. Here's a 3-qubit **Alpha** circuit, first with **q[0]** selected:

![Bloch sphere block for circuit Alpha, showing q[0] as an equal superposition](../images/quantum/bloch-sphere-q0.png)

Its point sits on the equator, halfway between \( |0\rangle \) and \( |1\rangle \), matching the equation underneath: \( |\psi\rangle = \sqrt{0.5}\,|0\rangle + \sqrt{0.5}\,|1\rangle \), an equal superposition.

...and here's the same circuit with **q[1]** selected instead:

![Bloch sphere block for circuit Alpha, showing q[1] resting at the north pole](../images/quantum/bloch-sphere-q1.png)

This qubit's vector points straight up to \( |0\rangle \), matching \( |\psi\rangle = 1\,|0\rangle + 0\,|1\rangle \), a definite state with no superposition.

!!! note
    The exact numbers shown above are just illustrations of the UI, not a worked example, don't read them as a specific claim about what any particular circuit produces.

## Reading the sphere

Clicking the info icon (in the block's header) shows a short explanation in place:

> The Bloch sphere shows the reduced state of a single qubit. \( |0\rangle \) is the north pole, \( |1\rangle \) the south; the polar angle θ sets the probabilities and the azimuth φ the relative phase. A vector shorter than 1 means the qubit is entangled or mixed. Drag to rotate the view.

Underneath the sphere, the qubit's reduced state is spelled out as an equation (\( |\psi\rangle = \dots|0\rangle + \dots|1\rangle \)), along with its θ, φ, r (the vector's length), and x/y/z coordinates.

## Header controls

Alongside the qubit tabs and circuit dropdown, the header offers a reset icon (return to the default view angle), the info icon described above, a table/grid icon, and a **⋮** menu for further options, plus the usual expand and close icons shared by every block.
