from sympy import symbols, nroots
from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt
import numpy as np


s = symbols('s')

eps2 = 0.122
n = 5
#a = (1/n)*np.arcsinh(1/np.sqrt(eps2))
a = np.arcsinh(1/np.sqrt(eps2))
ancho = np.sinh(a/n)
alto = np.cosh(a/n)

#print(ancho,alto)
polinomio = 1 + eps2*(-256*s**10 - 640*s**8 - 432*s**6 - 40*s**4 - s**2)

raices = nroots(polinomio)
reales = []
complejas= []

for r in raices:
    real, imag = r.as_real_imag()
    
    if abs(imag) < 1e-10:
        reales.append(real)
    else:
        complejas.append(complex(r))
reales_smd = list(filter(lambda x: x>0, reales))
reales_smi = list(filter(lambda x: x<0, reales))

complejas_smd = list(filter(lambda x: abs(x.real>0), complejas))
complejas_smi = list(filter(lambda x: abs(x.real<0), complejas))

#print("Reales semiplano derecho:", reales_smd)
#print("Complejas semiplano derecho: ", complejas_smd)
#print('\n')
print("Reales semiplano izquierdo:", reales_smi)
print("Complejas semiplano izquierdo: ", complejas_smi)

# %% DEFINO MI ELIPSE PARA DIBUJAR
elipse = Ellipse(
    xy=(0, 0),      # centro (real, imaginario)
    width=alto,        # ancho (eje real)
    height=ancho,       # alto (eje imaginario)
    edgecolor='red',
    facecolor='none',
    angle=90
)

# %%

plt.figure(figsize=(8,6))

# gráfico
plt.axhline(0)  # eje horizontal
plt.axvline(0)  # eje vertical

#elipse chula
plt.gca().add_patch(elipse)

# de la parte de los imaginarios
real = [x.real for x in complejas]
imag = [x.imag for x in complejas]
plt.scatter(real, imag, marker='o')

#de la parte de los reales
plt.scatter(reales, np.zeros(len(reales)), marker='o')

plt.xlabel("Parte Real")
plt.ylabel("Parte Imaginaria")
plt.title("Plano complejo (raíces del polinomio)")

plt.xlim([-1.5,1.5])
plt.ylim([-1.5,1.5])

plt.grid()
plt.show()


