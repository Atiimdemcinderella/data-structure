import numpy as np
L=12 #length of beam in meters 
w=10 #intensity of load in KN/M
#Question a
#Bending moment(M) and shear force(V) at the first end, x=0
x=0
M=(w*(-6*x**2+6*L*x-L**2))/12
v=w*(L/2-x)
m='The bending monent at x=0 is'
n='the shear force at x=0 is'
print()
print('(a.1)' + m +str(M)+'and',n + str(v))
#Bending moment (M) and shear force (V) at the first end, x=L=10
x=L
M=(w*(-6*x**2+6*L*x-L**2))/12
V=w*(L/2-x)
a='The bending moment at x=L is'
b='the shear force at x=L is '
print('(a.2)' + m +str(M) + 'and',n +str(v))
#Question b
"""
When bending moment is zero, we get an expression x**2-Lx + L**2/6=0
"""
#from the expression 
a=1
b=-L
c=L**2/6
#using the almighty formula the two roots are;
discriminant=b**2-4*a*c
root_1b=(-b+np.sqrt(discriminant))/2*a
root_2b=(-b-np.sqrt(discriminant))/2*a
print()
print('(b) The points of contra-flexure are {0} and {1}'.format(root_1b,root_2b))
#question c
"""
when the shear force is zero, x= l/2
"""
x=L/2
print()
print('(c) the point at which v=0 is{}'.format(x))
#Question d
p=0
s=0.01
q=L+s
M=(w*(-6*x**2+6*L*x-L**2))/12
print()
print('(d) using the initialized variable, the bending moment at each step in arry is {0}'.format(M))
#Question e
v=w*(L/2-x)
print()
print('(e) The shear force for each stepmalong the span is {}'. format(v))
#Question f
"""
Let the absolute value of the bending moment array be AM
Also let minimum AM be m_AM
"""
AM=abs(M)
m_AM=int(AM)
"""
When the bending moment is m_AM, we get an expression x**2 - Lx + (L**2/6)+(2*m_AM)/w=0
"""
#from the above expression
a=1
b=-L
c=(L**2/6)+(2*m_AM)/w
#using the almighty formula the two roots are ;
discriminant=b**2-4*a*c
root_1f=(-b+np.sqrt(discriminant))/2*a
root_2f=(-b-np.sqrt(discriminant))/2*a
print()
print('(f) the points along L at which the absolute values of the bending moment arry is minimum are {0} and {1}'.format(root_1f,root_2f))
#Question g
"""
 let the relative errors be r_e
 """
r_e1=((root_1b-root_1f)/root_1b*100)
r_e2 =((root_2f-root_2b)/root_2f*100)
print()
print('(g) The relative errors between estimated points of contra-flexture are{0}% and{1}%'.format(r_e1,r_e2))
#Question h
"""
let maximum bending moment be max_M and the minimum bending moment be min_M
"""
#for he maximum 
max_M=int(M)
"""
When the bending moment is max_M. we get an expression x**2-Lx +(L**2/6)+(2*max_M)/w=0
"""
a=1
b=-L
c=(L**2/6)+(2*max_M)/w
#Using the almighty formula the two roots are;
discriminant=b**2-4*a*c
root_1=(-b+np.sqrt(discriminant))/2*a
root_2=(-b+np.sqrt(discriminant))/2*a
print()
print('(h.2) The point at which the minimium bending moment occur are {0} and {1}'.format(root_1,root_2))
