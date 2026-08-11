# Quantum teleportation

Quantum teleportation transmits the **exact quantum state** of a qubit from one place to another without physically sending the qubit itself. It consumes one pre-shared entangled pair and two classical bits, and despite the name, nothing travels faster than light - the protocol can't complete until the classical bits arrive by ordinary means.

## Why this exists

Suppose Alice holds a qubit in some state \( |\psi\rangle = \alpha|0\rangle + \beta|1\rangle \) and wants Bob to have it. Two obvious ideas fail:

- **"Just measure it and tell Bob the result."** Measuring collapses the state to a plain 0 or 1. The amplitudes \( \alpha \) and \( \beta \) - the actual information - are destroyed, and one measurement of one copy can never reveal them.
- **"Just copy it and send the copy."** Impossible. The **no-cloning theorem** says no quantum operation can duplicate an arbitrary unknown state. (The one-line reason: quantum operations are linear, and a machine that maps \( |\psi\rangle \mapsto |\psi\rangle|\psi\rangle \) for every \( |\psi\rangle \) would have to be quadratic in the amplitudes. No such linear machine exists.)

Teleportation is the workaround. It moves the state without measuring it directly and without copying it - the original is necessarily destroyed in the process, which is exactly what no-cloning demands. This isn't just a party trick: teleportation is the basic subroutine behind quantum repeaters, networked quantum computers, and many error-correction schemes.

## What you need to know first

- **Bell states** - the protocol runs on a shared \( |\Phi^+\rangle \) pair; see [Bell states](bell-states.md).
- **What \( \alpha \) and \( \beta \) are** - a general qubit state is \( \alpha|0\rangle + \beta|1\rangle \) where \( \alpha, \beta \) are complex numbers with \( |\alpha|^2 + |\beta|^2 = 1 \). \( |\alpha|^2 \) is the probability of measuring 0, \( |\beta|^2 \) of measuring 1. If complex numbers are rusty, Khan Academy's [complex numbers unit](https://www.khanacademy.org/math/algebra-home/alg-complex-numbers) covers everything needed here.
- **Classically controlled gates** - the last step applies gates *conditioned on measurement results*. Qompile supports this directly; see [Controls and conditionals](../gates/controls-and-conditionals.md) and the [Conditional (if)](../gates/conditional.md) page.

## How it works, step by step

