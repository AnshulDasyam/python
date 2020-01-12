handle = open('mbox short.txt')
count = dict()
blit = dict()
for lines in handle:
    if lines.startswith("From "):
        words = lines.split()
        email = words[1]
        count[email] = count.get(email, 0) + 1
        dom = email.split("@")
        domain = dom[1]
        blit[domain] = blit.get(domain,0) + 1
print(blit)
print(count)
high = None
name = None
for x, y in count.items():
    if high is None or y > high:
        high = y
        name = x
print(name, high)
