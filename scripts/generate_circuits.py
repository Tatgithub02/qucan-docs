"""Generate circuit diagram PNGs for all algorithm pages using Qiskit's mpl drawer."""

from pathlib import Path
from qiskit import QuantumCircuit
from numpy import pi

OUT = Path(__file__).resolve().parent.parent / "docs" / "qompile" / "algorithms" / "images"
OUT.mkdir(parents=True, exist_ok=True)

STYLE = {
    "backgroundcolor": "#000314",
    "textcolor": "#FFFFFF",
    "subtextcolor": "#AAAAAA",
    "linecolor": "#FFFFFF",
    "creglinecolor": "#AAAAAA",
    "gatetextcolor": "#FFFFFF",
    "gatefacecolor": "#1a1a3e",
    "barrierfacecolor": "#555555",
    "edgecolor": "#FFFFFF",
}
DRAW_KW = dict(output="mpl", style=STYLE)


def save(qc: QuantumCircuit, name: str) -> None:
    fig = qc.draw(**DRAW_KW)
    fig.savefig(OUT / f"{name}.png", dpi=150, bbox_inches="tight",
                facecolor="#000314", edgecolor="none")
    print(f"  saved {name}.png")
    import matplotlib.pyplot as plt
    plt.close(fig)


# --- Bell states -----------------------------------------------------------

def bell_phi_plus():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    save(qc, "bell-phi-plus")

def bell_phi_minus():
    qc = QuantumCircuit(2)
    qc.z(0)
    qc.h(0)
    qc.cx(0, 1)
    save(qc, "bell-phi-minus")

def bell_psi_plus():
    qc = QuantumCircuit(2)
    qc.x(1)
    qc.h(0)
    qc.cx(0, 1)
    save(qc, "bell-psi-plus")

def bell_psi_minus():
    qc = QuantumCircuit(2)
    qc.x(0)
    qc.x(1)
    qc.h(0)
    qc.cx(0, 1)
    save(qc, "bell-psi-minus")


# --- Superdense coding (message 11) ----------------------------------------

def superdense_coding():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.barrier(label="share")
    qc.x(0)
    qc.z(0)
    qc.barrier(label="encode")
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [0, 1])
    save(qc, "superdense-coding")


# --- Teleportation ----------------------------------------------------------

def teleportation():
    qc = QuantumCircuit(3, 2)
    qc.ry(pi / 3, 0)
    qc.barrier(label="msg")
    qc.h(1)
    qc.cx(1, 2)
    qc.barrier(label="bell pair")
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [0, 1])
    qc.barrier(label="correct")
    qc.cx(1, 2)
    qc.cz(0, 2)
    save(qc, "teleportation")


# --- Deutsch-Jozsa (balanced oracle, n=2) -----------------------------------

def deutsch_jozsa():
    qc = QuantumCircuit(3, 2)
    qc.x(2)
    qc.barrier()
    qc.h([0, 1, 2])
    qc.barrier(label="oracle")
    qc.cx(0, 2)
    qc.cx(1, 2)
    qc.barrier()
    qc.h([0, 1])
    qc.measure([0, 1], [0, 1])
    save(qc, "deutsch-jozsa")


# --- Bernstein-Vazirani (s = 101) -------------------------------------------

def bernstein_vazirani():
    qc = QuantumCircuit(4, 3)
    qc.x(3)
    qc.barrier()
    qc.h([0, 1, 2, 3])
    qc.barrier(label="oracle")
    qc.cx(0, 3)
    qc.cx(2, 3)
    qc.barrier()
    qc.h([0, 1, 2])
    qc.measure([0, 1, 2], [0, 1, 2])
    save(qc, "bernstein-vazirani")


# --- Simon's (n=2, s=11) ---------------------------------------------------