Three qubits: `q[0]` is Alice's message qubit in the unknown state \( |\psi\rangle \), and `q[1]` (Alice's) + `q[2]` (Bob's) form a shared Bell pair.

1. **Share entanglement:** create \( |\Phi^+\rangle \) between `q[1]` and `q[2]` (H on `q[1]`, CNOT `q[1]` → `q[2]`). Bob takes `q[2]` far away.
2. **Bell measurement:** Alice entangles her message qubit with her half of the pair - CNOT `q[0]` → `q[1]`, then H on `q[0]` - and measures both of her qubits. She gets two ordinary classical bits \( (m_0, m_1) \), each 0 or 1 with equal probability.
3. **Send two classical bits:** Alice sends \( m_0, m_1 \) to Bob over any classical channel (phone, internet, carrier pigeon).
4. **Correction:** Bob applies [X](../gates/pauli-x.md) to his qubit if \( m_1 = 1 \), then [Z](../gates/pauli-z.md) if \( m_0 = 1 \). His qubit is now in *exactly* the state \( |\psi\rangle \). Alice's original, meanwhile, was destroyed by her measurement - the state moved, it wasn't copied.

Two things worth stressing:

- **No faster-than-light communication.** Until the classical bits arrive, Bob's qubit looks completely random to him. The entanglement alone carries no usable message.
- **The state is never learned.** Nobody ever finds out what \( \alpha \) and \( \beta \) were. The protocol moves the state blindly, which is the only way no-cloning allows.

## The math

Write the full three-qubit state before Alice's measurement. Starting point:

\[ |\psi\rangle_0 \otimes |\Phi^+\rangle_{12} = (\alpha|0\rangle + \beta|1\rangle) \otimes \frac{|00\rangle + |11\rangle}{\sqrt{2}} \]

Apply CNOT `q[0]` → `q[1]`, then H on `q[0]`, expand, and group the terms by what Alice's two qubits look like. The algebra (worth doing once by hand) lands on:

\[
\frac{1}{2}\Big[\,
|00\rangle\,(\alpha|0\rangle + \beta|1\rangle) +
|01\rangle\,(\alpha|1\rangle + \beta|0\rangle) +
|10\rangle\,(\alpha|0\rangle - \beta|1\rangle) +
|11\rangle\,(\alpha|1\rangle - \beta|0\rangle)
\,\Big]
\]

Read this line carefully - it's the whole protocol in one equation. Whatever pair of bits Alice measures, Bob's qubit (the right-hand factor) is *almost* \( |\psi\rangle \), off by at most a bit flip and/or a sign flip:

| Alice measures \( (m_0, m_1) \) | Bob holds | Bob's fix |
|---|---|---|
| 00 | \( \alpha\lvert 0\rangle + \beta\lvert 1\rangle \) | nothing |
| 01 | \( \alpha\lvert 1\rangle + \beta\lvert 0\rangle \) | X |
| 10 | \( \alpha\lvert 0\rangle - \beta\lvert 1\rangle \) | Z |
| 11 | \( \alpha\lvert 1\rangle - \beta\lvert 0\rangle \) | X then Z |

Each outcome happens with probability \( \frac{1}{4} \) regardless of \( \alpha, \beta \) - which is why the measurement results leak nothing about the state.

## A worked example

Give the message qubit a concrete, recognizable state: apply [RY](../gates/ry-gate.md)(\( \pi/3 \)) to `q[0]`, producing

\[ |\psi\rangle = \cos\tfrac{\pi}{6}|0\rangle + \sin\tfrac{\pi}{6}|1\rangle \approx 0.866\,|0\rangle + 0.5\,|1\rangle \]

so \( |\psi\rangle \) measures 0 with probability 75% and 1 with probability 25%. Run the full protocol, then measure Bob's qubit `q[2]` over many shots: it shows the same 75/25 split, no matter which of the four outcomes Alice's measurement produced along the way. The 75/25 fingerprint has moved from `q[0]` to `q[2]`.

## The circuit

Build on 3 qubits (or load it from the [Ready algorithms](../tour/drag-drop/operations.md#switching-to-ready-algorithms) panel):

1. **Prepare the message:** RY(\( \pi/3 \)) on `q[0]` (any state works; this one is easy to recognize)
2. **Share the pair:** H on `q[1]`, CNOT `q[1]` → `q[2]`
3. **Bell measurement:** CNOT `q[0]` → `q[1]`, H on `q[0]`, [measure](../gates/measurement.md) `q[0]` → `c0` and `q[1]` → `c1`
4. **Corrections:** X on `q[2]` [conditioned](../gates/conditional.md) on `c1 = 1`, then Z on `q[2]` conditioned on `c0 = 1`
5. **Verify:** measure `q[2]`

References for the circuit layout: [Wikipedia: Quantum teleportation](https://en.wikipedia.org/wiki/Quantum_teleportation) and [IBM Quantum Learning: Entanglement in action](https://learning.quantum.ibm.com/course/basics-of-quantum-information/entanglement-in-action).

## The Qiskit code

```python
from math import pi
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(3, 3)

# Step 1: prepare the message state on q0 (75% |0>, 25% |1>)
qc.ry(pi / 3, 0)
qc.barrier()

# Step 2: Bell pair between q1 (Alice) and q2 (Bob)
qc.h(1)
qc.cx(1, 2)
qc.barrier()

# Step 3: Alice's Bell measurement on q0 and q1
qc.cx(0, 1)
qc.h(0)
qc.measure(0, 0)
qc.measure(1, 1)

# Step 4: Bob's corrections, conditioned on Alice's classical bits
with qc.if_test((qc.clbits[1], 1)):
    qc.x(2)
with qc.if_test((qc.clbits[0], 1)):
    qc.z(2)

# Step 5: check what arrived
qc.measure(2, 2)

counts = AerSimulator().run(qc, shots=4096).result().get_counts()
print(counts)
```

Line by line:

- `qc.ry(pi / 3, 0)` - prepares the recognizable 75/25 message state. Replace this with any gates you like; the protocol doesn't care what the state is.
- `qc.h(1)`, `qc.cx(1, 2)` - the shared Bell pair. In a real deployment this happens ahead of time and the qubits are then separated.
- `qc.cx(0, 1)`, `qc.h(0)`, two `measure` calls - Alice's Bell measurement. This is the decoder from [superdense coding](superdense-coding.md) run on the message-plus-pair; it projects her two qubits and produces the two classical bits.
- The `with qc.if_test(...)` blocks - Bob's classically controlled corrections. This is real feed-forward: the gate only fires when the matching classical bit came out 1.
- Reading the output: Qiskit prints bits as `c2 c1 c0` (leftmost = `q[2]`, Bob's verification bit). Summing over Alice's bits, the left character should be `0` about 75% of the time and `1` about 25% of the time - the message state's fingerprint, teleported.

## What you'll see

- **[Probabilities](../tour/visualizations/probabilities.md)** - all eight outcomes appear, but grouped by Bob's bit they reproduce the message's 75/25 split, evenly spread across Alice's four equally likely outcomes.
- **[Phase disks](../tour/visualizations/phase-disks.md)** - drop a snapshot after step 2 and `q[0]` shows the lopsided message state while `q[1]`/`q[2]` sit at 50/50; after the corrections, the lopsided disk has moved to `q[2]`.
- **[Statevector](../tour/visualizations/statevector.md)** - before Alice measures, eight amplitudes; the grouped structure of the boxed equation above is directly visible in which amplitudes share values.
