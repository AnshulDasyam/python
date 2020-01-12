"""Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which
    takes two parameters (hours and rate)"""


def computepay(hours,rate):
    pay = rate * hours
    return pay
hours = int(input("hours"))
rate = int(input("rate"))
pay = computepay(hours, rate)
print(pay)

