# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

#My inital Solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            first = nums[i]
            for j in range(len(nums)-1):
                second = nums[j+1]
                total = first + second
                if total == target:
                    return [i, j+1]

#Issue: i and j can become the same indecis, so it adds to itself


#Second Solution
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            first = nums[i]
            for j in range(len(nums)-1): #Not counting last index
                if i == j: #Extra Logic
                    continue
                second = nums[j+1] #Could Potentially get index error
                total = first + second
                if total == target:
                    return [i, j+1] #Returning wrong index with j


#Third Solution
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                first = nums[i]
                second = nums[j] 
                total = first + second
                if total == target:
                    return [i, j]


#Final Solution (Cleaner)
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        