x = int(input())
a = 0
b = 0
for y in range(1,x + 1) :
    a +=1
    if len(str(y)) >= 2 :
        b *= 10**(len(str(y)) - 1)
    b += y *10**(x  - a )
print(b)