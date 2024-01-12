from math import *
print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => "))
S=a**2
print("Ruudu pindala", round(S,1))
P=4*a
print("Ruudu ümbermõõt", round(P,1))
di=a*sqrt(2), #правельно писать sqrt because from math import *
print("Ruudu diagonaal", di,2) #скобка
print()
print("Ristküliku karakteristikud")
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #float
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #float
S=b*c
print("Ristküliku pindala", round(S,1))
P=2*(b+c) #добавить *
print("Ristküliku ümbermõõt", round(P,1))
di=sqrt(b**2+c**2) #два знака *
print("Ristküliku diagonaal", round(di,1))
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) #float
d=2*r # *
print("Ringi läbimõõt"+ str(round(d,1))) # str + round
S=pi*r**2 # **
print("Ringi pindala", round(S,2)) #round()
C=2*pi*r # *
print("Ringjoone pikkus", round(C,2)) # round()