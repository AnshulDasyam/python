handle = open('mbox short.txt')
count = dict()
for lines in handle:
    if lines.startswith("From "):
        words = lines.split()
        day = words[2]
        count[day] = count.get(day, 0) + 1
print(count)

