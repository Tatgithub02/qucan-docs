# Qiskit

The code panel can also render your circuit as Qiskit. Here's the same H + CNOT circuit shown in [OpenQASM](openqasm.md) rendered as Qiskit:

![Qiskit code view](../../images/code/qiskit-bell.png)

```python
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister[3, 'q']
creg_c = ClassicalRegister[3, 'c']
circuit = QuantumCircuit[qreg_q, creg_c]

circuit.h[qreg_q[0]]
circuit.cx[qreg_q[0], qreg_q[1]]
```

!!! note "Square brackets, not parentheses"
    Qompile's Qiskit view uses square brackets for constructor and method calls (e.g. `circuit.h[qreg_q[0]]`), rather than the parentheses you'd normally see in hand-written Qiskit (`circuit.h(qreg_q[0])`). This is confirmed to be how Qompile renders it - if you copy this code to run outside Qompile, you may need to convert brackets to parentheses first.

---

Continue to: [Cirq](cirq.md) · [Q#](qsharp.md)
