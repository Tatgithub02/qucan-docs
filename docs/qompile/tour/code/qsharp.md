# Q#

The code panel can also render your circuit as Q#. Here's the same H + CNOT circuit rendered as Q#:

![Q# code view](../../images/code/qsharp-bell.png)

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

Unlike the [Qiskit](qiskit.md) and [Cirq](cirq.md) views, Qompile's Q# output uses standard Q# syntax - parentheses for function calls (`H(q[0])`) and square brackets only where Q# itself uses them (array types and indexing, e.g. `Qubit[3]`, `q[0]`).
