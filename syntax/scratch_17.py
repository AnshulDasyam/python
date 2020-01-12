"""Write a program to find the summation, average, maximum, minimum of all the inputs from the user and return a error when the user enters a
 invalid datatype using try and except structure."""
a = 0
d = None
e = None
b = 0
c = 0
while True :
    try :
        a = int(input("enter a number >"))
    except :
        print("Invalid number")
    b += a
    c += 1
    if d is None :
        d = a
    if a >d :
        d = a
    if e is None :
        e = a
    if a < e :
        e = a
    x = input("If Done Type yes ")
    if x == "yes" or x == "Yes" :
        break

print("summation = ",b,"count = ",c,"Average =",b/c,"Maximum value = ",d,"Mininmum value =",e)




