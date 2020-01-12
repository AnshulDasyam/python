x =open("romeo.txt")
q = []
for y in x :
    z = y.split()
    q +=z
q.sort()
print(q)


