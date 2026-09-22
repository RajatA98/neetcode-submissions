# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #store visited nodes
        visited = set()
        cur = head
        #traverse through the linked list
        while cur:
            #check if we visted already if yes cycle
            if cur in visited:
                return True
            #we are visiting curent node for first time
            visited.add(cur)
            cur = cur.next
        #we have reached the end
        return False