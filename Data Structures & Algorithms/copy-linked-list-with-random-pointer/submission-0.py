"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Taverse through the List creating the copy
        if not head:
            return None
        n_head = Node(head.val,None,None)
       

        cur = head.next
        n_cur = n_head

        c_n = {}
        c_n[head] = n_head
        

        #Build the new list
        while cur:
           
            n_next = Node(cur.val,None,None)
            n_cur.next = n_next
            
            n_cur = n_next
            c_n[cur] = n_cur # map the nodes together 

            cur = cur.next

        #get the correct random traversing the map 

        for og, new in c_n.items():
            if og.random:
                new.random = c_n[og.random]
            else:
                new.random = None

        return n_head


