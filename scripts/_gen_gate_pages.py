# -*- coding: utf-8 -*-
"""Generates the one-page-per-gate reference under docs/qompile/gates/.

This script is a build-time authoring aid, not part of the published site.
"""
import os

OUT_DIR = 'docs/qompile/gates'
IMG_DIR = '../images/gates'
os.makedirs(OUT_DIR, exist_ok=True)


def table(rows):
    lines = ['| | |', '|---|---|']
    for k, v in rows:
        lines.append(f'| **{k}** | {v} |')
    return '\n'.join(lines)


def names_table(rows):
    """rows: list of (lang, code_or_None)"""
    lines = ['| Language | Typical form |', '|---|---|']
    for lang, code in rows:
        cell = f'`{code}`' if code else '-'
        lines.append(f'| {lang} | {cell} |')
    return '\n'.join(lines)


def related(items):
    return '\n'.join(f'- {label}' for label in items)


def page(meta):
    parts = []
    parts.append(f"# {meta['title']}\n")
    parts.append(f"![{meta['tile_alt']} tile from the Operations catalog]({IMG_DIR}/{meta['image']}){{ .gate-tile }}\n")
    parts.append(meta['summary'] + '\n')
    parts.append(table(meta['facts']) + '\n')

    if meta.get('category_note'):
        parts.append(meta['category_note'] + '\n')

    parts.append('## What it does\n')
    parts.append(meta['what_it_does'] + '\n')

    if meta.get('matrix'):
        parts.append('## Matrix\n')
        parts.append(meta['matrix'] + '\n')

    if meta.get('basis_action'):
        parts.append('## Action on basis states\n')
        parts.append(meta['basis_action'] + '\n')

    if meta.get('bloch'):
        parts.append('## Phase and Bloch-sphere effect\n')
        parts.append(meta['bloch'] + '\n')

    if meta.get('example'):
        parts.append('## Example\n')
        parts.append(meta['example'] + '\n')

    if meta.get('names'):
        parts.append('## Other notations\n')
        parts.append(
            "Naming conventions across ecosystems; exact syntax can vary by library version, "
            "and this does not claim to be Qompile's generated output unless otherwise noted.\n"
        )
        parts.append(names_table(meta['names']) + '\n')

    if meta.get('notes'):
        parts.append('## Notes\n')
        parts.append(meta['notes'] + '\n')

    if meta.get('related'):
        parts.append('## Related\n')
        parts.append(related(meta['related']) + '\n')

    return '\n'.join(parts).rstrip() + '\n'


GATES = []

# ---------------------------------------------------------------- Identity
GATES.append(dict(
    key='identity',
    title='Identity (I)',
    image='identity.png',
    tile_alt='Identity gate',
    summary=(
        "The **identity gate** does nothing to the qubit's state. It exists so a wire can "
        "have an explicit, visible placeholder operation - for example to pad a circuit's "
        "timing/layout - without changing what the qubit represents."
    ),
    facts=[
        ('Qubits', '1'),
        ('Parameters', 'None'),
        ('Inverse', 'Itself (I is its own inverse)'),
        ('Also called', 'Identity, No-op'),
    ],
    what_it_does=(
        "Applying `I` leaves every amplitude exactly as it was. It's a genuine gate in the "
        "mathematical sense (a valid 1-qubit unitary), it's simply the unitary that changes nothing."
    ),
    matrix=r"""\[
I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
\]""",
    basis_action=(
        "- \\( |0\\rangle \\rightarrow |0\\rangle \\)\n"
        "- \\( |1\\rangle \\rightarrow |1\\rangle \\)"
    ),
    example=(
        "Placing `I` on `q[0]` leaves its state unchanged - useful mainly for visually marking "
        "a time step on a wire, or as a starting point before editing a gate's parameters."
    ),
    names=[
        ('OpenQASM 2.0', 'id q[0];'),
        ('Qiskit', 'circuit.id[q[0]]'),
        ('Cirq', 'cirq.I(q[0])'),
        ('Q#', 'I(q[0]);'),
    ],
    related=[
        '[Pauli-X / NOT](pauli-x.md) - the gate that flips a qubit',
        '[Hadamard (H)](hadamard.md) - the gate that creates superposition',
    ],
))

# ---------------------------------------------------------------- Pauli-X
GATES.append(dict(
    key='pauli-x',
    title='Pauli-X / NOT',
    image='not.png',
    tile_alt='NOT gate',
    summary=(
        "The **Pauli-X gate**, shown in Qompile's catalog as **NOT**, is the quantum "
        "equivalent of a classical NOT gate - it flips \\( |0\\rangle \\) to \\( |1\\rangle \\) "
        "and vice versa."
    ),
    facts=[
        ('Qubits', '1'),
        ('Parameters', 'None'),
        ('Inverse', 'Itself (X² = I)'),
        ('Also called', 'X gate, bit-flip gate, quantum NOT'),
    ],
    what_it_does=(
        "X swaps the amplitudes of \\( |0\\rangle \\) and \\( |1\\rangle \\). Applied to a "
        "definite state it behaves exactly like a classical bit flip; applied to a superposition "
        "it swaps the two amplitudes while leaving their values (and any phase) otherwise intact."
    ),
    matrix=r"""\[
X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
\]""",
    basis_action=(
        "- \\( |0\\rangle \\rightarrow |1\\rangle \\)\n"
        "- \\( |1\\rangle \\rightarrow |0\\rangle \\)"
    ),
    bloch=(
        "On the Bloch sphere, X is a 180° rotation about the X-axis. It swaps the north and "
        "south poles (\\( |0\\rangle \\) and \\( |1\\rangle \\)) and leaves points on the X-axis unmoved."
    ),
    example=(
        "Placing `X` on `q[0]` (initially \\( |0\\rangle \\)) prepares \\( |1\\rangle \\) - the "
        "[Probabilities](../tour/visualizations/probabilities.md) panel then shows 100% on outcome `1`."
    ),
    names=[
        ('OpenQASM 2.0', 'x q[0];'),
        ('Qiskit', 'circuit.x[q[0]]'),
        ('Cirq', 'cirq.X(q[0])'),
        ('Q#', 'X(q[0]);'),
    ],
    related=[
        '[Pauli-Y](pauli-y.md)',
        '[Pauli-Z](pauli-z.md)',
        '[CNOT](cnot.md) - applies X to a target qubit only when a control qubit is \\(|1\\rangle\\)',
    ],
))

# ---------------------------------------------------------------- Pauli-Y
GATES.append(dict(
    key='pauli-y',
    title='Pauli-Y',
    image='y-gate.png',
    tile_alt='Y gate',
    summary=(
        "The **Pauli-Y gate** flips the qubit like X, but also rotates its phase - it's the "
        "\"bit-and-phase-flip\" member of the Pauli family."
    ),
    facts=[
        ('Qubits', '1'),
        ('Parameters', 'None'),
        ('Inverse', 'Itself (Y² = I)'),
        ('Also called', 'Y gate'),
    ],
    what_it_does=(
        "Y swaps \\( |0\\rangle \\) and \\( |1\\rangle \\) like X does, but multiplies each "
        "resulting amplitude by \\( \\pm i \\). It is equal, up to a global phase, to applying "
        "Z and then X (or X then Z, with opposite sign): \\( Y = iXZ \\)."
    ),
    matrix=r"""\[
Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}
\]""",
    basis_action=(
        "- \\( |0\\rangle \\rightarrow i\\,|1\\rangle \\)\n"
        "- \\( |1\\rangle \\rightarrow -i\\,|0\\rangle \\)"
    ),
    bloch=(
        "On the Bloch sphere, Y is a 180° rotation about the Y-axis - it swaps the poles "
        "like X, but rotates points on the equator in the opposite sense to X."
    ),
    example=(
        "Placing `Y` on `q[0]` (initially \\( |0\\rangle \\)) prepares \\( i\\,|1\\rangle \\). "
        "In the [Statevector](../tour/visualizations/statevector.md) panel, the `1` amplitude has "
        "the same magnitude as an X gate would give, but a different phase color."
    ),
    names=[
        ('OpenQASM 2.0', 'y q[0];'),
        ('Qiskit', 'circuit.y[q[0]]'),
        ('Cirq', 'cirq.Y(q[0])'),
        ('Q#', 'Y(q[0]);'),
    ],
    related=[
        '[Pauli-X / NOT](pauli-x.md)',
        '[Pauli-Z](pauli-z.md)',
    ],
))

