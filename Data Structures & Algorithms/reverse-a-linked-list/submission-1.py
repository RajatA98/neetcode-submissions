# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #traverse through list
        #have a pointer looking at current list
        #pointer pointing to prev
        #temp while node is disconnected

        if not head:
            return None

        prev = None

        cur = head

        temp = head

        next_n = cur.next

        while cur:
            next_n = cur.next
            temp = cur
            temp.next = prev
            prev = cur
            cur = next_n
            
        
        return prev