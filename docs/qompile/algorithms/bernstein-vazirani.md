# Bernstein-Vazirani

Bernstein-Vazirani recovers a **hidden bitstring** in a single query to a function that a classical computer would have to call \( n \) separate times. It uses exactly the same circuit skeleton as [Deutsch-Jozsa](deutsch-jozsa.md) - if you've read that page, this one is a short and satisfying payoff.

## Why this exists

The game: a mystery function hides a secret \( n \)-bit string \( s \). Given any input \( x \), the function returns the **dot product mod 2** of the secret and your input:

\[ f(x) = s \cdot x = (s_0 x_0 \oplus s_1 x_1 \oplus \cdots \oplus s_{n-1} x_{n-1}) \]

In words: look at the positions where *both* \( s \) and \( x \) have a 1, count them, and return whether that count is odd (1) or even (0). Your job is to find \( s \).

Classically the best you can do is probe one bit at a time: query \( x = 100\ldots0 \) to learn \( s \)'s first bit, \( x = 010\ldots0 \) for the second, and so on - \( n \) queries, no shortcuts, because each query returns only one bit and \( s \) contains \( n \) bits of information.

Bernstein-Vazirani reads out the whole string in **one query**. It's a sharper demonstration than Deutsch-Jozsa: not just "which of two categories," but \( n \) full bits of hidden structure extracted at once. It's also the stepping stone to [Simon's algorithm](simons.md), where the gap over classical becomes exponential.

## What you need to know first

Everything here was set up on the Deutsch-Jozsa page - read [What an oracle is](deutsch-jozsa.md#what-an-oracle-is) and [Phase kickback](deutsch-jozsa.md#phase-kickback) first. The one extra ingredient:

- **Dot product mod 2** - just XOR (addition mod 2) applied across the bit positions selected by \( s \). Khan Academy's [XOR primer](https://www.khanacademy.org/computing/computer-science/cryptography/ciphers/a/xor-bitwise-operation) and [modular arithmetic intro](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic) cover the background.

There's also a beautiful fact hiding in this algorithm, worth stating up front: applying a Hadamard to every qubit of a basis state \( |x\rangle \) produces

\[ H^{\otimes n}|x\rangle = \frac{1}{\sqrt{2^n}} \sum_{y} (-1)^{x \cdot y}\,|y\rangle \]

That is, the Hadamard layer converts *bitstrings* into *phase patterns* and back. Bernstein-Vazirani is a direct application: build the phase pattern of \( s \) using the oracle, then let the Hadamard layer convert it back into the bitstring \( s \).

## How it works, step by step

Same skeleton as Deutsch-Jozsa: \( n \) input qubits plus one ancilla.

1. **Prepare the ancilla:** X then H, putting it in \( |-\rangle \) so the oracle stamps phases (phase kickback).
2. **Superpose the inputs:** H on every input qubit.
3. **One oracle call:** every branch \( |x\rangle \) picks up the tag \( (-1)^{s \cdot x} \).
4. **Interfere:** H on every input qubit again.
5. **Measure the input register:** the result is \( s \) itself, every bit of it, with certainty.

## The math

After step 3 the input register holds \( \frac{1}{\sqrt{2^n}} \sum_x (-1)^{s \cdot x} |x\rangle \). But compare that to the boxed identity above: this is *exactly* \( H^{\otimes n}|s\rangle \). And Hadamard is its own inverse (\( H^2 = I \)), so applying the final Hadamard layer simply undoes it:

\[ H^{\otimes n}\left(H^{\otimes n}|s\rangle\right) = |s\rangle \]

The register lands on the basis state \( |s\rangle \) exactly - probability 1, no randomness. The oracle's phase pattern *was* the Hadamard transform of the secret, and the final layer inverts the transform.

## A worked example

Take \( n = 3 \) and secret \( s = 101 \) (so \( s_0 = 1, s_1 = 0, s_2 = 1 \)). The oracle must XOR \( x_0 \oplus x_2 \) into the ancilla, which is just two [CNOTs](../gates/cnot.md): one from `q[0]`, one from `q[2]`, both targeting the ancilla.

Follow one branch to see the tagging: input \( x = 110 \) (\( x_0 = 0, x_1 = 1, x_2 = 1 \)) has \( s \cdot x = (1\cdot0) \oplus (0\cdot1) \oplus (1\cdot1) = 1 \), so branch \( |110\rangle \) gets a minus sign. Do this for all eight branches and the sign pattern spells out the Hadamard transform of \( |101\rangle \); the final H layer collapses it back, and all 1024 shots read `101`.

Notice what the oracle looks like structurally: **one CNOT per 1-bit of the secret**. The algorithm literally reads off which wires the CNOTs hang from - but it does so through the front door, with one function call, without peeking inside the box.

## The circuit

For \( s = 101 \), build on 4 qubits (`q[0]`-`q[2]` inputs, `q[3]` ancilla), or load it from the [Ready algorithms](../tour/drag-drop/operations.md#switching-to-ready-algorithms) panel:

1. X on `q[3]`, then H on `q[3]`
2. H on `q[0]`, `q[1]`, `q[2]`
3. **Oracle:** CNOT `q[0]` → `q[3]`, CNOT `q[2]` → `q[3]`
4. H on `q[0]`, `q[1]`, `q[2]`
5. [Measure](../gates/measurement.md) `q[0]`, `q[1]`, `q[2]`

To hide a different secret, change which input qubits get a CNOT to the ancilla in step 3.

References for the circuit layout: [Wikipedia: Bernstein-Vazirani algorithm](https://en.wikipedia.org/wiki/Bernstein%E2%80%93Vazirani_algorithm) and [IBM Quantum Learning: Quantum query algorithms](https://learning.quantum.ibm.com/course/fundamentals-of-quantum-algorithms/quantum-query-algorithms).

## The Qiskit code

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

s = "101"                  # the secret string
n = len(s)

qc = QuantumCircuit(n + 1, n)

# Step 1: ancilla into |->
qc.x(n)
qc.h(n)

# Step 2: superpose all inputs
qc.h(range(n))
qc.barrier()

# Step 3: the oracle - one CNOT per 1-bit of the secret.
# s is written as s_{n-1} ... s_1 s_0, so read it right to left.
for i, bit in enumerate(reversed(s)):
    if bit == "1":
        qc.cx(i, n)
qc.barrier()

# Step 4: interfere
qc.h(range(n))

# Step 5: read out the secret
qc.measure(range(n), range(n))

counts = AerSimulator().run(qc, shots=1024).result().get_counts()
print(counts)
```

Line by line:

- `s = "101"` - change this to any bitstring; the rest of the code adapts automatically.
- The `reversed(s)` in the oracle loop handles bit ordering: Qiskit's qubit 0 is the *rightmost* character of a printed bitstring, so the string is read right to left when wiring CNOTs.
- `qc.measure(range(n), range(n))` - only the input register is measured; the ancilla did its phase-kickback job and ends unentangled in \( |-\rangle \).
- Output: `{'101': 1024}`. One query, every bit of the secret, every shot.

## What you'll see

- **[Probabilities](../tour/visualizations/probabilities.md)** - a single bar at 100% sitting exactly on the secret string.
- **[Q-Sphere](../tour/visualizations/q-sphere.md)** - pause after the oracle: all eight branches present with equal size, and the phase coloring spells out the \( (-1)^{s \cdot x} \) pattern; after the final Hadamards, one point on \( |s\rangle \).
- **[Statevector](../tour/visualizations/statevector.md)** - after the oracle, amplitudes of equal magnitude with signs alternating in the secret's pattern; at the end, a single 1.0 amplitude on \( |s\rangle \).
