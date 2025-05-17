# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.


#Initial Solution
#At first the inner for loop on its own would only run once. To solve this I tracked how many zeroes are in the array
#Now Knowing how many zeroes there are, It can run the for loop that many times. 
def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    zeroes = 0
    for num in nums:
        if num == 0:
            zeroes+=1

    for _ in range(zeroes):
        for i in range(len(nums) - 1):
            print(nums)
            if nums[i] == 0:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp

#Problem: Ineficient
#Second Solution
def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            temp = nums[insert_pos]
            nums[insert_pos] = nums[i]
            nums[i] = temp
            insert_pos += 1

#Using pointers only one loop is required
#One pointer to scan the array 'i'
#Second pointer to keep track of where to swap 'insert_pos'



nums = [0,1,0,3,12]
print(moveZeroes(nums))