# ---------------------------------------------------------------- Pauli-Z
GATES.append(dict(
    key='pauli-z',
    title='Pauli-Z',
    image='z-gate.png',
    tile_alt='Z gate',
    summary=(
        "The **Pauli-Z gate** leaves \\( |0\\rangle \\) alone and flips the sign of "
        "\\( |1\\rangle \\). It's the simplest possible \"phase flip.\""
    ),
    facts=[
        ('Qubits', '1'),
        ('Parameters', 'None'),
        ('Inverse', 'Itself (Z² = I)'),
        ('Also called', 'Z gate, phase-flip gate; equal to P(π)'),
    ],
    what_it_does=(
        "Z does nothing visible to a qubit that's definitely \\( |0\\rangle \\) or \\( |1\\rangle \\) "
        "- measuring gives the same result either way. Its effect only becomes visible on a "
        "superposition, where it flips the *relative phase* between the \\( |0\\rangle \\) and "
        "\\( |1\\rangle \\) components by \\( \\pi \\)."
    ),
    matrix=r"""\[
Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
\]""",
    basis_action=(
        "- \\( |0\\rangle \\rightarrow |0\\rangle \\)\n"
        "- \\( |1\\rangle \\rightarrow -|1\\rangle \\)"
    ),
    bloch=(
        "On the Bloch sphere, Z is a 180° rotation about the Z-axis, which passes straight "
        "through the poles - so the poles (\\( |0\\rangle \\), \\( |1\\rangle \\)) don't move, "
        "but any point on the equator (an equal superposition) rotates halfway around. See "
        "[Phase disks](../tour/visualizations/phase-disks.md) for how this shows up visually."
    ),
    example=(
        "`H` then `Z` on `q[0]` turns \\( |{+}\\rangle = (|0\\rangle+|1\\rangle)/\\sqrt{2} \\) "
        "into \\( |{-}\\rangle = (|0\\rangle-|1\\rangle)/\\sqrt{2} \\) - same measurement "
        "probabilities as plain `H`, but a different relative phase."
    ),
    names=[
        ('OpenQASM 2.0', 'z q[0];'),
        ('Qiskit', 'circuit.z[q[0]]'),
        ('Cirq', 'cirq.Z(q[0])'),
        ('Q#', 'Z(q[0]);'),
    ],
    related=[
        '[S](s-gate.md) and [T](t-gate.md) - smaller phase flips (π/2 and π/4) than Z\'s π',
        '[P](p-gate.md) - the general phase gate; Z = P(π)',
    ],
))

# ---------------------------------------------------------------- Hadamard
GATES.append(dict(
    key='hadamard',
    title='Hadamard (H)',
    image='hadamard.png',
    tile_alt='Hadamard gate',
    summary=(
        "The **Hadamard gate** is the standard way to create superposition. Applied to "
        "\\( |0\\rangle \\), it produces an equal mix of \\( |0\\rangle \\) and \\( |1\\rangle \\) "
        "- the starting point of most quantum algorithms."
    ),
    facts=[
        ('Qubits', '1'),
        ('Parameters', 'None'),
        ('Inverse', 'Itself (H² = I)'),
        ('Also called', 'H gate'),
    ],
    what_it_does=(
        "H maps each basis state to an equal-weight superposition of both basis states, "
        "with a relative sign that depends on which one it started from. Qompile's own gate "
        "info panel (opened via the **Info** action described in "
        "[Editing, viewing info, and other gate actions](../tour/drag-drop/circuit.md#editing-viewing-info-and-other-gate-actions)) "
        "puts it this way:\n\n"
        "> The Hadamard gate creates superposition by mapping "
        "\\( |0\\rangle \\mapsto |{+}\\rangle = \\dfrac{1}{\\sqrt{2}}(|0\\rangle+|1\\rangle) \\) "
        "and \\( |1\\rangle \\mapsto |{-}\\rangle = \\dfrac{1}{\\sqrt{2}}(|0\\rangle-|1\\rangle) \\)."
    ),
    matrix=r"""\[
H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}
\]""",
    basis_action=(
        "- \\( |0\\rangle \\rightarrow \\dfrac{1}{\\sqrt{2}}\\big(|0\\rangle + |1\\rangle\\big) = |{+}\\rangle \\)\n"
        "- \\( |1\\rangle \\rightarrow \\dfrac{1}{\\sqrt{2}}\\big(|0\\rangle - |1\\rangle\\big) = |{-}\\rangle \\)"
    ),
    bloch=(
        "On the Bloch sphere, H swaps the Z-axis and X-axis (with a sign flip) - it's a 180° "
        "rotation about the diagonal axis halfway between X and Z. That's why applying H twice "
        "returns you to where you started."
    ),
    example=(
        "`H` on `q[0]` (starting at \\( |0\\rangle \\)) is the first step of a "
        "[Bell state](../algorithms/bell-states.md): once followed by a [CNOT](cnot.md), it "
        "produces the entangled state \\( (|00\\rangle+|11\\rangle)/\\sqrt{2} \\)."
    ),
    names=[
        ('OpenQASM 2.0', 'h q[0];'),
        ('Qiskit', 'circuit.h[q[0]]'),
        ('Cirq', 'cirq.H(q[0])'),
        ('Q#', 'H(q[0]);'),
    ],
    related=[
        '[Bell states](../algorithms/bell-states.md) - H + CNOT, the canonical example',
        '[CNOT](cnot.md)',
        '[Phase disks](../tour/visualizations/phase-disks.md) - see phase change after H, S, T',
    ],
))

# ---------------------------------------------------------------- S
GATES.append(dict(
    key='s-gate',
    title='S',
    image='s-gate.png',
    tile_alt='S gate',
    summary=(
        "The **S gate** leaves \\( |0\\rangle \\) alone and multiplies \\( |1\\rangle \\) by "
        "\\( i \\) - a quarter-turn phase shift. It's also called the **√Z gate**, since "
        "applying it twice is the same as one Z gate."
    ),
    facts=[
        ('Qubits', '1'),
        ('Parameters', 'None'),
        ('Inverse', '[S†](s-dagger.md) (not self-inverse)'),
        ('Also called', '√Z, phase gate; equal to P(π/2)'),
    ],
    what_it_does=(
        "S adds a relative phase of \\( \\pi/2 \\) (90°) between the \\( |1\\rangle \\) and "
        "\\( |0\\rangle \\) components of a state, without changing measurement probabilities "
        "in the computational basis. \\( S^2 = Z \\), which is why it's read as \"square root of Z.\""
    ),
    matrix=r"""\[
S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}
\]""",
    basis_action=(
        "- \\( |0\\rangle \\rightarrow |0\\rangle \\)\n"
        "- \\( |1\\rangle \\rightarrow i\\,|1\\rangle \\)"
    ),
    bloch=(
        "S rotates the Bloch vector by \\( \\pi/2 \\) about the Z-axis. On a state that's already "
        "a superposition, this is exactly the kind of phase change visualized by "
        "[phase disks](../tour/visualizations/phase-disks.md), the [Q-Sphere](../tour/visualizations/q-sphere.md), "
        "and the [Statevector](../tour/visualizations/statevector.md) chart - see the worked "
        "H → S → T example on the phase disks page."
    ),
    example=(
        "`H` then `S` on `q[0]` produces \\( \\dfrac{1}{\\sqrt{2}}(|0\\rangle + i|1\\rangle) \\): "
        "the same 50/50 measurement split as plain `H`, but the \\( |1\\rangle \\) bar in the "
        "Statevector chart is now colored a quarter-turn around the Phase wheel from the \\( |0\\rangle \\) bar."
    ),
    names=[
        ('OpenQASM 2.0', 's q[0];'),
        ('Qiskit', 'circuit.s[q[0]]'),
        ('Cirq', 'cirq.S(q[0])'),
        ('Q#', 'S(q[0]);'),
    ],
    related=[
        '[S†](s-dagger.md) - the inverse of S',
        '[T](t-gate.md) - a smaller, π/4 phase step',
        '[P](p-gate.md) - the general phase gate; S = P(π/2)',
        '[Phase disks](../tour/visualizations/phase-disks.md)',
    ],
))

