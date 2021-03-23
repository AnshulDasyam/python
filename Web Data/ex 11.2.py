import re
z = list()
handle = open('mbox short.txt')
for lines in handle :
    x = lines.rstrip()
    if re.search('New Revision: ',x) :
        y = (re.findall('[0-9]+',x))
        y[0] = int(y[0])
        z.append(y[0])
print(sum(z)/len(z))

