"""You are given an array A of size N. The array contains integers and is of even length. The elements of the array
represent N coin of values V1, V2, ....Vn. You play against an opponent in an alternating way.
In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, and
receives the value of the coin.
You need to determine the maximum possible amouint of money you can win if you go first.

Input:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains two
lines of input. The first line contains N denoting the size of the array. The second line contains N elements of the
array.
list(map(int,input().split()))
Output:

a=[12,56,99]
b=[0 for i in range(100)]


For each testcase, in a new line, print the maximum amount."""


a = list()
b=int(input("Number of coins>> "))
c = 0
while True :
    a.append(int(input("Enter the values of the coins one by one>> ")))
    if len(a) == b :
        break
print(a)
while True :
    if len(a) == 0 :  break

    c += d
    a.remove(d)
    if len(a) == 0 : break
    e = max(a)
    a.remove(e)
print("maximum value player can select",c)



