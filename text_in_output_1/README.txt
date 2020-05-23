Wichtige Befehle um Zahlen aus Text-Datei zu lesen und zu plotten:

import matplotlib.pyplot as plt
import numpy as np

f = open("filename",'r')
print(f.read())
print(f.readline())  # nur eine Line ausgeben

f = open("filename","a")  # file öffnen in append-Mode
f.write("Now the file has more content!") 
f.close()

# Mit Numpy am einfachsten!
array = np.loadtxt('filename')
X=array[:,0]  # Erste Spalte
Y=array[:,1]  # Zweite Spalte
...
np.savetxt('test.out', array, delimiter=',' fmt='%1.4e') # oder fmt='%10.5f'


plt.plot(x,y, 'r-')
plt.axis('equal')
