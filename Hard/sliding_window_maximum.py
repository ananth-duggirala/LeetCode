"""
Problem statement: https://leetcode.com/problems/sliding-window-maximum
"""

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        Q = deque()
        solution = []
        for i in range(k):
            while Q and nums[Q[-1]] < nums[i]:
                Q.pop()
            Q.append(i)
        
        for i in range(k,n):
            solution.append(nums[Q[0]])
            
            while Q and Q[0] <= i-k:
                Q.popleft()
            
            while Q and nums[Q[-1]] < nums[i]:
                Q.pop()
            Q.append(i)

        solution.append(nums[Q[0]]) # final iteration
        
        return solution