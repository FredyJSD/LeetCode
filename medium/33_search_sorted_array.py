# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# 
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in 
# nums, or -1 if it is not in nums.
# 
# You must write an algorithm with O(log n) runtime complexity.

#Initial Solution (Not efficient)
def search(self, nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    
    return -1


#Final Solution
def search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (high + low) // 2

        if nums[mid] == target:
            return mid

        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

# Adjusted Binary search tree
# Checks whether the lower half is sorted, if not it throws it away
# Then it does binary search within that range
        