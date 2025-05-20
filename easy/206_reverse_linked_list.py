# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev


#Start Linked List with None
#Create a temp variable to hold the reamining old list
#Point the new head.next to what essentially was the previous link
#Move up the new linked list up by one by poiting it to the "head"
#Reassign the remaining old list held on temp to head again
#Repeat until head is none