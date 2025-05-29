# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    #Find half point of array
    #If target is larger than midpoint, search upper half
    #Else search lower half
    #Repeat
    array_len = len(nums)
    left = 0
    right = array_len - 1
    while left <= right:
        mid = (right + left) // 2
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        elif target == nums[mid]:
            return mid
    
    return -1

    
    