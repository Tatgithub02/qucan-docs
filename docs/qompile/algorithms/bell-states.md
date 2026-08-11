# Bell states

A **Bell state** is the simplest example of quantum entanglement - a two-qubit state where measuring one qubit instantly determines the outcome of the other. There are four of them, and all four are built from the same two gates: a **Hadamard** to create superposition, followed by a **CNOT** to entangle the qubits. An **X** gate or two placed in front steers the circuit to one specific Bell state out of the four.

They are worth knowing well: [Superdense coding](superdense-coding.md) and [Quantum teleportation](teleportation.md) both begin by sharing a Bell state between two parties.

## The four states

Throughout this page the left digit is `q[0]` and the right digit is `q[1]`.

- \( |\Phi^+\rangle = \dfrac{|00\rangle + |11\rangle}{\sqrt{2}} \) - the qubits always **agree**
- \( |\Phi^-\rangle = \dfrac{|00\rangle - |11\rangle}{\sqrt{2}} \) - agree, with a relative minus sign
- \( |\Psi^+\rangle = \dfrac{|01\rangle + |10\rangle}{\sqrt{2}} \) - the qubits always **disagree**
- \( |\Psi^-\rangle = \dfrac{|01\rangle - |10\rangle}{\sqrt{2}} \) - disagree, with a relative minus sign

!!! note "How to read the notation"
    \( |00\rangle \) is "ket" notation for "both qubits read 0". The number in front of each ket is its **amplitude**, and squaring an amplitude gives the probability of measuring that outcome. In \( |\Phi^+\rangle \), each amplitude is \( \tfrac{1}{\sqrt{2}} \approx 0.707 \), so each outcome has probability \( 0.707^2 = 50\% \), and the two probabilities sum to 1. The minus sign in \( |\Phi^-\rangle \) and \( |\Psi^-\rangle \) is a **relative phase**: it doesn't change the measurement probabilities on its own, but it makes the state behave differently once more gates act on it, which is exactly what protocols like superdense coding exploit.

## Step by step: building \( |\Phi^+\rangle \)

1. Both qubits start at \( |0\rangle \), so the joint state is \( |00\rangle \).
2. **H on `q[0]`** puts the first qubit in an equal superposition: \( \tfrac{1}{\sqrt{2}}(|00\rangle + |10\rangle) \). `q[0]` is now 0 and 1 at once; `q[1]` is untouched.
3. **CNOT (control `q[0]`, target `q[1]`)** flips `q[1]` only in the part of the state where `q[0]` is 1: \( \tfrac{1}{\sqrt{2}}(|00\rangle + |11\rangle) \).

That final state is \( |\Phi^+\rangle \). Neither qubit has a definite value on its own, but the two are now guaranteed to match when measured - that guarantee is the entanglement.

## One recipe, four states

The other three Bell states use the exact same H + CNOT core. The only difference is an **X** gate (a bit flip) on one or both qubits *before* the core, which changes what state the recipe starts from and therefore where it ends up.

See [Build your circuit with code](../tour/code/openqasm.md) for why parentheses in the Qiskit and Cirq code below can look a little square in this site's code font.

=== "|Φ+⟩"

    ![Bell state circuit: H on q0, CNOT from q0 to q1](../images/circuit/left-align-cnot.png)

    Just **H** then **CNOT**, the base pattern, as derived step by step above.

    \( \tfrac{1}{\sqrt{2}}(|00\rangle + |11\rangle) \)

    === "OpenQASM"

        ```qasm
        OPENQASM 2.0;
        include "qelib1.inc";

        qreg q[3];
        creg c[3];

        h q[0];
        cx q[0], q[1];
        ```

    === "Qiskit"

        ```python
        from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
        from numpy import pi

        qreg_q = QuantumRegister(3, 'q')
        creg_c = ClassicalRegister(3, 'c')
        circuit = QuantumCircuit(qreg_q, creg_c)

        circuit.h(qreg_q[0])
        circuit.cx(qreg_q[0], qreg_q[1])
        ```

    === "Cirq"

        ```python
        import cirq
        import math

        q = cirq.LineQubit.range(3)
        circuit = cirq.Circuit()
        circuit.append(cirq.H(q[0]))
        circuit.append(cirq.CNOT(q[0], q[1]))
        print(circuit)
        ```

    === "Q#"

        ```qsharp
        namespace QompileCircuit {
            open Microsoft.Quantum.Canon;
            open Microsoft.Quantum.Intrinsic;
            open Microsoft.Quantum.Math;
            open Microsoft.Quantum.Convert;

            operation Circuit() : Result[] {
                use q = Qubit[3];
                mutable c = [Zero, size = 3];

                H(q[0]);
                CNOT(q[0], q[1]);

                ResetAll(q);
                return c;
            }
        }
        ```

