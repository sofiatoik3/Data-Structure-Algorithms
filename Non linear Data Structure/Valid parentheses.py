# -*- coding: utf-8 -*-
"""

@author: sofia
"""

def isValid(self, s: str) -> bool:
    PossibleCombination = [""]
    Starts = "([{"
    Ends = ")]}"
    options = "()[]{}"
    if ((len(s)==1) and (len(s)%2 != 0 )):
        return False
    for i in range (len(s)):
        if (s[i] in Starts):
            PossibleCombination.append(s[i])
        elif (s[i] in Ends):
                
            for j in range(len(options)):
                if (options[j]==s[i]):
                    temp = options [j-1]
                    if (temp != PossibleCombination[-1] ):
                        return False
                    else:
                        PossibleCombination.pop()
                            
    if (len(PossibleCombination)==1):                    
        return True
    else:
        return False