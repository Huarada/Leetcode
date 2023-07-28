# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        cur = dummy = ListNode() # creation of dummy node
        while list1 and list2: # making sure that we re not invading memory

            if list1.val < list2.val:
                cur.next = list1 #link the two nodes with smallest numbers in order
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2,cur = list2.next, list2
        
        if list1 or list2:
            cur.next = list1 if list1 else list2
    
        return dummy.next
