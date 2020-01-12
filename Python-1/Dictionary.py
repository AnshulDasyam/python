text = input("text here>>")
words = text.split()
print("words",words)
count = dict()
for x in words :
    count[x] = count.get(x,0) + 1
print(count.items())

