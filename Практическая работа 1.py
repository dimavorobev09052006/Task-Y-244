from math import *
x=-4.5
y=0.75*10**-4
z=-0.845*10**2
a1=pow(9 + (x - y )**2,1/3)
a2=x**2+y**2+2
a3= exp(abs(x-y))*tan(z)**3
s=a1/a2-a3
print(round(s,5))