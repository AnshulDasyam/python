import re


rev = []

fname = input('Enter file: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened: ', fname)
    exit()


for line in fhand:
    line = line.rstrip()
    rev_temp = re.findall('^New Revision: ([0-9.]+)', line)
    if not rev_temp:
        for val in rev_temp:
            val = float(val)            # Convert the strings to floats
            rev = rev + [val]           # Concats new values

rev_sum = sum(rev)
count = float(len(rev))
rev_ave = rev_sum / count

print(rev_ave)