#Given an integer array nums, find the subarray with the largest sum, and return its sum.


#Initial Solution
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = float('-inf')
        current_sum = 0
        for num in nums:
            current_sum += num
            max_num = max(max_num, current_sum)
        return max_num 


#Problem: If current_sum goes below 0 then might as well have it restart at 0


#Second Solution
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = float('-inf')
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum < 0:
                current_sum = 0
            max_num = max(max_num, current_sum)
        return max_num


#Problem: If the max is a negative number it would be recorded as a 0


#Final Solution
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = float('-inf')
        current_sum = 0
        for num in nums:
            current_sum += num
            max_num = max(max_num, current_sum)
            if current_sum < 0:
                current_sum = 0
        return max_num

