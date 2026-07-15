# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.ans = None
        self.inorder(root , k)
        return self.ans
        
    
    def inorder(self , root , k):
        if not root or self.ans is not None:
            return self.ans
        self.inorder(root.left , k)
        self.count += 1
        if self.count == k:
            self.ans = root.val
        self.inorder(root.right , k)

        