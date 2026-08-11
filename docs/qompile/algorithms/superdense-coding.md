# Superdense coding

Superdense coding lets you send **two classical bits** of information by physically transmitting **only one qubit**. It sounds like it violates information theory, but it doesn't - the trick is that the sender and receiver share an entangled pair *in advance*, and that shared entanglement is what carries the extra capacity.

## Why this exists

A single classical bit can carry exactly one bit of information: it's a 0 or a 1, nothing more. A single qubit, measured on its own, also gives you at most one bit - you measure it, you get 0 or 1. So how could sending one qubit ever deliver two bits?

The answer is that the qubit being sent isn't alone. It's one half of an entangled [Bell state](bell-states.md), and the *pair* has four perfectly distinguishable configurations - the four Bell states. Superdense coding is the protocol that exploits this: the sender steers the shared pair into one of the four Bell states by acting only on **her own qubit**, sends that qubit over, and the receiver identifies which of the four states the pair is in. Four distinguishable outcomes = two bits.

This is the conceptual twin of [quantum teleportation](teleportation.md), just run in reverse: teleportation spends one entangled pair plus two classical bits to move one qubit; superdense coding spends one entangled pair plus one qubit to move two classical bits.

## What you need to know first

- **The four Bell states** - read the [Bell states](bell-states.md) page first. The key facts: there are exactly four of them, they're perfectly distinguishable from each other, and the plus/minus sign difference is invisible to a plain measurement but real.
- **Local gates can move between Bell states** - this is the non-obvious ingredient. If the pair is in \( |\Phi^+\rangle \) and Alice applies a gate to *just her qubit*, the joint state of the *pair* changes:

    | Alice applies (to her qubit only) | Pair becomes |
    |---|---|
    | nothing | \( \lvert\Phi^+\rangle \) |
    | [X](../gates/pauli-x.md) | \( \lvert\Psi^+\rangle \) |
    | [Z](../gates/pauli-z.md) | \( \lvert\Phi^-\rangle \) |
    | X then Z | \( \lvert\Psi^-\rangle \) |

    One qubit's worth of local action selects among four global states. That's the entire engine of the protocol.

## How it works, step by step

Call the sender **Alice** and the receiver **Bob**.

1. **Setup (before any message exists):** someone prepares a Bell pair \( |\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}} \) and gives one qubit to Alice (`q[0]`) and one to Bob (`q[1]`). They can then travel arbitrarily far apart.
2. **Encoding:** Alice decides on her two-bit message \( (z, x) \). She applies **X** to her qubit if \( x = 1 \), then **Z** if \( z = 1 \). Per the table above, the pair is now in one of the four Bell states, one per message.
3. **Transmission:** Alice sends her single qubit to Bob. This is the only thing that travels.
4. **Decoding:** Bob now holds both qubits. He applies a [CNOT](../gates/cnot.md) (Alice's qubit as control) followed by [H](../gates/hadamard.md) on Alice's qubit. This maps each Bell state to a distinct pair of definite bits.
5. **Measurement:** Bob measures both qubits and reads the message directly: `q[0]` gives \( z \), `q[1]` gives \( x \).

## A worked example: sending `11`

Start with the shared pair:

\[ |\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}} \]

**Alice applies X** (because \( x = 1 \)). Her qubit is the first one, so \( |0\rangle \leftrightarrow |1\rangle \) in the first slot:

\[ \frac{|10\rangle + |01\rangle}{\sqrt{2}} = |\Psi^+\rangle \]

**Alice applies Z** (because \( z = 1 \)). Z flips the sign of any term where her qubit is \( |1\rangle \):

\[ \frac{-|10\rangle + |01\rangle}{\sqrt{2}} = |\Psi^-\rangle \]

She sends her qubit to Bob. **Bob applies CNOT** (`q[0]` controls `q[1]`):

\[ \frac{-|11\rangle + |01\rangle}{\sqrt{2}} = \frac{|0\rangle - |1\rangle}{\sqrt{2}} \otimes |1\rangle \]

Notice the second qubit has factored out as a definite \( |1\rangle \) - that's bit \( x = 1 \) recovered. **Bob applies H** to the first qubit, and since \( H\left(\frac{|0\rangle - |1\rangle}{\sqrt{2}}\right) = |1\rangle \):

\[ |1\rangle \otimes |1\rangle = |11\rangle \]

Bob measures `11`. Both bits arrive intact, and only one qubit ever crossed the channel.

