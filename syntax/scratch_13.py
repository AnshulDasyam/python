"""FINDING THE MAXIMUM VALUE OF THE NUMBERS ENTERED BY THE USER"""

x = None
a = int(input('no.1> '))
b = int(input('no.2> '))
c = int(input('no.3> '))
d = int(input('no.4> '))
e = int(input('no.5> '))
f = int(input('no.6> '))
for y in [a,b,c,d,e,f] :
    if x is None :
        x = y
    if y > x :
        x = y
    print("the number checked is ", y)
    print("the maximum till now is", x)
print("all done")





