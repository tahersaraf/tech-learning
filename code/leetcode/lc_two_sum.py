"""
1. Two Sum

https://leetcode.com/problems/two-sum/description/
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i,num in enumerate(nums):
            result = target - num

            if result in seen:
                return [seen[result], i]
            
            seen[num] = i

        return []