=== "|Φ-⟩"

    <!-- Screenshot to add: X on q0, then H on q0, then CNOT from q0 to q1 -->

    An **X on `q[0]`** before the core flips `q[0]` to \( |1\rangle \) first. H acting on \( |1\rangle \) produces \( \tfrac{1}{\sqrt{2}}(|0\rangle - |1\rangle) \) instead of a plus, and that minus sign carries through the CNOT.

    \( \tfrac{1}{\sqrt{2}}(|00\rangle - |11\rangle) \)

    === "OpenQASM"

        ```qasm
        OPENQASM 2.0;
        include "qelib1.inc";

        qreg q[3];
        creg c[3];

        x q[0];
        h q[0];
        cx q[0], q[1];
        ```

    === "Qiskit"

        ```python
        from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
        from numpy import pi

        qreg_q = QuantumRegister(3, 'q')
        creg_c = ClassicalRegister(3, 'c')
        circuit = QuantumCircuit(qreg_q, creg_c)

        circuit.x(qreg_q[0])
        circuit.h(qreg_q[0])
        circuit.cx(qreg_q[0], qreg_q[1])
        ```

    === "Cirq"

        ```python
        import cirq
        import math

        q = cirq.LineQubit.range(3)
        circuit = cirq.Circuit()
        circuit.append(cirq.X(q[0]))
        circuit.append(cirq.H(q[0]))
        circuit.append(cirq.CNOT(q[0], q[1]))
        print(circuit)
        ```

    === "Q#"

        ```qsharp
        namespace QompileCircuit {
            open Microsoft.Quantum.Canon;
            open Microsoft.Quantum.Intrinsic;
            open Microsoft.Quantum.Math;
            open Microsoft.Quantum.Convert;

            operation Circuit() : Result[] {
                use q = Qubit[3];
                mutable c = [Zero, size = 3];

                X(q[0]);
                H(q[0]);
                CNOT(q[0], q[1]);

                ResetAll(q);
                return c;
            }
        }
        ```

=== "|Ψ+⟩"

    <!-- Screenshot to add: X on q1, then H on q0, then CNOT from q0 to q1 -->

    An **X on `q[1]`** before the core starts the pair at \( |01\rangle \) instead of \( |00\rangle \), so the CNOT ends up correlating opposite values: the outcomes become `01` and `10` instead of `00` and `11`.

    \( \tfrac{1}{\sqrt{2}}(|01\rangle + |10\rangle) \)

    === "OpenQASM"

        ```qasm
        OPENQASM 2.0;
        include "qelib1.inc";

        qreg q[3];
        creg c[3];

        x q[1];
        h q[0];
        cx q[0], q[1];
        ```

    === "Qiskit"

        ```python
        from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
        from numpy import pi

        qreg_q = QuantumRegister(3, 'q')
        creg_c = ClassicalRegister(3, 'c')
        circuit = QuantumCircuit(qreg_q, creg_c)

        circuit.x(qreg_q[1])
        circuit.h(qreg_q[0])
        circuit.cx(qreg_q[0], qreg_q[1])
        ```

    === "Cirq"

        ```python
        import cirq
        import math

        q = cirq.LineQubit.range(3)
        circuit = cirq.Circuit()
        circuit.append(cirq.X(q[1]))
        circuit.append(cirq.H(q[0]))
        circuit.append(cirq.CNOT(q[0], q[1]))
        print(circuit)
        ```

    === "Q#"

        ```qsharp
        namespace QompileCircuit {
            open Microsoft.Quantum.Canon;
            open Microsoft.Quantum.Intrinsic;
            open Microsoft.Quantum.Math;
            open Microsoft.Quantum.Convert;

            operation Circuit() : Result[] {
                use q = Qubit[3];
                mutable c = [Zero, size = 3];

                X(q[1]);
                H(q[0]);
                CNOT(q[0], q[1]);

                ResetAll(q);
                return c;
            }
        }
        ```

=== "|Ψ-⟩"

    <!-- Screenshot to add: X on q0 and X on q1, then H on q0, then CNOT from q0 to q1 -->

    An **X on both qubits** combines the two effects: the pair starts at \( |11\rangle \), giving both the swapped correlation (`01`/`10`) and the minus sign.

    \( \tfrac{1}{\sqrt{2}}(|01\rangle - |10\rangle) \)

    === "OpenQASM"

        ```qasm
        OPENQASM 2.0;
        include "qelib1.inc";

        qreg q[3];
        creg c[3];

        x q[0];
        x q[1];
        h q[0];
        cx q[0], q[1];
        ```

    === "Qiskit"

        ```python
        from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
        from numpy import pi

        qreg_q = QuantumRegister(3, 'q')
        creg_c = ClassicalRegister(3, 'c')
        circuit = QuantumCircuit(qreg_q, creg_c)

        circuit.x(qreg_q[0])
        circuit.x(qreg_q[1])
        circuit.h(qreg_q[0])
        circuit.cx(qreg_q[0], qreg_q[1])
        ```

    === "Cirq"

        ```python
        import cirq
        import math

        q = cirq.LineQubit.range(3)
        circuit = cirq.Circuit()
        circuit.append(cirq.X(q[0]))
        circuit.append(cirq.X(q[1]))
        circuit.append(cirq.H(q[0]))
        circuit.append(cirq.CNOT(q[0], q[1]))
        print(circuit)
        ```

    === "Q#"

        ```qsharp
        namespace QompileCircuit {
            open Microsoft.Quantum.Canon;
            open Microsoft.Quantum.Intrinsic;
            open Microsoft.Quantum.Math;
            open Microsoft.Quantum.Convert;

            operation Circuit() : Result[] {
                use q = Qubit[3];
                mutable c = [Zero, size = 3];

                X(q[0]);
                X(q[1]);
                H(q[0]);
                CNOT(q[0], q[1]);

                ResetAll(q);
                return c;
            }
        }
        ```

## What you'll see

All four Bell states look the same in the probability view and only reveal their differences in the phase-aware views:

- **[Probabilities](../tour/visualizations/probabilities.md)** - two equal bars at 50% each. For \( |\Phi^\pm\rangle \) the bars sit on `00` and `11`; for \( |\Psi^\pm\rangle \) they sit on `01` and `10`.
- **[Q-Sphere](../tour/visualizations/q-sphere.md)** - two points, one per basis state in the superposition. For the minus states, the two points show different phase colors, which is how the Q-Sphere distinguishes \( |\Phi^+\rangle \) from \( |\Phi^-\rangle \).
- **[Statevector](../tour/visualizations/statevector.md)** - two non-zero amplitudes of equal magnitude (≈0.707). For the minus states, one of the two amplitudes is negative.