# ---------------------------------------------------------------- S dagger
GATES.append(dict(
    key='s-dagger',
    title='S†',
    image='s-dagger.png',
    tile_alt='S-dagger gate',
    summary=(
        "**S†** (\"S-dagger\") is the inverse of the [S gate](s-gate.md): it multiplies "
        "\\( |1\\rangle \\) by \\( -i \\) instead of \\( +i \\), undoing whatever S did."
    ),
    facts=[
        ('Qubits', '1'),
        ('Parameters', 'None'),
        ('Inverse', '[S](s-gate.md)'),
        ('Also called', 'S-dagger, adjoint of S; equal to P(−π/2)'),
    ],
    what_it_does=(
        "S† rotates the relative phase between \\( |1\\rangle \\) and \\( |0\\rangle \\) by "
        "\\( -\\pi/2 \\). Applying S followed by S† (in either order) returns a state to exactly "
        "where it started."
    ),
    matrix=r"""\[
S^\dagger = \begin{pmatrix} 1 & 0 \\ 0 & -i \end{pmatrix}
\]""",
    basis_action=(
        "- \\( |0\\rangle \\rightarrow |0\\rangle \\)\n"
        "- \\( |1\\rangle \\rightarrow -i\\,|1\\rangle \\)"
    ),
    example=(
        "`H`, then `S`, then `S†` on `q[0]` returns exactly to \\( |{+}\\rangle \\), the same "
        "state plain `H` alone would give."
    ),
    names=[
        ('OpenQASM 2.0', 'sdg q[0];'),
        ('Qiskit', 'circuit.sdg[q[0]]'),
        ('Cirq', 'cirq.S(q[0])**-1'),
        ('Q#', 'Adjoint S(q[0]);'),
    ],
    related=[
        '[S](s-gate.md)',
        '[T†](t-dagger.md)',
    ],
))

# ---------------------------------------------------------------- T
GATES.append(dict(
    key='t-gate',
    title='T',
    image='t-gate.png',
    tile_alt='T gate',
    summary=(
        "The **T gate** applies a smaller phase shift than S - \\( \\pi/4 \\) (45°) instead of "
        "\\( \\pi/2 \\). It's also called the **√S gate**, and is especially important because "
        "it's one of the few gates needed to reach *any* quantum computation when combined with "
        "H and CNOT."
    ),
    facts=[
        ('Qubits', '1'),
        ('Parameters', 'None'),
        ('Inverse', '[T†](t-dagger.md) (not self-inverse)'),
        ('Also called', '√S, π/8 gate; equal to P(π/4)'),
    ],
    what_it_does=(
        "T adds a relative phase of \\( \\pi/4 \\) between \\( |1\\rangle \\) and \\( |0\\rangle \\). "
        "\\( T^2 = S \\) and \\( T^4 = Z \\) - four T gates in a row bring you back to where two "
        "S gates (or one Z) would."
    ),
    matrix=r"""\[
T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}
\]""",
    basis_action=(
        "- \\( |0\\rangle \\rightarrow |0\\rangle \\)\n"
        "- \\( |1\\rangle \\rightarrow e^{i\\pi/4}\\,|1\\rangle \\)"
    ),
    bloch=(
        "T rotates the Bloch vector by only \\( \\pi/4 \\) about the Z-axis - an eighth of a "
        "full turn, and half of what S does. See the worked H → T → S example on the "
        "[Phase disks](../tour/visualizations/phase-disks.md) page for how this looks in the app."
    ),
    example=(
        "`H` then `T` on `q[0]` gives \\( \\dfrac{1}{\\sqrt{2}}(|0\\rangle + e^{i\\pi/4}|1\\rangle) \\): "
        "identical measurement odds to plain `H`, with the \\( |1\\rangle \\) component's phase "
        "color rotated an eighth of the way around the Phase wheel - half as far as `S` would move it."
    ),
    names=[
        ('OpenQASM 2.0', 't q[0];'),
        ('Qiskit', 'circuit.t[q[0]]'),
        ('Cirq', 'cirq.T(q[0])'),
        ('Q#', 'T(q[0]);'),
    ],
    notes=(
        "T is not one of the Clifford gates (I, X, Y, Z, H, S, CNOT) - adding it is what makes "
        "a gate set \"universal,\" able to approximate any quantum computation. This is why T "
        "shows up so often in algorithm resource-counting discussions."
    ),
    related=[
        '[S](s-gate.md) - T² = S',
        '[T†](t-dagger.md) - the inverse of T',
        '[Phase disks](../tour/visualizations/phase-disks.md)',
    ],
))

# ---------------------------------------------------------------- T dagger
GATES.append(dict(
    key='t-dagger',
    title='T†',
    image='t-dagger.png',
    tile_alt='T-dagger gate',
    summary=(
        "**T†** (\"T-dagger\") is the inverse of the [T gate](t-gate.md): a \\( -\\pi/4 \\) "
        "phase shift instead of \\( +\\pi/4 \\)."
    ),
    facts=[
        ('Qubits', '1'),
        ('Parameters', 'None'),
        ('Inverse', '[T](t-gate.md)'),
        ('Also called', 'T-dagger, adjoint of T; equal to P(−π/4)'),
    ],
    what_it_does=(
        "T† rotates the relative phase between \\( |1\\rangle \\) and \\( |0\\rangle \\) by "
        "\\( -\\pi/4 \\), undoing a T gate."
    ),
    matrix=r"""\[
T^\dagger = \begin{pmatrix} 1 & 0 \\ 0 & e^{-i\pi/4} \end{pmatrix}
\]""",
    basis_action=(
        "- \\( |0\\rangle \\rightarrow |0\\rangle \\)\n"
        "- \\( |1\\rangle \\rightarrow e^{-i\\pi/4}\\,|1\\rangle \\)"
    ),
    example=(
        "Two T† gates in a row are the same as one S† gate; four are the same as one Z gate."
    ),
    names=[
        ('OpenQASM 2.0', 'tdg q[0];'),
        ('Qiskit', 'circuit.tdg[q[0]]'),
        ('Cirq', 'cirq.T(q[0])**-1'),
        ('Q#', 'Adjoint T(q[0]);'),
    ],
    related=[
        '[T](t-gate.md)',
        '[S†](s-dagger.md)',
    ],
))

# ---------------------------------------------------------------- P
GATES.append(dict(
    key='p-gate',
    title='P (phase)',
    image='p-gate.png',
    tile_alt='P gate',
    summary=(
        "The **P gate** is the general-purpose phase gate: pick any angle \\( \\theta \\), and "
        "P applies exactly that much relative phase to \\( |1\\rangle \\). Z, S, and T are all "
        "just P with a specific angle plugged in."
    ),
    facts=[
        ('Qubits', '1'),
        ('Parameters', '\\( \\theta \\) - phase angle, in radians'),
        ('Inverse', 'P(−θ)'),
        ('Also called', 'Phase gate; sometimes written R1 or U1'),
    ],
    what_it_does=(
        "P(θ) leaves \\( |0\\rangle \\) completely untouched and multiplies \\( |1\\rangle \\) by "
        "\\( e^{i\\theta} \\). Setting \\( \\theta = \\pi/4, \\pi/2, \\pi \\) reproduces T, S, and "
        "Z exactly."
    ),
    matrix=r"""\[
P(\theta) = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\theta} \end{pmatrix}
\]""",
    basis_action=(
        "- \\( |0\\rangle \\rightarrow |0\\rangle \\)\n"
        "- \\( |1\\rangle \\rightarrow e^{i\\theta}\\,|1\\rangle \\)"
    ),
    bloch=(
        "P(θ) rotates the Bloch vector by θ about the Z-axis - like [RZ](rz-gate.md), but "
        "without RZ's extra overall phase factor (see the note on that page for the exact "
        "relationship between the two)."
    ),
    example=(
        "`H` then `P` with \\( \\theta = \\pi/3 \\) on `q[0]` gives "
        "\\( \\dfrac{1}{\\sqrt{2}}(|0\\rangle + e^{i\\pi/3}|1\\rangle) \\) - any angle you like, "
        "not just the fixed steps S and T provide."
    ),
    names=[
        ('OpenQASM 2.0', 'u1(theta) q[0];'),
        ('Qiskit', 'circuit.p[theta, q[0]]'),
        ('Cirq', 'cirq.ZPowGate(exponent=theta / math.pi)(q[0])'),
        ('Q#', 'R1(theta, q[0]);'),
    ],
    related=[
        '[RZ](rz-gate.md) - the same phase step, plus an overall phase factor',
        '[S](s-gate.md) = P(π/2), [T](t-gate.md) = P(π/4), [Pauli-Z](pauli-z.md) = P(π)',
    ],
))

