# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:07:32 2022

@author: sofia
"""

def lengthOfLongestSubstring(self, s):
    if len(s)==0:
        count=0
    else:
        s=s+s[len(s)-1]
        count=1
    for i in range (len(s)):
        Posible_list=[]
        length=len(s)
        Posible_list.append(s[i])
        for j in range (i,length-1):
            if s[j+1] in Posible_list:
                counter=len(Posible_list)
                if counter>count:
                    count=counter
                    
                    Posible_list=[]
                    break
                else:
                    Posible_list=[] 
                    break
            else:
                
                Posible_list.append(s[j+1])
                
        counter=len(Posible_list)
        if counter>count:
            count=counter    
    return (count)