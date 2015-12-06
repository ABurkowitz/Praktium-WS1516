import numpy as np
import scipy.optimize
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
f, uc , a = np.genfromtxt('messwerte_phasenverschiebung.txt', unpack=True)

#L(10.11e-3,0.03e-3)
#C(2.098e-9,0.006e-9)
#R1(48.1,0.1)
#R2(509.5,0.5)
#Rap(3.3e3)

plt.plot(f, uc , 'bx', label="Kondensatorspannung")

plt.xlabel(r'$Frequenz / Hz$')
plt.ylabel(r'$Spannung / V$')
plt.xscale('log')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('Kondensatorspannung.pdf')

L=ufloat(10.11e-3,0.03e-3)
C=ufloat(2.098e-9,0.006e-9)
R=ufloat(509.5,0.5)
rdiffomega=R/L
romegares=unp.sqrt(1/(C*L)-(R*L)**2/2)
print (rdiffomega)
print (romegares)
rguete=romegares/rdiffomega
print (rguete)
#(rdiffomega)(5.040+/-0.016)e+04
#(romegares)(2.171+/-0.004)e+05
#(rguete)4.309+/-0.010
omega0=unp.sqrt(1/(L*C))
omega1=R/(L*2)+unp.sqrt(R**2/(4*L**2)+1/(L*C))
omega2=-R/(L*2)+unp.sqrt(R**2/(4*L**2)+1/(L*C))
print(omega0)
print(omega1)
print(omega2)
#omega0=(2.171+/-0.004)e+05
#omega1=(2.438+/-0.005)e+05
#omega2=(1.934+/-0.004)e+05