# ---------------------------------------------------------------- RZ
GATES.append(dict(
    key='rz-gate',
    title='RZ',
    image='rz-gate.png',
    tile_alt='RZ gate',
    summary=(
        "**RZ** rotates a qubit by an angle \\( \\theta \\) about the Z-axis of the Bloch "
        "sphere. It produces the same *relative* phase shift as [P](p-gate.md), but - unlike "
        "P - also applies an overall phase, making it a true rotation."
    ),
    facts=[
        ('Qubits', '1'),
        ('Parameters', '\\( \\theta \\) - rotation angle, in radians'),
        ('Inverse', 'RZ(−θ)'),
        ('Also called', 'Z-rotation'),
    ],
    what_it_does=(
        "RZ(θ) multiplies \\( |0\\rangle \\) by \\( e^{-i\\theta/2} \\) and \\( |1\\rangle \\) by "
        "\\( e^{i\\theta/2} \\). The *difference* between those two phases is θ - exactly what "
        "P(θ) produces - so RZ(θ) and P(θ) affect measurement probabilities identically: "
        "\\( RZ(\\theta) = e^{-i\\theta/2}\\,P(\\theta) \\)."
    ),
    matrix=r"""\[
RZ(\theta) = \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix}
\]""",
    basis_action=(
        "- \\( |0\\rangle \\rightarrow e^{-i\\theta/2}\\,|0\\rangle \\)\n"
        "- \\( |1\\rangle \\rightarrow e^{i\\theta/2}\\,|1\\rangle \\)"
    ),
    bloch=(
        "Because global phase (a factor applied equally to every amplitude in a state) has no "
        "observable effect, RZ(θ) and P(θ) move a qubit's point on the Bloch sphere identically "
        "- both are rotations by θ about the Z-axis. The difference only shows up when the "
        "qubit is *entangled* with, or has its phase compared against, another qubit that "
        "wasn't rotated - since global-phase equivalence only holds per-qubit, not for a shared "
        "multi-qubit state."
    ),
    example=(
        "`H` then `RZ` with \\( \\theta = \\pi/2 \\) on `q[0]` gives the same measurement "
        "probabilities as `H` then [S](s-gate.md) - the Probabilities panel is identical either way."
    ),
    names=[
        ('OpenQASM 2.0', 'rz(theta) q[0];'),
        ('Qiskit', 'circuit.rz[theta, q[0]]'),
        ('Cirq', 'cirq.rz(theta)(q[0])'),
        ('Q#', 'Rz(theta, q[0]);'),
    ],
    related=[
        '[P](p-gate.md) - the relative-phase-only version of this rotation',
        '[RX](rx-gate.md) and [RY](ry-gate.md) - the other two axis rotations',
    ],
))

# ---------------------------------------------------------------- RX
GATES.append(dict(
    key='rx-gate',
    title='RX',
    image='rx-gate.png',
    tile_alt='RX gate',
    summary=(
        "**RX** rotates a qubit by an angle \\( \\theta \\) about the X-axis of the Bloch "
        "sphere - the natural generalization of the [Pauli-X](pauli-x.md) gate to any rotation angle."
    ),
    facts=[
        ('Qubits', '1'),
        ('Parameters', '\\( \\theta \\) - rotation angle, in radians'),
        ('Inverse', 'RX(−θ)'),
        ('Also called', 'X-rotation'),
    ],
    what_it_does=(
        "RX(θ) smoothly interpolates between doing nothing (θ = 0) and a full X gate "
        "(θ = π, up to a global phase). Small angles produce a small amount of superposition; "
        "π radians fully flips the qubit."
    ),
    matrix=r"""\[
RX(\theta) = \begin{pmatrix}
\cos(\theta/2) & -i\sin(\theta/2) \\
-i\sin(\theta/2) & \cos(\theta/2)
\end{pmatrix}
\]""",
    basis_action=(
        "- \\( |0\\rangle \\rightarrow \\cos(\\theta/2)\\,|0\\rangle - i\\sin(\\theta/2)\\,|1\\rangle \\)\n"
        "- \\( |1\\rangle \\rightarrow -i\\sin(\\theta/2)\\,|0\\rangle + \\cos(\\theta/2)\\,|1\\rangle \\)"
    ),
    example=(
        "`RX` with \\( \\theta = \\pi/2 \\) on `q[0]` (starting at \\( |0\\rangle \\)) gives an "
        "equal superposition, like [H](hadamard.md) does - but with a different relative phase "
        "(an \\( -i \\) on the \\( |1\\rangle \\) term instead of a plain \\( + \\))."
    ),
    names=[
        ('OpenQASM 2.0', 'rx(theta) q[0];'),
        ('Qiskit', 'circuit.rx[theta, q[0]]'),
        ('Cirq', 'cirq.rx(theta)(q[0])'),
        ('Q#', 'Rx(theta, q[0]);'),
    ],
    related=[
        '[RY](ry-gate.md)',
        '[RZ](rz-gate.md)',
        '[U](u-gate.md) - RX(θ) = U(θ, −π/2, π/2)',
    ],
))

# ---------------------------------------------------------------- RY
GATES.append(dict(
    key='ry-gate',
    title='RY',
    image='ry-gate.png',
    tile_alt='RY gate',
    summary=(
        "**RY** rotates a qubit by an angle \\( \\theta \\) about the Y-axis of the Bloch "
        "sphere. Unlike RX and RZ, its matrix entries are all real numbers, which makes it a "
        "common choice for building superpositions with adjustable probabilities."
    ),
    facts=[
        ('Qubits', '1'),
        ('Parameters', '\\( \\theta \\) - rotation angle, in radians'),
        ('Inverse', 'RY(−θ)'),
        ('Also called', 'Y-rotation'),
    ],
    what_it_does=(
        "RY(θ) turns \\( |0\\rangle \\) into a superposition weighted by \\( \\cos(\\theta/2) \\) "
        "and \\( \\sin(\\theta/2) \\), with no complex phase at all - useful whenever you want to "
        "dial in a specific measurement probability directly."
    ),
    matrix=r"""\[
RY(\theta) = \begin{pmatrix}
\cos(\theta/2) & -\sin(\theta/2) \\
\sin(\theta/2) & \cos(\theta/2)
\end{pmatrix}
\]""",
    basis_action=(
        "- \\( |0\\rangle \\rightarrow \\cos(\\theta/2)\\,|0\\rangle + \\sin(\\theta/2)\\,|1\\rangle \\)\n"
        "- \\( |1\\rangle \\rightarrow -\\sin(\\theta/2)\\,|0\\rangle + \\cos(\\theta/2)\\,|1\\rangle \\)"
    ),
    example=(
        "`RY` with \\( \\theta = \\pi/3 \\) on `q[0]` (starting at \\( |0\\rangle \\)) gives "
        "\\( \\cos(\\pi/6)|0\\rangle + \\sin(\\pi/6)|1\\rangle \\), which the "
        "[Probabilities](../tour/visualizations/probabilities.md) panel shows as a 75%/25% split."
    ),
    names=[
        ('OpenQASM 2.0', 'ry(theta) q[0];'),
        ('Qiskit', 'circuit.ry[theta, q[0]]'),
        ('Cirq', 'cirq.ry(theta)(q[0])'),
        ('Q#', 'Ry(theta, q[0]);'),
    ],
    related=[
        '[RX](rx-gate.md)',
        '[RZ](rz-gate.md)',
        '[U](u-gate.md) - RY(θ) = U(θ, 0, 0)',
    ],
))

