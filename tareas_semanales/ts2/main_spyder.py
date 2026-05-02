# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp

# %% ejercicio numero 1 - 2
orden = 6
fc = 1/(2*np.pi)
fc = 1
fs = 1000

b, a = sp.butter(orden, fc/(fs/2), btype='low')

w, h = sp.freqz(b, a)

plt.figure(figsize=(12,6))
plt.semilogx((w*fs)/(2*np.pi), 20*np.log10(abs(h)))
plt.title("Filtro Butterworth de orden 6")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud [dB]")
plt.grid(which='both', linestyle='--', linewidth=0.7)
plt.axvline(fc, color='red', linestyle='--', label='fc')
plt.legend()
plt.show()
# %% ejercicio 3
