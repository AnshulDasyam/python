"""Finding the roots of a expression ax^2 + bx + c"""
import cmath
a=int(input("co-efficient of x^2(a) = "))
b=int(input("co-efficient of x(b) = "))
c=int(input("constant term(c) = "))
delta =(b**2 - 4*a*c)
print("Your equation is",a,"x**2 +",b,"x +",c)
r1 = (-b + cmath.sqrt(delta))/2*a
r2 = (-b - cmath.sqrt(delta))/2*a
if delta >= 0 :
    print("Real",end=" ")
    r1 = (-b + delta**0.5) / 2 * a
    r2 = (-b - delta**0.5) / 2 * a
    if r1 == r2 :
        print("And equal roots")
    else :
        print("And unequal roots")
else :
    print("Imaginary roots")
print("The roots are ",r1,"And",r2)