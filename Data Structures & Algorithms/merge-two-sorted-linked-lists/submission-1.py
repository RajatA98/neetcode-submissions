# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        #determine the starting node
        if list1.val <= list2.val:
            head = list1
            l1 = list1.next
            l2 = list2
        else:
            head = list2
            l2 = list2.next
            l1 = list1
        
        #traverse through the lists until one is null
        merged = head
        while l1 and l2:
            if l1.val <= l2.val:
                merged.next = l1
                l1 = l1.next
            else:
                merged.next = l2
                l2 = l2.next
            
            merged = merged.next
        
        if l1 is None:
            merged.next = l2
        else:
            merged.next = l1
        

        return head

        
        