# ---------------------------------------------------------------- sqrt X
GATES.append(dict(
    key='sqrt-x',
    title='√X',
    image='sqrt-x.png',
    tile_alt='Square-root-of-X gate',
    summary=(
        "**√X** (\"square root of X\") is a gate that, applied twice, is exactly equal to one "
        "[Pauli-X](pauli-x.md) gate. It's a common native gate on real quantum hardware."
    ),
    facts=[
        ('Qubits', '1'),
        ('Parameters', 'None'),
        ('Inverse', '[√X†](sqrt-x-dagger.md) (not self-inverse)'),
        ('Also called', 'SX gate'),
    ],
    what_it_does=(
        "√X creates an equal superposition from either basis state, similar to H, but with a "
        "different pattern of complex phases. Applying it twice in a row reproduces a full "
        "bit-flip: \\( (\\sqrt{X})^2 = X \\)."
    ),
    matrix=r"""\[
\sqrt{X} = \frac{1}{2}\begin{pmatrix} 1+i & 1-i \\ 1-i & 1+i \end{pmatrix}
\]""",
    basis_action=(
        "- \\( |0\\rangle \\rightarrow \\dfrac{1}{2}\\big[(1+i)|0\\rangle + (1-i)|1\\rangle\\big] \\)\n"
        "- \\( |1\\rangle \\rightarrow \\dfrac{1}{2}\\big[(1-i)|0\\rangle + (1+i)|1\\rangle\\big] \\)"
    ),
    example=(
        "Two `√X` gates in a row on `q[0]` (starting at \\( |0\\rangle \\)) land exactly on "
        "\\( |1\\rangle \\) - the same result one `X` gate would give in a single step."
    ),
    names=[
        ('OpenQASM 2.0', 'sx q[0];'),
        ('Qiskit', 'circuit.sx[q[0]]'),
        ('Cirq', 'cirq.X(q[0])**0.5'),
        ('Q#', None),
    ],
    related=[
        '[√X†](sqrt-x-dagger.md) - the inverse of √X',
        '[Pauli-X / NOT](pauli-x.md) - (√X)² = X',
    ],
))

# ---------------------------------------------------------------- sqrt X dagger
GATES.append(dict(
    key='sqrt-x-dagger',
    title='√X†',
    image='sqrt-x-dagger.png',
    tile_alt='Square-root-of-X-dagger gate',
    summary=(
        "**√X†** is the inverse of [√X](sqrt-x.md) - applying √X then √X† (in either order) "
        "returns a qubit exactly to its starting state."
    ),
    facts=[
        ('Qubits', '1'),
        ('Parameters', 'None'),
        ('Inverse', '[√X](sqrt-x.md)'),
        ('Also called', 'SX-dagger, adjoint of SX'),
    ],
    what_it_does=(
        "√X† applies the complex-conjugate transpose of √X's matrix, undoing its effect."
    ),
    matrix=r"""\[
\sqrt{X}^\dagger = \frac{1}{2}\begin{pmatrix} 1-i & 1+i \\ 1+i & 1-i \end{pmatrix}
\]""",
    basis_action=(
        "- \\( |0\\rangle \\rightarrow \\dfrac{1}{2}\\big[(1-i)|0\\rangle + (1+i)|1\\rangle\\big] \\)\n"
        "- \\( |1\\rangle \\rightarrow \\dfrac{1}{2}\\big[(1+i)|0\\rangle + (1-i)|1\\rangle\\big] \\)"
    ),
    names=[
        ('OpenQASM 2.0', 'sxdg q[0];'),
        ('Qiskit', 'circuit.sxdg[q[0]]'),
        ('Cirq', 'cirq.X(q[0])**-0.5'),
        ('Q#', None),
    ],
    related=[
        '[√X](sqrt-x.md)',
    ],
))

# ---------------------------------------------------------------- U
GATES.append(dict(
    key='u-gate',
    title='U (general single-qubit gate)',
    image='u-gate.png',
    tile_alt='U gate',
    summary=(
        "**U** is the most general possible single-qubit gate - with the right three angles, "
        "it can reproduce *any* single-qubit unitary, including every other gate on this page."
    ),
    facts=[
        ('Qubits', '1'),
        ('Parameters', '\\( \\theta, \\varphi, \\lambda \\) - three angles, in radians'),
        ('Inverse', 'U(−θ, −λ, −φ)'),
        ('Also called', 'U3 gate'),
    ],
    what_it_does=(
        "U(θ, φ, λ) covers every possible way to rotate and phase-shift a single qubit. "
        "Every gate on this reference page is a special case of U with particular angles plugged in."
    ),
    matrix=r"""\[
U(\theta, \varphi, \lambda) = \begin{pmatrix}
\cos(\theta/2) & -e^{i\lambda}\sin(\theta/2) \\
e^{i\varphi}\sin(\theta/2) & e^{i(\varphi+\lambda)}\cos(\theta/2)
\end{pmatrix}
\]""",
    notes=(
        "Some useful special cases (all exact, no leftover global phase):\n\n"
        "- \\( U(0, 0, \\lambda) = P(\\lambda) \\) - see [P](p-gate.md)\n"
        "- \\( U(\\theta, -\\pi/2, \\pi/2) = RX(\\theta) \\) - see [RX](rx-gate.md)\n"
        "- \\( U(\\theta, 0, 0) = RY(\\theta) \\) - see [RY](ry-gate.md)\n"
        "- \\( U(\\pi, 0, \\pi) = X \\) - see [Pauli-X](pauli-x.md)\n"
        "- \\( U(\\pi/2, 0, \\pi) = H \\) - see [Hadamard](hadamard.md)"
    ),
    example=(
        "`U` with \\( (\\theta,\\varphi,\\lambda) = (\\pi/2, 0, \\pi) \\) on `q[0]` produces "
        "exactly the same state as an `H` gate - a good way to see how U generalizes the "
        "gates you already know."
    ),
    names=[
        ('OpenQASM 2.0', 'u(theta, phi, lambda) q[0];'),
        ('Qiskit', 'circuit.u[theta, phi, lam, q[0]]'),
        ('Cirq', None),
        ('Q#', None),
    ],
    related=[
        '[P](p-gate.md)', '[RX](rx-gate.md)', '[RY](ry-gate.md)', '[Hadamard](hadamard.md)',
    ],
))

# ---------------------------------------------------------------- CNOT
GATES.append(dict(
    key='cnot',
    title='CNOT',
    image='cnot.png',
    tile_alt='CNOT gate',
    summary=(
        "**CNOT** (\"controlled-NOT\") is the most common two-qubit gate: it flips a target "
        "qubit, but only when a control qubit is \\( |1\\rangle \\). It's the standard way to "
        "create entanglement between two qubits."
    ),
    facts=[
        ('Qubits', '2 (one control, one target)'),
        ('Parameters', 'None'),
        ('Inverse', 'Itself (CNOT² = I)'),
        ('Also called', 'CX, controlled-X'),
    ],
    what_it_does=(
        "If the control qubit is \\( |0\\rangle \\), CNOT does nothing. If the control is "
        "\\( |1\\rangle \\), CNOT applies an [X gate](pauli-x.md) to the target. Applied to a "
        "control in superposition, this correlates the two qubits - the essence of entanglement."
    ),
    matrix=r"""\[
\text{CNOT} = \begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&0&1\\
0&0&1&0
\end{pmatrix}
\]""",
    basis_action=(
        "(control first, target second)\n\n"
        "- \\( |00\\rangle \\rightarrow |00\\rangle \\)\n"
        "- \\( |01\\rangle \\rightarrow |01\\rangle \\)\n"
        "- \\( |10\\rangle \\rightarrow |11\\rangle \\)\n"
        "- \\( |11\\rangle \\rightarrow |10\\rangle \\)"
    ),
    example=(
        "On the circuit canvas, CNOT is drawn as a solid dot on the control wire connected by a "
        "vertical line to a circled **+** on the target wire - see "
        "[Multi-qubit gate symbols](../tour/drag-drop/circuit.md#multi-qubit-gate-symbols). "
        "`H` on `q[0]` followed by `CNOT` from `q[0]` to `q[1]` is the standard "
        "[Bell state](../algorithms/bell-states.md) circuit:\n\n"
        "![Bell state circuit: H on q0, CNOT from q0 to q1](../images/circuit/left-align-cnot.png)"
    ),
    names=[
        ('OpenQASM 2.0', 'cx q[0], q[1];'),
        ('Qiskit', 'circuit.cx[q[0], q[1]]'),
        ('Cirq', 'cirq.CNOT(q[0], q[1])'),
        ('Q#', 'CNOT(q[0], q[1]);'),
    ],
    related=[
        '[Toffoli](toffoli.md) - the three-qubit generalization (two controls)',
        '[Control](control.md) - add a standalone control point to build custom controlled gates',
        '[Bell states](../algorithms/bell-states.md)',
    ],
))

