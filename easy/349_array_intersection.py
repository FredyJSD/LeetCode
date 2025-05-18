# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must be unique and you may return the result in any order.

#Initial Solution
def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    List = []
    for num1 in nums1:
        for num2 in nums2:
            if num1 == num2:
                if num1 not in List:
                    List.append(num1)
    
    return List


#Inefficient due to inner for loop
#Using Sets

#Final Solution
def intersection(nums1, nums2):
    nums2_set = set(nums2)
    intersection_set = set()
    for num in nums1:
        if num in nums2_set:
            intersection_set.add(num)

    return list(intersection_set)

#Convert nums2 into a set, that way its faster to check for intersection



nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

List = intersection(nums1, nums2)
print(List)