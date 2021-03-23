handle = open("D:\Github\python\syntax\mbox short.txt")
count = dict()
for line in handle :
    words = line.split()
    for x in words :
        count[x] = count.get(x,0) + 1
print(count)
high = None
text = None
for z,q in count.items() :
    if high is None or q > high :
        high = q
        text = z
print(high,text)