# ---------------------------------------------------------------- Toffoli
GATES.append(dict(
    key='toffoli',
    title='Toffoli',
    image='toffoli.png',
    tile_alt='Toffoli gate',
    summary=(
        "The **Toffoli gate** is a doubly-controlled NOT: it flips the target qubit only when "
        "*both* control qubits are \\( |1\\rangle \\). It's the quantum version of a classical "
        "AND gate (the target ends up holding the AND of the two controls, if it started at \\( |0\\rangle \\))."
    ),
    facts=[
        ('Qubits', '3 (two controls, one target)'),
        ('Parameters', 'None'),
        ('Inverse', 'Itself (Toffoli² = I)'),
        ('Also called', 'CCX, CCNOT, doubly-controlled NOT'),
    ],
    what_it_does=(
        "Toffoli acts as the identity on every basis state except the one where both controls "
        "are \\( |1\\rangle \\); there, it flips the target - swapping \\( |110\\rangle \\) with "
        "\\( |111\\rangle \\) (using the convention that the first two qubits are the controls "
        "and the third is the target). Every other basis state is unchanged."
    ),
    basis_action=(
        "(controls first and second, target third)\n\n"
        "- \\( |110\\rangle \\rightarrow |111\\rangle \\)\n"
        "- \\( |111\\rangle \\rightarrow |110\\rangle \\)\n"
        "- every other 3-qubit basis state is left unchanged"
    ),
    notes=(
        "Toffoli's full matrix is 8×8 - identity everywhere except a single 2×2 X block in the "
        "corner covering \\( |110\\rangle \\) and \\( |111\\rangle \\), matching the basis-state "
        "mapping above."
    ),
    example=(
        "With `q[0]` and `q[1]` both set to \\( |1\\rangle \\) (e.g. with two [X](pauli-x.md) "
        "gates) and `q[2]` at \\( |0\\rangle \\), a Toffoli from controls `q[0], q[1]` to target "
        "`q[2]` flips `q[2]` to \\( |1\\rangle \\) - same as classical `AND(1, 1) = 1`."
    ),
    names=[
        ('OpenQASM 2.0', 'ccx q[0], q[1], q[2];'),
        ('Qiskit', 'circuit.ccx[q[0], q[1], q[2]]'),
        ('Cirq', 'cirq.TOFFOLI(q[0], q[1], q[2])'),
        ('Q#', 'CCNOT(q[0], q[1], q[2]);'),
    ],
    related=[
        '[CNOT](cnot.md) - the single-control version',
        '[RCCX](rccx.md) - a cheaper, relative-phase version of Toffoli',
    ],
))

# ---------------------------------------------------------------- SWAP
GATES.append(dict(
    key='swap',
    title='SWAP',
    image='swap.png',
    tile_alt='SWAP gate',
    summary=(
        "The **SWAP gate** exchanges the states of two qubits - whatever `q[0]` held, `q[1]` "
        "now holds, and vice versa."
    ),
    facts=[
        ('Qubits', '2'),
        ('Parameters', 'None'),
        ('Inverse', 'Itself (SWAP² = I)'),
        ('Also called', 'SWAP'),
    ],
    what_it_does=(
        "SWAP leaves \\( |00\\rangle \\) and \\( |11\\rangle \\) unchanged (swapping identical "
        "values does nothing) and exchanges \\( |01\\rangle \\) and \\( |10\\rangle \\). It works "
        "the same way on superpositions and entangled states, not just definite basis states."
    ),
    matrix=r"""\[
\text{SWAP} = \begin{pmatrix}
1&0&0&0\\
0&0&1&0\\
0&1&0&0\\
0&0&0&1
\end{pmatrix}
\]""",
    basis_action=(
        "- \\( |00\\rangle \\rightarrow |00\\rangle \\)\n"
        "- \\( |01\\rangle \\rightarrow |10\\rangle \\)\n"
        "- \\( |10\\rangle \\rightarrow |01\\rangle \\)\n"
        "- \\( |11\\rangle \\rightarrow |11\\rangle \\)"
    ),
    example=(
        "On the circuit canvas, SWAP is drawn as an **✕** mark on each of the two wires it "
        "connects - see [Multi-qubit gate symbols](../tour/drag-drop/circuit.md#multi-qubit-gate-symbols)."
    ),
    names=[
        ('OpenQASM 2.0', 'swap q[0], q[1];'),
        ('Qiskit', 'circuit.swap[q[0], q[1]]'),
        ('Cirq', 'cirq.SWAP(q[0], q[1])'),
        ('Q#', 'SWAP(q[0], q[1]);'),
    ],
    related=[
        '[CNOT](cnot.md)',
    ],
))

# ---------------------------------------------------------------- RXX
GATES.append(dict(
    key='rxx-gate',
    title='RXX',
    image='rxx-gate.png',
    tile_alt='RXX gate',
    summary=(
        "**RXX** is a two-qubit \"Ising coupling\" gate - it entangles two qubits by an amount "
        "that depends continuously on an angle \\( \\theta \\), based on the \\( X \\otimes X \\) interaction."
    ),
    facts=[
        ('Qubits', '2'),
        ('Parameters', '\\( \\theta \\) - coupling angle, in radians'),
        ('Inverse', 'RXX(−θ)'),
        ('Also called', 'XX-rotation, Ising XX coupling gate'),
    ],
    what_it_does=(
        "RXX(θ) is defined as \\( e^{-i\\theta X \\otimes X / 2} \\). It mixes pairs of basis "
        "states that differ in *both* qubits: \\( |00\\rangle \\) with \\( |11\\rangle \\), and "
        "\\( |01\\rangle \\) with \\( |10\\rangle \\)."
    ),
    matrix=r"""\[
RXX(\theta) = \begin{pmatrix}
\cos(\theta/2) & 0 & 0 & -i\sin(\theta/2) \\
0 & \cos(\theta/2) & -i\sin(\theta/2) & 0 \\
0 & -i\sin(\theta/2) & \cos(\theta/2) & 0 \\
-i\sin(\theta/2) & 0 & 0 & \cos(\theta/2)
\end{pmatrix}
\]""",
    basis_action=(
        "- \\( |00\\rangle \\rightarrow \\cos(\\theta/2)|00\\rangle - i\\sin(\\theta/2)|11\\rangle \\)\n"
        "- \\( |01\\rangle \\rightarrow \\cos(\\theta/2)|01\\rangle - i\\sin(\\theta/2)|10\\rangle \\)\n"
        "- \\( |10\\rangle \\rightarrow \\cos(\\theta/2)|10\\rangle - i\\sin(\\theta/2)|01\\rangle \\)\n"
        "- \\( |11\\rangle \\rightarrow \\cos(\\theta/2)|11\\rangle - i\\sin(\\theta/2)|00\\rangle \\)"
    ),
    example=(
        "`RXX` with \\( \\theta = \\pi/2 \\) applied to `q[0], q[1]` (both starting at "
        "\\( |0\\rangle \\)) produces \\( \\dfrac{1}{\\sqrt{2}}(|00\\rangle - i|11\\rangle) \\) - "
        "an entangled state built in a single gate, without a separate [H](hadamard.md) + "
        "[CNOT](cnot.md) pair."
    ),
    names=[
        ('OpenQASM 2.0', 'rxx(theta) q[0], q[1];'),
        ('Qiskit', 'circuit.rxx[theta, q[0], q[1]]'),
        ('Cirq', 'cirq.XXPowGate(exponent=theta / math.pi)(q[0], q[1])'),
        ('Q#', None),
    ],
    related=[
        '[RZZ](rzz-gate.md) - the equivalent coupling gate built from Z⊗Z',
    ],
))

