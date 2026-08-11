# Ready algorithms

**Ready algorithms** is the second tab of the [Operations](../tour/drag-drop/operations.md#switching-to-ready-algorithms) panel, a list of well-known quantum algorithms as prebuilt circuits you can load directly onto the canvas instead of assembling them gate by gate. Each one below has its own page with what the algorithm does, its circuit, the code across all four supported languages, and what to expect in the visualizations.

## Two ideas behind these algorithms

Almost everything on this list draws its power from one or both of two quantum effects. Here's the plain-language version of each:

- **Superposition** - a qubit doesn't have to be a definite `0` or `1`. It can exist in a blend of both at once, and it only settles on one answer at the moment you measure it. Algorithms use this to hold many candidate answers in the same register at the same time, then nudge the blend so the *right* answer is the one you're most likely to measure.
- **Entanglement** - two or more qubits can become linked so their measurement outcomes are correlated: measure one and you instantly know something about the other, even though neither had a definite value beforehand. [Bell states](bell-states.md) are the simplest example, and the two communication protocols below run entirely on this effect.

Neither is magic on its own. The art of a quantum algorithm is choreographing superposition and entanglement so that wrong answers cancel out and right answers reinforce, a pattern you'll see repeated on every page in this section.

## Entanglement and communication

Small, foundational circuits that show what entanglement makes possible between two parties.

- [Bell states](bell-states.md) - the simplest entangled state, the building block the other two protocols below rely on
- [Superdense coding](superdense-coding.md) - send two classical bits by only sending one qubit
- [Quantum teleportation](teleportation.md) - transmit a qubit's exact state using entanglement plus two classical bits

## Query algorithms

Algorithms that answer a question about a hidden function using far fewer queries than any classical approach could.

- [Deutsch-Jozsa](deutsch-jozsa.md) - decide if a function is constant or balanced in a single query
- [Bernstein-Vazirani](bernstein-vazirani.md) - recover a hidden bitstring in a single query
- [Simon's](simons.md) - find a hidden XOR-mask period, exponentially faster than any classical method
- [Grover's](grovers.md) - search an unsorted list quadratically faster than any classical method

## Optimization, simulation, and factoring

More advanced algorithms, several of them designed to make the most of today's noisy, limited-qubit hardware.

- [QAOA](qaoa.md) - Quantum Approximate Optimization Algorithm, for combinatorial optimization problems
- [QPE](qpe.md) - Quantum Phase Estimation, a subroutine other algorithms (including Shor's) build on
- [Shor's](shors.md) - factor large numbers exponentially faster than the best known classical algorithm
- [VQE](vqe.md) - Variational Quantum Eigensolver, for estimating a molecule or system's lowest energy state

!!! note
    These are teaching-sized versions of each algorithm, meant to show the circuit structure and what the visualizations reveal, not production-scale implementations for cracking real encryption or simulating large molecules.
