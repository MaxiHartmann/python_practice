import numpy as np
import matplotlib.pyplot as plt

# Grenze: y+ = 11
yplus=11
C_p=5    # for a smooth wall
kappa=0.41 

y_visk = np.logspace(0.1,1,10)
y_log = np.logspace(1,3, 20)
u_p1 = y_visk 
u_p2 = 1/kappa * np.log(y_log) + C_p

textstr="u+ = 1/k log(y+) + C"

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(y_visk, u_p1, color='black', marker='^')
ax.plot(y_log, u_p2, color='black', marker='^')
ax.set_xlabel('y+')
ax.set_ylabel('U+')
ax.set_ylim(0.1, 25)
# ax.set_xlim(0.1, 2000)
ax.grid(which='both')
# plt.plot(y, u_p1)
# plt.plot(y, u_p2)
plt.xscale("log")
# ax.xaxis.set(ticks=range(1,5))
ax.text(20,10 , textstr, fontsize=8)
plt.show()
