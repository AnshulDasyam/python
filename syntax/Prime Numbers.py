n = int(input("Check twin primes till >>"))
z = dict()
for x in range(3,n) :
    for y in range(2,x) :
        if x % y == 0 :
            break
        if (x + 2) % y == 0 :
            break
    else :
        z[x] = x + 2
print(z)
