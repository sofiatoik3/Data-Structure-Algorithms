"""
Created on Saturday Aug 5 11:49:38 2023

@author: sofia
"""

def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums = nums1[0:(m)]+nums2
        cont = 0
        while (cont != m+n):
            x = min(nums)
            nums1[cont] = x
            nums.remove(x)
            cont += 1
        return (nums1)