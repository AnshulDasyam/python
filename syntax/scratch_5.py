hours = (input('ur hours ='))
rate = (input('rate ='))
try :
    hours=float(hours)
    rate = float(rate)
except :
    hours = 0
if hours > 40:
    pay = rate*1.5*hours
    print("ur pay is = ",pay)
    print("gg")
elif hours == 0 :
    print("please enter a numeric code")
else :
    pay = rate*hours
    print("ur pay is =",pay)