The same computation for the other three messages gives `00`, `01`, and `10` - each Bell state lands on exactly one outcome, with certainty. There's no probability involved in a noiseless run; the four outcomes are perfectly distinguishable.

## The circuit

Build it in three blocks on a 2-qubit circuit (or load it from the [Ready algorithms](../tour/drag-drop/operations.md#switching-to-ready-algorithms) panel):

1. **Entangle:** H on `q[0]`, CNOT `q[0]` → `q[1]`
2. **Encode (Alice, on `q[0]` only):** depends on the message
3. **Decode (Bob):** CNOT `q[0]` → `q[1]`, H on `q[0]`, then [measure](../gates/measurement.md) both qubits

=== "Message 00"

    No encoding gates at all. The circuit is: H `q[0]`, CNOT `q[0]`→`q[1]`, CNOT `q[0]`→`q[1]`, H `q[0]`, measure. Output: `00`.

=== "Message 01"

    An **X** on `q[0]` between the two blocks: H `q[0]`, CNOT, **X `q[0]`**, CNOT, H `q[0]`, measure. Output: `01`.

=== "Message 10"

    A **Z** on `q[0]` between the two blocks: H `q[0]`, CNOT, **Z `q[0]`**, CNOT, H `q[0]`, measure. Output: `10`.

=== "Message 11"

    An **X** then a **Z** on `q[0]`: H `q[0]`, CNOT, **X `q[0]`**, **Z `q[0]`**, CNOT, H `q[0]`, measure. Output: `11`.

Good external references for the circuit layout: [Wikipedia: Superdense coding](https://en.wikipedia.org/wiki/Superdense_coding) and [IBM Quantum Learning: Entanglement in action](https://learning.quantum.ibm.com/course/basics-of-quantum-information/entanglement-in-action).

## The Qiskit code

Here's the full protocol for message `11` in standard Qiskit (runnable outside Qompile):

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

message = "11"          # the two bits Alice wants to send, as (z, x)

qc = QuantumCircuit(2, 2)

# Step 1: create the shared Bell pair
qc.h(0)
qc.cx(0, 1)
qc.barrier()

# Step 2: Alice encodes her message on q0 alone
if message[1] == "1":   # x bit
    qc.x(0)
if message[0] == "1":   # z bit
    qc.z(0)
qc.barrier()

# Step 3: Bob decodes with the Bell measurement
qc.cx(0, 1)
qc.h(0)
qc.measure([0, 1], [0, 1])

counts = AerSimulator().run(qc, shots=1024).result().get_counts()
print(counts)
```

Line by line:

- `QuantumCircuit(2, 2)` - two qubits (Alice's and Bob's) and two classical bits to hold the decoded message.
- `qc.h(0)` then `qc.cx(0, 1)` - the standard Bell-pair recipe from the [Bell states](bell-states.md) page. After this, imagine the qubits being separated.
- `qc.barrier()` - purely visual, it draws a dividing line so the three phases of the protocol are easy to see in the circuit diagram. It doesn't change the state.
- The two `if` statements - Alice's encoding. Note she only ever touches qubit 0. Try changing `message` to any of the four values.
- `qc.cx(0, 1)` then `qc.h(0)` - Bob's decoder, which "un-does" the entangling recipe and converts each Bell state into a distinct pair of plain bits.
- The result should be `{'11': 1024}` - every single shot decodes correctly, because the four Bell states are perfectly distinguishable.

!!! note
    Qiskit prints measurement results with qubit 0 on the **right**. For this circuit both conventions happen to agree for `00` and `11`, but if you experiment with `01`/`10`, remember: the right-hand character of the printed string is `q[0]` (the \( z \) bit), the left-hand one is `q[1]` (the \( x \) bit).

## What you'll see

- **[Probabilities](../tour/visualizations/probabilities.md)** - after the full circuit, a single bar at 100% on the outcome matching the encoded message. Place a [phase disk](../tour/visualizations/phase-disks.md) snapshot right after the encoding step instead, and you'll see both qubits still at 50/50 - the message is stored in *which* Bell state the pair is in, not in either qubit alone.
- **[Q-Sphere](../tour/visualizations/q-sphere.md)** - after encoding, two points (an entangled superposition, with phase coloring showing the minus sign for messages `10` and `11`); after decoding, a single point on one basis state.
- **[Statevector](../tour/visualizations/statevector.md)** - after decoding, a single amplitude of 1.0 on the message state, all others zero.
