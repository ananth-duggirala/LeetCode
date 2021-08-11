"""
Problem statement: https://leetcode.com/problems/binary-search
"""

from math import floor, ceil
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        mid = math.floor(n/2)
        end = n-1
        
        while True:
            if nums[mid] == target:
                return mid
            if target < nums[0] or target > nums[n-1]:
                return -1
            
            if nums[mid] < target:
                start = mid+1
                mid = ceil((start + end)/2)
                if start == mid:
                    if nums[mid] == target:
                        return mid
                    else:
                        return -1
                
            if target < nums[mid]:
                end = mid-1
                mid = ceil((start + end)/2)
                if start == mid:
                    if nums[mid] == target:
                        return mid
                    else:
                        return -1