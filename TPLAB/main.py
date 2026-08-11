import matplotlib.pyplot as plt
import control
import numpy as np

#Filtro SOS
R1, R2 = 33e3, 13e3
C1, C2 = 1e-9, 2.22e-9

num1 = [1/(R1*R2*C1*C2)]
den1 = [1,(1 + R2/R1)*(1/(R2*C2)),1/(R1*R2*C1*C2)]

#Filtro de Primer orden
R, C = 33e3, 1e-9

num2 = [1/(R*C)]
den2 = [1, 1/(R*C)]

#Transferencias

H1 = control.TransferFunction(num1, den1)
H2 = control.TransferFunction(num2, den2)

#esto lo busque en google
Ht = H1 * H2

#Respuesta en frecuencia
worn = np.logspace(1, 6, 500)

#esto lo busque en google
mag, phase, omega = control.bode(Ht,worn,dB=True,plot=False)
gd = - np.gradient(phase, omega)


#Grafico
plt.subplot(3,1,1)
plt.semilogx(omega/(2*np.pi), 20*np.log10(mag))
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud [dB]")
plt.grid(True)
plt.tight_layout()

plt.subplot(3,1,2)
plt.semilogx(omega/(2*np.pi), phase)
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Fase [grados]")
plt.grid(True)
plt.tight_layout()

plt.subplot(3,1,3)
plt.semilogx(omega/(2*np.pi), gd*1e6)
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("delay [mS]")
plt.grid(True)
plt.tight_layout()
plt.show()