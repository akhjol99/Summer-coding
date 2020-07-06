from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 1
        forward =1
        backward =1
        m = nums[0]
        for i in range(len(nums)):
            forward = forward*nums[i] or nums[i]
            backward = backward*nums[len(nums)-i-1] or nums[len(nums)-i-1]
            
            m = max(forward, backward, m)
            
        return m
