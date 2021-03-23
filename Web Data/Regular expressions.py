import re
hand = open('mbox short.txt')
for line in hand:
    line = line.rstrip()
    # Using ^. and finding words with @
    x = re.findall('\S+@\S+', line)
    if len(x) > 0: print("1",x)
    # Remove unnecesary symbols
    x = re.findall('\S+@\S+[0-9a-zA-Z]', line)
    if len(x) > 0: print("2  ",x)
    # Find all lines which begin with X-
    x = re.findall('^X-\S+: [0-9.]+',line)
    if len(x) > 0: print("3      ",x)
    # Just extract the numbers
    x = re.findall('^X-\S+: ([0-9.]+)', line)
    if len(x) > 0: print("4          ",x)


