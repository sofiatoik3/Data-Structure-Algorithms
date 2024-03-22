# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:42:22 2023

@author: sofia
"""

                       

def fubinochi (n):
    a=1
    b=1
    Final = 0
    if (n==1) or (n==2):
        return 1
    else:
        for i in range (n-3):
            Final = a+b;
            b = a
            a = Final
        return Final
res = fubinochi(300)

def dupes (NewList):
    Unique =set(NewList)
    Unique = list (Unique)
    Final = []
    for i in range (len(Unique)):
        Value = [Num for Num in NewList if Num == Unique[i]]
        Final.append(len(Value))
    return Final

result = dupes([1,1,1,3,4,5,2,3])
