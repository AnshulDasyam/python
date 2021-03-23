'''Asking the user for a input file and finding  lines starting with _______ '''

a = open(input("file name:"))
c = 0
g = 0
for b in a :
    if b.startswith("X-DSPAM-Confidence:") :
       b = b.rstrip()
       print(b)
       e = float(b[20:26])
       print(e)
       c +=1
       g +=e
print("The average is",g/c)

