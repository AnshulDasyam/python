a = input()
for x,y in zip(range(len(a) - 1,-1,-1),range(0,len(a))) :
    if a[x] != a[y] :
        print("Not a palindrome")
        break
else :
    print("Its a palindrome")


