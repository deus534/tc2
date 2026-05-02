# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Frecuencia normalizada
w = np.logspace(-1, 1, 500)  # de 0.1 a 10 rad/s

def H(w, Q):
    # Magnitud del filtro de 2º orden normalizado (w0 = 1)
    num = 1
    den = np.sqrt((1 - w**2)**2 + (w/Q)**2)
    return num/den

# Valores de Q a comparar
Q_values = [0.1, 0.5, 0.707, 1.932, 10]

plt.figure(figsize=(8,6))
for Q in Q_values:
    H_w = H(w, Q)
    plt.semilogx(w, 20*np.log10(H_w), label=f"Q = {Q}")

plt.axhline(-3, color='gray', linestyle='--', label="-3 dB")
plt.title("Respuesta en frecuencia de filtro 2º orden normalizado")
plt.xlabel("Frecuencia normalizada ω")
plt.ylabel("Magnitud (dB)")
plt.grid(True, which="both", ls="--")
plt.legend()
plt.show()
