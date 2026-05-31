import scipy.signal as sig
import matplotlib.pyplot as plt
import numpy as np
import control

#recordar que todo esta normalizado para w0=1

w = np.logspace(-2, 2, 500)
#%% Con python
b, a = sig.bessel(N=3, Wn=1, btype='low', analog=True)
wt_p, ht_p = sig.freqs(b, a, worN=w)


#%% esto realizandolo con expandidas

# si lo normalizo me quedaria de la siguiente manera
#sys1_num = control.tf([1.31],[1, 1.31])
#sys2_num = control.tf([11.45],[1, 4.69, 11.45])

sys1_num = control.tf([1],[1, 1])
sys2_num = control.tf([1],[1, 1/0.72, 1])

syst_num = control.series(sys1_num, sys2_num)

mag_1, phase_1, w_1 = control.bode(sys1_num, w, plot=False)
mag_2, phase_2, w_2 = control.bode(sys2_num, w, plot=False)
mag_t, phase_t, w_t = control.bode(syst_num, w, plot=False)

#%%
#normalizado a w0=1
num = [15]
den = [1, 6, 15, 15]

#el w0 del de orden 3 es raiz cubica(15)
num, den = sig.lp2lp(num, den, 1/np.cbrt(15))

wt, ht = sig.freqs(num, den, w)

plt.figure(figsize=(12,6))

plt.semilogx(wt, 20*np.log10(abs(ht)))
plt.semilogx(wt_p, 20*np.log10(abs(ht_p)))
plt.semilogx(w_t, 20 *np.log10(abs(mag_t)))
plt.semilogx(w_2, 20 *np.log10(abs(mag_2)), '--')
plt.semilogx(w_1, 20 *np.log10(abs(mag_1)), '--')


plt.legend(['original', 'python', 'numerica','SOS_numerica', 'orden 1_numerica'])
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud [dB]")
plt.grid()
plt.show()