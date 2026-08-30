# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Travese through both lists until one hits null
        #4 pointers needed l1_cur l2_cur and new_head merge_cur

        if not list1:
            return list2
        if not list2:
            return list1

        l1_cur = list1
        l2_cur = list2

        if l1_cur.val <= l2_cur.val:
            new_head = l1_cur
            l1_cur = l1_cur.next
        else:
            new_head = l2_cur
            l2_cur = l2_cur.next
        

        #compare both values and move the head of the merged list

        merged_cur = new_head

        while l1_cur and l2_cur:
            if l1_cur.val <= l2_cur.val:
                merged_cur.next = l1_cur
                l1_cur = l1_cur.next
            else:
                merged_cur.next = l2_cur
                l2_cur = l2_cur.next
            
            merged_cur = merged_cur.next
    
        
        if l1_cur == None:
            merged_cur.next = l2_cur
        else:
            merged_cur.next = l1_cur

        return new_head
