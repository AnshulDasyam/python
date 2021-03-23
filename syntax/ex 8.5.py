handle = open('mbox short.txt')
x = list()
for line in handle :
    if line.startswith("From ") :
        words = line.split()
        detail = words[1]
        print(detail)
        x.append(detail)
print(x)
print(len(x))



