import collections
ar = list(map(int,input().split()))
ar.sort()
for x in range(0,10**(len(ar))) :
    z = list(map(int,str(x)))
    if collections.Counter(ar) == collections.Counter(z):
        print(x)