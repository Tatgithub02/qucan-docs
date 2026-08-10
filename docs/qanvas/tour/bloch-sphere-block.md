# Bloch sphere

The **Bloch sphere** block (found under [Quantum](tools.md#quantum) in the Tools panel) shows a single qubit's reduced state as a point on a sphere. It uses the same circuit-selector dropdown described on the [Coding](coding-block.md#choosing-which-circuit-to-show) page, pick a circuit by name (**Alpha**, **Beta**, ...) to show its qubits here.

## Picking a qubit

A circuit usually has more than one qubit, so tabs across the top let you switch which qubit's reduced state the sphere is showing, here **q[1]**:

![Bloch sphere block showing q[1], with an info tooltip explaining the view](../images/quantum/bloch-sphere-q1.png)

...and here **q[0]** on the same circuit:

![Bloch sphere block showing q[0]](../images/quantum/bloch-sphere-q0.png)

!!! note
    The exact numbers shown above are just illustrations of the UI, not a worked example, don't read them as a specific claim about what any particular circuit produces.

## Reading the sphere

Clicking the info icon (in the block's header) shows a short explanation in place:

> The Bloch sphere shows the reduced state of a single qubit. \( |0\rangle \) is the north pole, \( |1\rangle \) the south; the polar angle θ sets the probabilities and the azimuth φ the relative phase. A vector shorter than 1 means the qubit is entangled or mixed. Drag to rotate the view.

Underneath the sphere, the qubit's reduced state is spelled out as an equation (\( |\psi\rangle = \dots|0\rangle + \dots|1\rangle \)), along with its θ, φ, r (the vector's length), and x/y/z coordinates.

## Header controls

Alongside the qubit tabs and circuit dropdown, the header offers a reset icon (return to the default view angle), the info icon described above, a table/grid icon, and a **⋮** menu for further options, plus the usual expand and close icons shared by every block.
