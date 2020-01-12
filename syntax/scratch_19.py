count = 0
d = 0
while True :
    count +=1
    if count == 1 :
        a = int(input("number = "))
        d = a
    elif count != 1 :
        b = input("operator = ")
        a = int(input("number = "))
        if b == "*" :
            d = d*a
        elif b == "/":
            d = d/a
        elif b == "-":
            d = d - a
        elif b == "+" :
            d = b+a
    print(d)
    c = (input("PRESS 1 IF DONE >"))
    if c == "1" :
        break
print(d)


