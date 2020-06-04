import matplotlib as plt
import numpy as np

# Konstanten:
a0 = 0.2969
a1 = -0.126
a2 = -0.3516
a3 = 0.2843
a4 = -0.1015 # or -0.1036 if TE closed

# NACA MPXX e.g. NACA 2412
print("Enter M: ")
M = int(input())
print("Enter P: ")
P = int(input())
print("Enter XX: ")
XX =int(input())
print("Wie viele Punkte: ")
nbPts = int(input())

x = np.linspace(0,1, nbPts, endpoint=True)
print(M,P,XX)

# front 0 < x < P
y_c = M/ np.power(P,2) * (2*P*x - np.power(x,2))
print(x)
print(y_c)
y_c_back = M/(1-P)
