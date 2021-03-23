
#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message.
# If the score is between 0.0 and 1.0, print a grade using the following table:
marks = input("input ur score")
try :
    score = float(marks)
except :
    score = 100
if score >1 :
    print("invalid score")
elif score < 0 :
    print("invalid score")
elif  score >=0.9 :
    print ("u got an a")
elif score >=0.7 :
    print("u got a b")
elif score >=0.4 :
    print(" u got a c")
else :
    print("u fail")