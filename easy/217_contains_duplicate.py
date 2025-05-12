#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#Initial Solution
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            num_to_check = nums[i]
            for j in range(i + 1, len(nums)):                            
                if num_to_check == nums[j]:
                    return True

        return False


#Initial solution uses brute force
#Problem: If array becomes large enough then itll take to long


#Second Solution
class secondSolution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False


#Notes: Using a set makes it easier to simply check if duplicate is in list