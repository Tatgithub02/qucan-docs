# Cirq

**Cirq** is Google Quantum AI's open-source Python framework for writing, manipulating, and running quantum circuits. It's built with today's noisy, intermediate-scale quantum hardware in mind, giving you fine-grained control over things like qubit layout and gate timing, and it can run circuits on Google's own quantum processors as well as on built-in simulators (including `qsim`, a high-performance wavefunction simulator).

The code panel can also render your circuit as Cirq. Here's the same H + CNOT circuit rendered as Cirq:

![Cirq code view](../../images/code/cirq-bell.png)

```python
import cirq
import math

q = cirq.LineQubit.range(3)
circuit = cirq.Circuit()
circuit.append(cirq.H(q[0]))
circuit.append(cirq.CNOT(q[0], q[1]))
print(circuit)
```

!!! note "Why the parentheses can look like brackets"
    As on the [Qiskit](qiskit.md) page, this site's code font (B612 Mono) draws `(` and `)` in a fairly square, angular style, so calls like `cirq.Circuit()` or `print(circuit)` can look bracketed at a glance. The code is ordinary Cirq with real parentheses; only genuine index brackets, like the `[0]` in `q[0]`, are square brackets.

For the full API reference and guides on running circuits on real hardware or simulators, see the official [Cirq documentation](https://quantumai.google/cirq).

---

Continue to: [Q#](qsharp.md)
