# Einfaches Polynom f(x) = a + bx + cx^2 + dx^3 + ex^4 + fx^5 + g^6
#==================================================================
set xrange [-5:10]
set yrange [-150:250]
a=-12 
b=-25
c=-2.0
d=0.7
e=0
f=0
g=0
f(x)=a+b*x+c*x**2+d*x**3+e*x**4+f*x**5+g*x**6
plot f(x)
