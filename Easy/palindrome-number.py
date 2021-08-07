"""
Problem link: https://leetcode.com/problems/palindrome-number
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:            
        digits = []
        is_negative = False
        
        if x<0:
            return False
        
        while x>0:
            digits.append(x%10)
            x = x//10
        
        n = len(digits)
        for i in range(n//2):
            if digits[i] != digits[n-1-i]:
                return False
        return True