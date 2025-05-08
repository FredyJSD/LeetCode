# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#Inital Solution
#Problem: Starts with the 0
#Problem: What if one list ends before the other
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        newList = ListNode()
        current = newList
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                current = current.next
                list1 = list1.next
            elif list1.val > list2.val:
                current.next = list2
                current = current.next
                list2 = list2.next
            else:
                current.next = list1
                current = current.next
                list1 = list1.next
        
        return newList

#Second Solution
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        newList = ListNode()
        current = newList
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                current = current.next
                list1 = list1.next
            elif list1.val > list2.val:
                current.next = list2
                current = current.next
                list2 = list2.next
            else:
                current.next = list1
                current = current.next
                list1 = list1.next
                current.next = list2
                current = current.next
                list2 = list2.next
        
        if list1:
            while list1:
                current.next = list1
                current = current.next
                list1 = list1.next
        elif list2:
            while list2:
                current.next = list2
                current = current.next
                list2 = list2.next

        return newList.next

#Simplified
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        newList = ListNode()
        current = newList
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                current = current.next
                list1 = list1.next
            elif list1.val > list2.val:
                current.next = list2
                current = current.next
                list2 = list2.next
            else:
                current.next = list1
                current = current.next
                list1 = list1.next
                current.next = list2
                current = current.next
                list2 = list2.next
        
        current.next = list1 if list1 else list2

        return newList.next

#Notes: list = list1.next is stopping from the entire list to be attached to the newList
#Notes: List comprehension simplifies the code
#Notes: Remeber that the code starts at 0, so newList.next must be returned
#Notes: If both nodes are equal add them at the same time