import scipy.signal as sp
import matplotlib.pyplot as plt
import numpy as np
import control

w = np.logspace(-2, 2, 500)

#%% 1ra etapa
num1_hp = [1.61, 0]
den1_hp = [1, 1.61]

num1_lp = [1]
den1_lp = [1, 0.62]

w_hp, h_hp = sp.freqs(num1_hp, den1_hp, w)
w_lp, h_lp = sp.freqs(num1_lp, den1_lp, w)

#Graficos de prueba
'''
plt.figure(figsize=(12,6))
plt.semilogx(w_hp, 20*np.log10(abs(h_hp)))
plt.semilogx(w_lp, 20*np.log10(abs(h_lp)))

plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud [dB]")
plt.grid()
plt.show()
'''
#%% 2da etapa

num2_hp = [0.62, 0, 0]
den2_hp = [1, 0.54, 0.87]

num2_lp = [0.71]
den2_lp = [1, 0.62, 1.15]

w2_lp, h2_lp = sp.freqs(num2_lp, den2_lp, w)
w2_hp, h2_hp = sp.freqs(num2_hp, den2_hp, w)

#graficos de prueba
'''
plt.figure(figsize=(12,6))
plt.semilogx(w2_hp, 20*np.log10(abs(h2_hp)))
plt.semilogx(w2_lp, 20*np.log10(abs(h2_lp)))

plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud [dB]")
plt.grid()
plt.show()
'''

#%% sistema completo

#obtengo los sistemas y los pongo en cascada
sys1_hp = control.tf(num1_hp, den1_hp)
sys1_lp = control.tf(num1_lp, den1_lp)

sys2_hp = control.tf(num2_hp, den2_hp)
sys2_lp = control.tf(num2_lp, den2_lp)

syst_lp = control.series(sys1_lp, sys2_lp)
syst_hp = control.series(sys1_hp, sys2_hp)

print(syst_hp)
#%% GRAFICANDO EL SISTEMA COMPLETO
#obtengo las frecuencias para graficar
mag_lp, phase_lp, wt_lp = control.bode(syst_lp, w, plot=False)
mag_hp, phase_hp, wt_hp = control.bode(syst_hp, w, plot=False)

#test graficos todos los graficos
'''
#graficos
plt.figure(figsize=(12,6))
plt.title("Sistema completo")
#high pass
plt.semilogx(wt_hp, 20*np.log10(abs(mag_hp)))
plt.semilogx(w_hp, 20*np.log10(abs(h_hp)), '--')
plt.semilogx(w2_hp, 20*np.log10(abs(h2_hp)), '--')

#low pass
#plt.semilogx(wt_lp, 20*np.log10(abs(mag_lp)))
#plt.semilogx(w_lp, 20*np.log10(abs(h_lp)), '--')
#plt.semilogx(w2_lp, 20*np.log10(abs(h2_lp)), '--')

plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud [dB]")
plt.grid()
plt.show()
'''
#%% Ahora comparo
#analitico vs python
n = 3       # orden del cheby
rp = 0.5    # db

#forma floja de realizarlo
num, den = sp.cheby1(3, rp, 1, btype='high', analog=True, output='ba')

w_cheby, h_cheby = sp.freqs(num, den, w)

plt.figure(figsize=(12,6))
plt.title(f"Chebyshev de orden {n}")
plt.semilogx(w_cheby, 20*np.log10(abs(h_cheby)), label='computer')
plt.semilogx(wt_hp, 20*np.log10(abs(mag_hp)), label='analitico')

plt.legend()
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud [dB]")
plt.grid()
plt.show()

#%% Forma pro de hacerlo

z, p, k = sp.cheb1ap(n, rp)
num_lp, den_lp = sp.zpk2tf(z, p, k)
num_hp, den_hp = sp.lp2hp(num_lp, den_lp)

w3_lp, h3_lp = sp.freqs(num_hp, den_hp)

plt.figure(figsize=(12,6))
plt.title(f"Chebyshev de orden {n}")
plt.semilogx(w3_lp, 20*np.log10(abs(h3_lp)), label='computer 2')
plt.semilogx(w_cheby, 20*np.log10(abs(h_cheby)), label='computer 1')


plt.legend()
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud [dB]")
plt.grid()
plt.show()