def simons():
    qc = QuantumCircuit(4, 2)
    qc.h([0, 1])
    qc.barrier(label="oracle")
    qc.cx(0, 2)
    qc.cx(1, 3)
    qc.cx(0, 3)
    qc.barrier()
    qc.h([0, 1])
    qc.measure([0, 1], [0, 1])
    save(qc, "simons")


# --- Grover's (N=4, winner |11>) -------------------------------------------

def grovers():
    qc = QuantumCircuit(2, 2)
    qc.h([0, 1])
    qc.barrier(label="oracle")
    qc.cz(0, 1)
    qc.barrier(label="diffuser")
    qc.h([0, 1])
    qc.z([0, 1])
    qc.cz(0, 1)
    qc.h([0, 1])
    qc.measure([0, 1], [0, 1])
    save(qc, "grovers")


# --- QAOA (triangle MaxCut, p=1) -------------------------------------------

def qaoa():
    qc = QuantumCircuit(3, 3)
    qc.h([0, 1, 2])
    qc.barrier(label="cost")
    qc.cx(0, 1); qc.rz(2 * 0.59, 1); qc.cx(0, 1)
    qc.cx(1, 2); qc.rz(2 * 0.59, 2); qc.cx(1, 2)
    qc.cx(0, 2); qc.rz(2 * 0.59, 2); qc.cx(0, 2)
    qc.barrier(label="mixer")
    qc.rx(2 * 0.32, [0, 1, 2])
    qc.measure([0, 1, 2], [0, 1, 2])
    save(qc, "qaoa")


# --- QPE (T-gate, 3 counting qubits) ---------------------------------------

def qpe():
    qc = QuantumCircuit(4, 3)
    qc.x(3)
    qc.barrier()
    qc.h([0, 1, 2])
    qc.barrier(label="controlled-U")
    qc.cp(pi / 4, 0, 3)
    qc.cp(pi / 2, 1, 3)
    qc.cp(pi, 2, 3)
    qc.barrier(label="inverse QFT")
    qc.swap(0, 2)
    qc.h(0)
    qc.cp(-pi / 2, 0, 1)
    qc.h(1)
    qc.cp(-pi / 4, 0, 2)
    qc.cp(-pi / 2, 1, 2)
    qc.h(2)
    qc.measure([0, 1, 2], [0, 1, 2])
    save(qc, "qpe")


# --- Shor's (factoring 15, a=7, simplified) ---------------------------------

def shors():
    qc = QuantumCircuit(7, 3)
    qc.h([0, 1, 2])
    qc.x(3)
    qc.barrier(label="controlled ×7 mod 15")
    qc.cx(0, 4); qc.cx(0, 5)
    qc.barrier()
    qc.cx(1, 4); qc.cx(1, 6)
    qc.barrier()
    qc.cx(2, 3); qc.cx(2, 5)
    qc.barrier(label="inverse QFT")
    qc.swap(0, 2)
    qc.h(0)
    qc.cp(-pi / 2, 0, 1)
    qc.h(1)
    qc.cp(-pi / 4, 0, 2)
    qc.cp(-pi / 2, 1, 2)
    qc.h(2)
    qc.measure([0, 1, 2], [0, 1, 2])
    save(qc, "shors")


# --- VQE (ZZ measurement, H2-like) -----------------------------------------

def vqe():
    theta = -pi / 2
    qc = QuantumCircuit(2, 2)
    qc.ry(theta, [0, 1])
    qc.cx(0, 1)
    qc.barrier(label="measure ZZ")
    qc.measure([0, 1], [0, 1])
    save(qc, "vqe")


# --- main -------------------------------------------------------------------

if __name__ == "__main__":
    print("Generating circuit images...")
    bell_phi_plus()
    bell_phi_minus()
    bell_psi_plus()
    bell_psi_minus()
    superdense_coding()
    teleportation()
    deutsch_jozsa()
    bernstein_vazirani()
    simons()
    grovers()
    qaoa()
    qpe()
    shors()
    vqe()
    print("Done.")
