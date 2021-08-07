"""
Problem link: https://leetcode.com/problems/roman-to-integer/
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        decimal_value = 0
        curr = 0
        
        while curr < len(s):
            if curr+1 < len(s) and s[curr] == "I" and s[curr+1] == "V":
                decimal_value += 4
                curr += 2
                
            elif curr+1 < len(s) and s[curr] == "I" and s[curr+1] == "X":
                decimal_value += 9
                curr += 2
 
            elif curr+1 < len(s) and s[curr] == "X" and s[curr+1] == "L":
                decimal_value += 40
                curr += 2
 
            elif curr+1 < len(s) and s[curr] == "X" and s[curr+1] == "C":
                decimal_value += 90
                curr += 2
 
            elif curr+1 < len(s) and s[curr] == "C" and s[curr+1] == "D":
                decimal_value += 400
                curr += 2
 
            elif curr+1 < len(s) and s[curr] == "C" and s[curr+1] == "M":
                decimal_value += 900
                curr += 2
 
            else:
                if s[curr] == "I":
                    decimal_value += 1
                    curr += 1
 
                elif s[curr] == "V":
                    decimal_value += 5
                    curr += 1

                elif s[curr] == "X":
                    decimal_value += 10
                    curr += 1

                elif s[curr] == "L":
                    decimal_value += 50
                    curr += 1

                elif s[curr] == "C":
                    decimal_value += 100
                    curr += 1

                elif s[curr] == "D":
                    decimal_value += 500
                    curr += 1

                elif s[curr] == "M":
                    decimal_value += 1000
                    curr += 1

        return decimal_value
