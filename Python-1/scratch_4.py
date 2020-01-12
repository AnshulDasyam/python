

"""Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its
parameter and returns a grade as a string """


def computegrade(score):
    qa  = "a"
    qb = "b"
    qc = "c"
    qd = "fail0"
    qe = "invaild"
    if score > 1 :
        return qe
    if score > 0.8 :
        return qa
    elif score > 0.6:
        return qb
    elif score > 0.4:
        return qc
    elif score< 0 :
        return qe
    elif score < 0.4 :
        return qd

score = float(input("ur score"))
xyz =computegrade(score)
print(xyz)