# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #Traverse to end to find size

        cur = head
        size = 0
        while cur:
            size += 1
            cur = cur.next
        
        #now end up right before the node we need to remove
        dummy = ListNode(0,head)
        cur = dummy

        for i in range(size-n):
            cur = cur.next


        cur.next = cur.next.next

       
        return dummy.next