# ---------------------------------------------------------------- RZZ
GATES.append(dict(
    key='rzz-gate',
    title='RZZ',
    image='rzz-gate.png',
    tile_alt='RZZ gate',
    summary=(
        "**RZZ** is the Z-based counterpart of [RXX](rxx-gate.md): a continuously tunable "
        "two-qubit coupling built from the \\( Z \\otimes Z \\) interaction."
    ),
    facts=[
        ('Qubits', '2'),
        ('Parameters', '\\( \\theta \\) - coupling angle, in radians'),
        ('Inverse', 'RZZ(−θ)'),
        ('Also called', 'ZZ-rotation, Ising ZZ coupling gate'),
    ],
    what_it_does=(
        "RZZ(θ) is defined as \\( e^{-i\\theta Z \\otimes Z / 2} \\). Unlike RXX, it never mixes "
        "basis states into each other - it only ever applies a phase, based on whether the two "
        "qubits agree (\\( |00\\rangle, |11\\rangle \\)) or disagree (\\( |01\\rangle, |10\\rangle \\))."
    ),
    matrix=r"""\[
RZZ(\theta) = \mathrm{diag}\left(e^{-i\theta/2},\ e^{i\theta/2},\ e^{i\theta/2},\ e^{-i\theta/2}\right)
\]""",
    basis_action=(
        "- \\( |00\\rangle \\rightarrow e^{-i\\theta/2}\\,|00\\rangle \\)\n"
        "- \\( |01\\rangle \\rightarrow e^{i\\theta/2}\\,|01\\rangle \\)\n"
        "- \\( |10\\rangle \\rightarrow e^{i\\theta/2}\\,|10\\rangle \\)\n"
        "- \\( |11\\rangle \\rightarrow e^{-i\\theta/2}\\,|11\\rangle \\)"
    ),
    example=(
        "Applying `RZZ` to two qubits already in superposition adds a phase that depends on "
        "whether the two qubits' bits match - a building block for algorithms like [QAOA]"
        "(../algorithms/qaoa.md) that encode a cost function into phases."
    ),
    names=[
        ('OpenQASM 2.0', 'rzz(theta) q[0], q[1];'),
        ('Qiskit', 'circuit.rzz[theta, q[0], q[1]]'),
        ('Cirq', 'cirq.ZZPowGate(exponent=theta / math.pi)(q[0], q[1])'),
        ('Q#', None),
    ],
    related=[
        '[RXX](rxx-gate.md)',
        '[QAOA](../algorithms/qaoa.md)',
    ],
))

# ---------------------------------------------------------------- RCCX
GATES.append(dict(
    key='rccx',
    title='RCCX',
    image='rccx.png',
    tile_alt='RCCX gate',
    summary=(
        "**RCCX** (\"relative-phase CCX\", also called the Margolus gate) gives the same "
        "computational-basis result as a [Toffoli](toffoli.md) gate, but can be built from "
        "fewer elementary gates - at the cost of introducing extra phases on some inputs."
    ),
    facts=[
        ('Qubits', '3 (two controls, one target)'),
        ('Parameters', 'None'),
        ('Inverse', 'Itself, on computational basis inputs'),
        ('Also called', 'Margolus gate, simplified Toffoli'),
    ],
    what_it_does=(
        "On every computational basis state, RCCX flips the target exactly when both controls "
        "are \\( |1\\rangle \\) - identical to Toffoli's action. The difference is *not* visible "
        "in the basis-state mapping: RCCX implements this using a cheaper sequence of gates by "
        "allowing a relative phase to appear on some intermediate/superposition inputs, which "
        "Toffoli does not introduce."
    ),
    basis_action=(
        "(controls first and second, target third - identical to Toffoli on computational basis states)\n\n"
        "- \\( |110\\rangle \\rightarrow |111\\rangle \\)\n"
        "- \\( |111\\rangle \\rightarrow |110\\rangle \\)\n"
        "- every other computational basis state is left unchanged"
    ),
    notes=(
        "Because RCCX only *matches* Toffoli on computational basis states - not as an exactly "
        "identical unitary - it's safe to use as a drop-in replacement when its inputs and "
        "outputs are always basis states (e.g. classical logic built from quantum gates), but "
        "it should not be substituted for a true Toffoli inside a larger circuit where the "
        "extra relative phase would affect interference between amplitudes."
    ),
    example=(
        "RCCX is most useful as a cheaper building block inside larger circuits - e.g. "
        "constructing [RC3X](rc3x.md) or other multi-controlled gates - where its relative-phase "
        "caveat doesn't matter because it's immediately uncomputed or only ever touches basis states."
    ),
    names=[
        ('OpenQASM 2.0', 'rccx q[0], q[1], q[2];'),
        ('Qiskit', 'circuit.rccx[q[0], q[1], q[2]]'),
        ('Cirq', None),
        ('Q#', None),
    ],
    related=[
        '[Toffoli](toffoli.md) - the exact (more expensive) version',
        '[RC3X](rc3x.md) - the four-qubit counterpart',
    ],
))

# ---------------------------------------------------------------- RC3X
GATES.append(dict(
    key='rc3x',
    title='RC3X',
    image='rc3x.png',
    tile_alt='RC3X gate',
    summary=(
        "**RC3X** extends [RCCX](rccx.md) to three controls: a cheaper, relative-phase version "
        "of a triply-controlled X gate (C3X) on four qubits."
    ),
    facts=[
        ('Qubits', '4 (three controls, one target)'),
        ('Parameters', 'None'),
        ('Inverse', 'Itself, on computational basis inputs'),
        ('Also called', 'Simplified 3-controlled Toffoli'),
    ],
    what_it_does=(
        "On computational basis states, RC3X flips the target exactly when all three controls "
        "are \\( |1\\rangle \\), matching a true C3X (triply-controlled X) gate. Like RCCX, it "
        "achieves this more cheaply by allowing relative phases on non-basis-state inputs."
    ),
    basis_action=(
        "(three controls first, target last - identical to C3X on computational basis states)\n\n"
        "- \\( |1110\\rangle \\rightarrow |1111\\rangle \\)\n"
        "- \\( |1111\\rangle \\rightarrow |1110\\rangle \\)\n"
        "- every other computational basis state is left unchanged"
    ),
    notes=(
        "Because RC3X needs four qubits, it appears greyed out in the Operations catalog until "
        "your circuit has at least four quantum registers - see the note on the "
        "[Operations](../tour/drag-drop/operations.md#catalog-view) page."
    ),
    names=[
        ('OpenQASM 2.0', 'rc3x q[0], q[1], q[2], q[3];'),
        ('Qiskit', 'circuit.rc3x[q[0], q[1], q[2], q[3]]'),
        ('Cirq', None),
        ('Q#', None),
    ],
    related=[
        '[RCCX](rccx.md)',
        '[Toffoli](toffoli.md)',
    ],
))

# ---------------------------------------------------------------- Measurement
GATES.append(dict(
    key='measurement',
    title='Measurement',
    image='measure.png',
    tile_alt='Measurement gate',
    summary=(
        "**Measurement** reads out a qubit's state as a classical bit - the one operation in a "
        "quantum circuit that isn't reversible."
    ),
    facts=[
        ('Qubits', '1 quantum register + 1 classical register'),
        ('Parameters', 'Which classical bit to store the result in'),
        ('Reversible?', 'No'),
        ('Also called', 'Measure'),
    ],
    what_it_does=(
        "Measurement collapses a qubit's superposition into a definite outcome - \\( 0 \\) or "
        "\\( 1 \\) - with probability given by the squared magnitude of that basis state's "
        "amplitude, and writes the result into a classical bit. Any superposition or "
        "entanglement the qubit had is destroyed by this collapse."
    ),
    example=(
        "Measuring a qubit prepared with [H](hadamard.md) gives `0` or `1` with 50/50 "
        "probability each time you run the circuit - matching the bars shown in "
        "[Probabilities](../tour/visualizations/probabilities.md). Every quantum wire also has a "
        "plain end-of-wire circle showing the default readout point, whether or not you've "
        "placed an explicit measurement - see "
        "[Quantum and classical registers](../tour/drag-drop/circuit.md#quantum-and-classical-registers)."
    ),
    names=[
        ('OpenQASM 2.0', 'measure q[0] -> c[0];'),
        ('Qiskit', 'circuit.measure[q[0], c[0]]'),
        ('Cirq', "cirq.measure(q[0], key='c0')"),
        ('Q#', 'let result = M(q[0]);'),
    ],
    related=[
        '[Reset](reset.md)',
        '[Conditional (if)](conditional.md) - act on a measurement result',
        '[Controls and conditionals](controls-and-conditionals.md)',
    ],
))

