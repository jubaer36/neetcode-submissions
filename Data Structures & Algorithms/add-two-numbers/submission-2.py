# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        node = l3
        node1 = l1
        node2 = l2
        carry_present = False
        while node1 or node2:
            v1 = node1.val if node1 else 0
            v2 = node2.val if node2 else 0
            sum_two_nodes = v1 + v2
            if (sum_two_nodes + carry_present) > 9:
                to_add = (sum_two_nodes + carry_present) % 10
                carry_present = True
            else:
                to_add = (sum_two_nodes + carry_present)
                carry_present = False  
            node.val = to_add
            # print(f"{node1.val} + {node2.val} = {node.val}")
            if node1:
                node1 = node1.next
            if node2:
                node2 = node2.next
            if node1 or node2 or carry_present:
                node.next = ListNode()
                node = node.next
        
        if carry_present:
            node.val = 1
        
        return l3


        