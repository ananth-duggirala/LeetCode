"""
Problem link: https://leetcode.com/problems/two-sum/
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        solution = []
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    solution.append(i)
                    solution.append(j)
                    return solution