# ---------------------------------------------------------------- Reset
GATES.append(dict(
    key='reset',
    title='Reset',
    image='reset.png',
    tile_alt='Reset gate',
    summary=(
        "**Reset** forces a qubit back to \\( |0\\rangle \\), no matter what state it was in - "
        "shown in the catalog with the \\( |0\\rangle \\) ket notation."
    ),
    facts=[
        ('Qubits', '1'),
        ('Parameters', 'None'),
        ('Reversible?', 'No'),
        ('Also called', 'Reset to |0⟩'),
    ],
    what_it_does=(
        "Reset discards whatever state a qubit is in - including superposition or entanglement "
        "- and reinitializes it to \\( |0\\rangle \\). It's a shortcut for \"measure, then flip "
        "back to 0 if the result was 1,\" which is exactly how it's implemented on real hardware."
    ),
    example=(
        "Reset is useful for reusing a qubit partway through a circuit - for example, after its "
        "role in an intermediate step is finished and you want to use it again from a clean "
        "\\( |0\\rangle \\) state."
    ),
    names=[
        ('OpenQASM 2.0', 'reset q[0];'),
        ('Qiskit', 'circuit.reset[q[0]]'),
        ('Cirq', 'cirq.reset(q[0])'),
        ('Q#', 'Reset(q[0]);'),
    ],
    related=[
        '[Measurement](measurement.md)',
    ],
))

# ---------------------------------------------------------------- Barrier
GATES.append(dict(
    key='barrier',
    title='Barrier',
    image='barrier.png',
    tile_alt='Barrier',
    summary=(
        "A **barrier** isn't a quantum operation at all - it's a visual/compiler divider that "
        "marks a point in the circuit that optimizers shouldn't rearrange gates across."
    ),
    facts=[
        ('Qubits', 'Any number (applies across the wires it spans)'),
        ('Parameters', 'None'),
        ('Changes the quantum state?', 'No'),
        ('Also called', 'Barrier'),
    ],
    what_it_does=(
        "Barriers have no effect on the mathematics of a circuit - the statevector, "
        "probabilities, and phases are exactly the same with or without one. They exist purely "
        "to (a) visually separate stages of a circuit for readability, and (b) tell a compiler "
        "or transpiler \"don't reorder or merge gates across this line,\" which matters when "
        "gate order affects real hardware behavior even though it doesn't affect the ideal "
        "simulated math."
    ),
    example=(
        "Placing a barrier after a state-preparation section and before an algorithm's main "
        "loop keeps the two visually and logically distinct, without changing any simulation results."
    ),
    names=[
        ('OpenQASM 2.0', 'barrier q[0], q[1];'),
        ('Qiskit', 'circuit.barrier[q[0], q[1]]'),
        ('Cirq', None),
        ('Q#', None),
    ],
    notes=(
        "Cirq has no direct equivalent instruction - its `Moment` structure organizes timing differently."
    ),
    related=[
        '[Managing registers](../tour/drag-drop/circuit.md#managing-registers)',
    ],
))

# ---------------------------------------------------------------- Control
GATES.append(dict(
    key='control',
    title='Control',
    image='control.png',
    tile_alt='Control point',
    summary=(
        "The **Control** tile is a standalone control point you can drag onto a wire and "
        "connect to another gate - the general-purpose way to build a custom controlled "
        "version of any gate, not just the built-in [CNOT](cnot.md) and [Toffoli](toffoli.md)."
    ),
    facts=[
        ('Qubits', '1 (per control point placed)'),
        ('Parameters', 'None - it takes on whatever gate it\'s connected to'),
        ('Changes the quantum state?', 'Only via the gate it controls'),
        ('Also called', 'Control point'),
    ],
    what_it_does=(
        "Where CNOT and Toffoli are pre-built controlled-X gates, the standalone Control tile "
        "lets you add a control condition to *any* gate - for example, a controlled-Z, a "
        "controlled-H, or a controlled rotation - by placing the control dot on one wire and "
        "connecting it to the gate you want controlled on another wire. The connected gate only "
        "applies when the control qubit is \\( |1\\rangle \\), exactly like the control half of "
        "a CNOT."
    ),
    example=(
        "Dragging a Control point onto `q[0]` and connecting it to a [Z gate](pauli-z.md) on "
        "`q[1]` builds a controlled-Z - a gate not otherwise in the default catalog."
    ),
    related=[
        '[CNOT](cnot.md) - a built-in controlled-X',
        '[Toffoli](toffoli.md) - a built-in, two-control controlled-X',
        '[Controls and conditionals](controls-and-conditionals.md)',
    ],
))

# ---------------------------------------------------------------- Conditional
GATES.append(dict(
    key='conditional',
    title='Conditional (if)',
    image='if-conditional.png',
    tile_alt='If conditional',
    summary=(
        "The **if** tile applies an operation only when a classical condition is true - the "
        "bridge between a measurement result and later quantum operations, based on classical, "
        "not quantum, control."
    ),
    facts=[
        ('Qubits', 'Depends on the operation it wraps'),
        ('Parameters', 'A classical register/bit and the value to compare against'),
        ('Category', 'Classical control flow, not a quantum gate'),
        ('Also called', 'Classically-controlled gate, `c_if`'),
    ],
    what_it_does=(
        "A conditional operation checks the current value of a classical bit (usually set by "
        "an earlier [measurement](measurement.md)) and only applies its attached gate when that "
        "value matches the condition. Unlike [Control](control.md) - which conditions a gate on "
        "a *qubit's* quantum state without collapsing it - a conditional checks an already-"
        "measured, classical value, so there's no superposition involved in the decision itself."
    ),
    example=(
        "Measure `q[0]` into `c[0]`, then apply `X` to `q[1]` conditioned on `c[0] == 1`: "
        "whatever definite value the measurement produced classically decides whether the `X` "
        "runs. This pattern shows up in protocols like quantum teleportation, where a receiver's "
        "correction gates depend on a sender's measurement outcomes."
    ),
    names=[
        ('OpenQASM 2.0', 'if (c[0] == 1) x q[1];'),
        ('Qiskit', 'circuit.x[q[1]].c_if[c, 1]'),
        ('Cirq', "cirq.X(q[1]).with_classical_controls('c0')"),
        ('Q#', 'if (M(q[0]) == One) { X(q[1]); }'),
    ],
    related=[
        '[Measurement](measurement.md)',
        '[Control](control.md) - the quantum-conditioned counterpart',
        '[Controls and conditionals](controls-and-conditionals.md)',
    ],
))

# ---------------------------------------------------------------- Phase disk marker
GATES.append(dict(
    key='phase-disk-marker',
    title='Phase disk marker',
    image='phase-disk-icon.png',
    tile_alt='Phase disk marker tool',
    summary=(
        "The **phase disk** tile isn't a gate either - it's a visualization tool. Clicking it "
        "inserts a snapshot marker on the circuit that displays each qubit's phase at that exact point."
    ),
    facts=[
        ('Qubits', 'All qubits at the chosen point in the circuit'),
        ('Parameters', 'None'),
        ('Changes the quantum state?', 'No'),
        ('Also called', 'Phase disk snapshot'),
    ],
    what_it_does=(
        "Selecting this tool and clicking a point on the circuit inserts a dashed vertical "
        "divider with one small disk per qubit wire, colored to show that qubit's phase at "
        "that moment - using the same Phase color wheel as the "
        "[Q-Sphere](../tour/visualizations/q-sphere.md) and "
        "[Statevector](../tour/visualizations/statevector.md) panels. It's a way to \"freeze\" "
        "and inspect phase information at a specific step, without needing those panels open."
    ),
    example=(
        "See [Phase disks](../tour/visualizations/phase-disks.md) for a full walkthrough, "
        "including how the disk's appearance changes as you add [S](s-gate.md) and "
        "[T](t-gate.md) gates before the snapshot point."
    ),
    related=[
        '[Phase disks](../tour/visualizations/phase-disks.md)',
        '[Phase disks (in-circuit)](../tour/drag-drop/circuit.md#phase-disks-in-circuit)',
    ],
))


if __name__ == '__main__':
    for meta in GATES:
        content = page(meta)
        out_path = os.path.join(OUT_DIR, f"{meta['key']}.md")
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print('wrote', out_path)
