b = list()
while True :
    a = float(input("enter a number >>"))
    b.append(a)
    c = input("if over input done >>")
    if c == "done" or c == "Done" :
        break
print("max value is",max(b))
print("min value is",min(b))