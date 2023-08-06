# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 10:33:58 2022

@author: sofia
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        L_nums = [n]
        repeated = False
        while (n != 1) and (repeated == False ) :
            sum_n = 0
            s_num = str(n)
            for i in range(len(s_num)):
                sum_n += int(s_num[i])**2
            n = sum_n
            if sum_n in L_nums:
                repeated = True
            else:
                L_nums.append(sum_n)
        if repeated == True:
            return False
        else:
            return True
