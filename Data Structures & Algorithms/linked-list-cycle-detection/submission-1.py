# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is not None:
            slow = head
            fast = head
        else:
            return False
        
        while slow and fast:
            slow = slow.next if slow and slow.next else None
            fast = fast.next.next if fast.next else None
            if fast == slow and fast and slow:
                return True
        
        return False
            

        