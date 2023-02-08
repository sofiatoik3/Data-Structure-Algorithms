"""

@author: Sofia Luna
"""

def Missing_Numbers (length, numbers):
    Cont_I = 1 
    Cont_F = length
    Cont_M = round(length/2)
    for i in range ((round(len(numbers)/2))+1):
        if (Cont_I not in numbers):
            return Cont_I
        elif (Cont_F not in numbers):
            return Cont_F
        else:
            Cont_I += 1
            Cont_F -= 1