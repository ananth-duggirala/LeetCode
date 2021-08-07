"""
Problem link: https://leetcode.com/problems/reverse-integer
"""

class Solution:
    def reverse(self, x: int) -> int:
        x_rev = 0
        is_negative = False
        
        if x<0:
            is_negative = True
            x = -x
            
        while x>0:
            x_rev *= 10
            if x_rev + x%10 < 2**31 -1:
                x_rev += x % 10
            else:
                x_rev =0
                break
            x = x//10
        
        if is_negative:
            x_rev = -x_rev
            
        return x_rev