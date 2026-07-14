# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow , fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        second_part = slow.next
        slow.next = None
        stk = []
        while second_part:
            stk.append(second_part)
            second_part = second_part.next
        
        
        first_part = head

        
        

        while first_part and stk:
            look_ahead = first_part.next
            first_part.next = stk.pop()
            first_part.next.next = look_ahead
            first_part = look_ahead

            


        