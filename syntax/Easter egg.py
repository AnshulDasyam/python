c = 0
a = (input("file name>>"))
try :
    d = open(a)
    for b in d :
        c +=1
    print("There are ",c,"subject lines in this file")
except :
    if a == "dumdum" :
        print("no u a dumdum")
    else :
        print("invalid file")
