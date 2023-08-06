# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 23:52:40 2023

@author: sofia
"""

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    Arr = nums1 + nums2
    Arr = sorted(Arr)
    if (len(Arr)%2 == 0):
        Position1 = int(round((len(Arr))/2))
        Position2 =  Position1 - 1 
        self = (Arr[Position1] + Arr[Position2]) / 2
        return self
    else:
        Position = int(len(Arr)/2)
        Median = Arr[Position]
    return Median