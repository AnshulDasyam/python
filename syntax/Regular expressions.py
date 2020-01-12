import re
handle = open("mbox short.txt")
for lines in handle :
    x =lines.rstrip()
    if re.search("X.*:",x):
        print(x)