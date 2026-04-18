import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp


#-------REPASO--------

w0 = 2*np.pi*10
Q = 0.1
H = 1

num = [0,0,H*w0**2]
den = [1,w0/Q,w0**2]

w,h = sp.freqs(num, den, np.arange(1,1e3,0.001))

wb, mag, phase = sp.bode((num,den))

plt.semilogx(wb, mag)
plt.semilogx(wb, phase)

#plt.plot(w, np.abs(h))
#plt.plot(w, np.angle(h))