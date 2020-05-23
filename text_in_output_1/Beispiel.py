import matplotlib.pyplot as plt
import numpy as np

filename = 'dataPts.txt'

beta = np.radians(30) 

data = np.loadtxt(filename, skiprows=0)
X = data[:,0] 
Y = data[:,1]

X2= X * np.cos(beta) + Y * np.sin(beta)
Y2= -X* np.sin(beta) + Y * np.cos(beta)
print(np.shape(data))

plt.xlabel('x-Koordinate')
plt.ylabel('y-Koordiante')
plt.plot(X2,Y2, '-',color='k', linewidth=1)
plt.xlim(0,1)
plt.ylim(-1,1)
plt.axis('equal')
plt.grid(True)
plt.show()

np.savetxt('test.out', [X2,Y2], delimiter=',',  fmt='%1.4e') # oder fmt='%10.5f'
