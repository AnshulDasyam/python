import re
x = list()
handle = open("mbox.txt")
for lines in handle :
    a = lines.rstrip()
    if re.search('X-',a) :
        x.append(re.findall('X-',a))
print(len(x))