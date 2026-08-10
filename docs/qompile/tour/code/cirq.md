# Cirq

The code panel can also render your circuit as Cirq. Here's the same H + CNOT circuit rendered as Cirq:

![Cirq code view](../../images/code/cirq-bell.png)

```python
import cirq
import math

q = cirq.LineQubit.range[3]
circuit = cirq.Circuit[]
circuit.append[cirq.H[q[0]]]
circuit.append[cirq.CNOT[q[0], q[1]]]
print[circuit]
```

!!! note "Square brackets, not parentheses"
    As with the [Qiskit](qiskit.md) view, Qompile's Cirq output uses square brackets for calls (e.g. `cirq.Circuit[]`, `print[circuit]`) rather than the parentheses used in standard Cirq (`cirq.Circuit()`, `print(circuit)`). Convert brackets to parentheses if running this code outside Qompile.

---

Continue to: [Q#](qsharp.md)
