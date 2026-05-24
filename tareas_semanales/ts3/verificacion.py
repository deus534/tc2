# -*- coding: utf-8 -*-
import scipy.signal as sp
from sympy import symbols, expand, I, nroots


#%%
n = 3
rp = 0.5

z, p, k = sp.cheb1ap(n,rp)

for pole in p:
    print(pole)
print(k)
print('\n')
#%% Resolver ecucaciones
eps2 = 0.122
w, s = symbols('w s')

expre = 1 + eps2*(4*w**3 - 3*w)**2

sol = expand(expre)
sol_s = sol.subs(w, s/I)


print(f"resuelta con 'w': {sol}")
print(f"resuelta con 'w=s/j': {sol_s}")

#%%raices del polinomio
raices = nroots(sol_s)

print('\npolos para polinomio numerico')
for r in raices:
    real, imag = r.as_real_imag(r)
    if(real<0):
        print(f"{real}[::]{imag}")

t = symbols('t')
polinomio = 1.4*t**3 + 1.75*t**2 + 2.14*t + 1
raices = nroots(polinomio)
print('\npolos para polinomio analitico')
for r in raices:
    real, imag = r.as_real_imag(r)
    if(real<0):
        print(f"{real}[::]{imag}")
