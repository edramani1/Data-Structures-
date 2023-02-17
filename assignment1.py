#6935521
#edramani1
import numpy as np

x = 0
L = 12
w = 10
x1 = L     # when the value of x=12m
M = w*(-6*x**2 + 6*L*x - L**2)/(12)
V = w*((L/2)-x)
m1 = w*(-6*x1**2 + 6*L*x1 - L**2)/(12)
print("The bending moment when x = 0 is: ", M,"knm")
print("The bending moment when x = L is : ", m1,"knm")
a = -6
b = 72
c = -144
d = b**2 - 4*a*c
x1 = (-b + np.sqrt(d))/(2*a)
x2 = (-b - np.sqrt(d))/(2*a)
print("The point at which the bending moment is zero is {0}m and {1}m ".format(x1,x2))
print("")
# w*(L/2 - x) = 0 thus shear force is zero
# making x the subject of the equation above
# x = L/2

x = L/2        # the point at which shear force is zero
print("The point at which the shear force is zeros is:\n", x)
print("")
x = (np.array(range(0,12010,10)))/1000
M = w*(-6*x**2 + 6*L*x -L**2)/12
print("The moment at various points are calculated below: ", M)
print("")
x = (np.array(range(0, 12010, 10)))/1000       # in meters
V = w*((L/2) - x)         #kN
print("The shear force at various sections are calculated below: ", V)
print("")
Ma = (abs(M))      #absolute value of bending moments different points
Mam = min(Ma)
print(Mam)
#The formular for bending moment, M = w*(-6*x**2 + 6*L*x - L**2)/12
# Equating the expression to the minimum bending moment 
# The equation will  be 0.1704 = -6*x**2 + 6*L*x - L**2
# -6*x**2 + 6*L*x - L**2 = 0.1704
# -6*x**2 + 72*x - 144= 0.1704
#-6*x**2 + 72*x - 144.1704 = 0
print("")
a = -6
b = 72
c = -144.1704
d = b**2- 4*a*c
xf1 = (-b + np.sqrt(d))/(2*a)
xf2 = (-b - np.sqrt(d))/(2*a)
print("The points at which the minimum bending moment occurs are {0} and {1}".format(xf1,xf2))
#Relative error between the points of b and f
print("")
x1 = 2.535898384862245 
x2 = 9.464101615137755
r1 = x1 - xf1
r2 = x2 - xf2
print("The relative error for first  two points: ", r1)
print("")
print("The relative error for second two point: ",r2)
print("")
my = min(M)
print("")
mt = max(M)
print("The maximumt bending moment: ", mt)
print("")
print("The minimum bending moment:",my)
print("")
#finding the points at which  maximum bending moment occur
#from equation -6*x**2 + 72*x - 216= 0
a = -6
b = 72
c = -216
d = b**2 - 4*a*c
sol1 =(-b + np.sqrt(d))/(2*a)
sol2 = (-b - np.sqrt(d))/(2*a)
print("The points at which the maximum bending moment occurs are {0} and {1} .".format(sol1,sol2))
print("")
print("Therefore the point where the maximum bending occurs is 6.0 meters.")
#finding the points for the minimum bending moment
#from the equation -6*x**2 + 72*x = 0
print("")
a = -6
b = 72
c = 0
d = b**2 - 4*a*c
sol3 = (-b + np.sqrt(d))/(2*a)
sol4 = (-b - np.sqrt(d))/(2*a)
print("The points at which the minimum bending moment occurs are {0} and {1} .".format(sol3,sol4))
print("")
print("Therefore the points where the minimum bending moment occurs are  0 and 12.")


